import streamlit as st
from datetime import datetime
import pandas as pd
import hotel_engine
import land_engine
import pricing_engine

# Static mapping of airports to areas
airport_areas = {
    'HAN': 'Hanoi',
    'SGN': 'Ho Chi Minh City', 
    'DAD': 'Da Nang'
}

# Load data
hotel_df = pd.read_parquet('data/marts/hotel_rates.parquet')
land_df = pd.read_parquet('data/marts/land_services.parquet')

st.title("Travel Pricing Engine")

# Initialize session state for hotel segments
if 'hotel_segments' not in st.session_state:
    st.session_state.hotel_segments = []

st.sidebar.header("Trip Parameters")

# Overall trip dates and passengers
travel_date = st.sidebar.date_input("Travel Date", datetime.today())
booking_date = st.sidebar.date_input("Booking Date", datetime.today())
adults = st.sidebar.number_input("Adults", min_value=0, value=2)
child_4_5 = st.sidebar.number_input("Children 4-5", min_value=0, value=0)
child_6_8 = st.sidebar.number_input("Children 6-8", min_value=0, value=0)
child_9_11 = st.sidebar.number_input("Children 9-11", min_value=0, value=0)
infants = st.sidebar.number_input("Infants", min_value=0, value=0)

# Markup
markup_percentage = st.sidebar.number_input("Markup Percentage", min_value=0.0, value=10.0)

# Add Hotel Segment
st.header("Add Hotel Segment")
with st.expander("Add New Hotel Segment"):
    # City selection
    cities = sorted(hotel_df['city'].unique())
    city = st.selectbox("City", cities, key="add_city")
    
    # Hotel selection based on city
    hotels_in_city = hotel_df[hotel_df['city'] == city]['hotel_name'].unique()
    hotel_name = st.selectbox("Hotel Name", sorted(hotels_in_city), key="add_hotel")
    
    # Room selection based on hotel
    rooms_in_hotel = hotel_df[(hotel_df['city'] == city) & (hotel_df['hotel_name'] == hotel_name)]['room_name'].unique()
    room_name = st.selectbox("Room Name", sorted(rooms_in_hotel), key="add_room")
    
    # Meal plan selection based on room
    meal_plans = hotel_df[(hotel_df['city'] == city) & (hotel_df['hotel_name'] == hotel_name) & (hotel_df['room_name'] == room_name)]['meal_plan'].unique()
    meal_plan = st.selectbox("Meal Plan", sorted(meal_plans), key="add_meal")
    
    rooms = st.number_input("Number of Rooms", min_value=1, value=1, key="add_rooms")
    nights = st.number_input("Number of Nights", min_value=1, value=1, key="add_nights")
    
    # Land services for this segment
    st.subheader("Land Services for this Segment")
    transport_type = st.selectbox("Transport Type", ["PVT", "SIC"], key="add_transport")
    
    if transport_type == "PVT":
        vehicle_types = sorted(land_df['vehicle_type'].dropna().unique())
        vehicle_type = st.selectbox("Vehicle Type", vehicle_types, key="add_vehicle")
    else:
        vehicle_type = "NA"
    
    # Services for the area (assuming city == area)
    airport = [k for k, v in airport_areas.items() if v == city][0]
    services_in_area = land_df[land_df['airport'] == airport]['service_name'].unique()
    selected_services = st.multiselect("Selected Services", sorted(services_in_area), key="add_services")
    
    if st.button("Add Segment"):
        segment = {
            'city': city,
            'hotel_name': hotel_name,
            'room_name': room_name,
            'meal_plan': meal_plan,
            'rooms': rooms,
            'nights': nights,
            'transport_type': transport_type,
            'vehicle_type': vehicle_type,
            'selected_services': selected_services,
            'airport': airport
        }
        st.session_state.hotel_segments.append(segment)
        st.success("Hotel segment with land services added!")

# Display and manage hotel segments
st.header("Hotel Segments")
if st.session_state.hotel_segments:
    for i, seg in enumerate(st.session_state.hotel_segments):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**Segment {i+1}**: {seg['city']} - {seg['hotel_name']} - {seg['room_name']} ({seg['meal_plan']}) - {seg['rooms']} rooms - {seg['nights']} nights")
            st.write(f"Land: {seg['transport_type']} - {seg['vehicle_type']} - Services: {', '.join(seg['selected_services']) if seg['selected_services'] else 'None'}")
        with col2:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.hotel_segments.pop(i)
                st.rerun()
else:
    st.write("No hotel segments added yet.")

if st.button("Calculate Quote"):
    if st.session_state.hotel_segments:
        try:
            # Convert dates
            travel_dt = datetime.combine(travel_date, datetime.min.time())
            booking_dt = datetime.combine(booking_date, datetime.min.time())
            
            # Calculate total costs
            total_hotel_cost = 0.0
            total_land_cost = 0.0
            for seg in st.session_state.hotel_segments:
                # Hotel cost
                hotel_cost = hotel_engine.calculate_hotel_cost(
                    seg['city'], seg['hotel_name'], seg['room_name'], seg['meal_plan'], 
                    seg['rooms'], seg['nights'], travel_dt, booking_dt,
                    adults, child_4_5, child_6_8, child_9_11, infants
                )
                total_hotel_cost += hotel_cost
                
                # Land cost for this segment
                land_cost = land_engine.calculate_land_cost(
                    seg['airport'], seg['selected_services'], seg['transport_type'], seg['vehicle_type'], 
                    travel_dt, booking_dt, adults, child_4_5, child_6_8, child_9_11, infants
                )
                total_land_cost += land_cost
            
            total_cost, final_price = pricing_engine.calculate_total_cost(total_hotel_cost, land_cost, markup_percentage)
            
            # Display results
            st.header("Pricing Quote")
            st.write(f"Total Hotel Cost: ${total_hotel_cost:.2f}")
            st.write(f"Total Land Cost: ${total_land_cost:.2f}")
            st.write(f"Total Cost: ${total_cost:.2f}")
            st.write(f"Final Price (with {markup_percentage}% markup): ${final_price:.2f}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please add at least one hotel segment before calculating.")