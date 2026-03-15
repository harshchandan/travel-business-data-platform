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

# Initialize session state for hotel segments and editing
if 'hotel_segments' not in st.session_state:
    st.session_state.hotel_segments = []
if 'editing_index' not in st.session_state:
    st.session_state.editing_index = -1

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

# Add/Edit Hotel Segment
st.header("Add/Edit Hotel Segment")

# Define cities for use in the form
cities = sorted(hotel_df['city'].unique())

with st.expander("Add New Segment" if st.session_state.editing_index == -1 else "Edit Segment"):
    # Set defaults based on editing
    if st.session_state.editing_index != -1:
        seg = st.session_state.hotel_segments[st.session_state.editing_index]
        city_default = seg['city']
        hotel_default = seg['hotel_name']
        room_default = seg['room_name']
        meal_default = seg['meal_plan']
        rooms_default = seg['rooms']
        nights_default = seg['nights']
        transport_default = seg['transport_type']
        vehicle_default = seg['vehicle_type']
        services_default = seg['selected_services']
    else:
        city_default = cities[0]
        hotel_default = ""
        room_default = ""
        meal_default = ""
        rooms_default = 1
        nights_default = 1
        transport_default = "PVT"
        vehicle_default = ""
        services_default = []
    
    # City selection
    city_index = cities.index(city_default) if city_default in cities else 0
    city = st.selectbox("City", cities, index=city_index, key="add_city")
    
    # Hotel selection based on city
    hotels_in_city = hotel_df[hotel_df['city'] == city]['hotel_name'].unique()
    hotel_index = sorted(hotels_in_city).index(hotel_default) if hotel_default in hotels_in_city else 0
    hotel_name = st.selectbox("Hotel Name", sorted(hotels_in_city), index=hotel_index, key="add_hotel")
    
    # Room selection based on hotel
    rooms_in_hotel = hotel_df[(hotel_df['city'] == city) & (hotel_df['hotel_name'] == hotel_name)]['room_name'].unique()
    room_index = sorted(rooms_in_hotel).index(room_default) if room_default in rooms_in_hotel else 0
    room_name = st.selectbox("Room Name", sorted(rooms_in_hotel), index=room_index, key="add_room")
    
    # Meal plan selection based on room
    meal_plans = hotel_df[(hotel_df['city'] == city) & (hotel_df['hotel_name'] == hotel_name) & (hotel_df['room_name'] == room_name)]['meal_plan'].unique()
    meal_index = sorted(meal_plans).index(meal_default) if meal_default in meal_plans else 0
    meal_plan = st.selectbox("Meal Plan", sorted(meal_plans), index=meal_index, key="add_meal")
    
    rooms = st.number_input("Number of Rooms", min_value=1, value=rooms_default, key="add_rooms")
    nights = st.number_input("Number of Nights", min_value=1, value=nights_default, key="add_nights")
    
    # Land services for this segment
    st.subheader("Land Services for this Segment")
    transport_index = ["PVT", "SIC"].index(transport_default) if transport_default in ["PVT", "SIC"] else 0
    transport_type = st.selectbox("Transport Type", ["PVT", "SIC"], index=transport_index, key="add_transport")
    
    if transport_type == "PVT":
        vehicle_types = sorted(land_df['vehicle_type'].dropna().unique())
        vehicle_index = vehicle_types.index(vehicle_default) if vehicle_default in vehicle_types else 0
        vehicle_type = st.selectbox("Vehicle Type", vehicle_types, index=vehicle_index, key="add_vehicle")
    else:
        vehicle_type = "NA"
    
    # Services for the area (assuming city == area)
    airport = [k for k, v in airport_areas.items() if v == city][0]
    services_in_area = land_df[land_df['airport'] == airport]['service_name'].unique()
    services_indices = [sorted(services_in_area).index(s) for s in services_default if s in services_in_area]
    selected_services = st.multiselect("Selected Services", sorted(services_in_area), default=services_default, key="add_services")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.editing_index != -1:
            if st.button("Update Segment"):
                st.session_state.hotel_segments[st.session_state.editing_index] = {
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
                st.session_state.editing_index = -1
                st.success("Segment updated!")
                st.rerun()
        else:
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
    
    with col2:
        if st.session_state.editing_index != -1:
            if st.button("Cancel Edit"):
                st.session_state.editing_index = -1

# Display and manage hotel segments
st.header("Hotel Segments")
if st.session_state.hotel_segments:
    for i, seg in enumerate(st.session_state.hotel_segments):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**Segment {i+1}**: {seg['city']} - {seg['hotel_name']} - {seg['room_name']} ({seg['meal_plan']}) - {seg['rooms']} rooms - {seg['nights']} nights")
            st.write(f"Land: {seg['transport_type']} - {seg['vehicle_type']} - Services: {', '.join(seg['selected_services']) if seg['selected_services'] else 'None'}")
        with col2:
            if st.button("Edit", key=f"edit_{i}"):
                st.session_state.editing_index = i
        with col3:
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