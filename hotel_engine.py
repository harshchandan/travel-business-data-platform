import pandas as pd
import os

# Load hotel rates data
hotel_df = pd.read_parquet('data/marts/hotel_rates.parquet')

def calculate_hotel_cost(city, hotel_name, room_name, meal_plan, rooms, nights, travel_date, booking_date, adults, child_4_5, child_6_8, child_9_11, infants):
    """
    Calculate hotel cost based on parameters.
    """
    # Filter valid contracts
    valid_contracts = hotel_df[
        (hotel_df['travel_valid_from'] <= travel_date) &
        (hotel_df['travel_valid_to'] >= travel_date) &
        (hotel_df['booking_valid_from'] <= booking_date) &
        (hotel_df['booking_valid_to'] >= booking_date)
    ]
    
    # Match specific hotel details
    matching_row = valid_contracts[
        (valid_contracts['city'] == city) &
        (valid_contracts['hotel_name'] == hotel_name) &
        (valid_contracts['room_name'] == room_name) &
        (valid_contracts['meal_plan'] == meal_plan)
    ]
    
    if matching_row.empty:
        raise ValueError("No valid hotel contract found for the given parameters.")
    
    # Assume one matching row
    row = matching_row.iloc[0]
    
    # Base cost for 2 pax
    base_cost = row['price_2pax'] * rooms * nights
    
    # Extra costs
    extra_adults = max(0, adults - 2)
    extra_cost = (row['extra_adult_price'] * extra_adults +
                  row['extra_child_price'] * (child_4_5 + child_6_8 + child_9_11) +
                  row['extra_infant_price'] * infants) * rooms * nights
    
    total_hotel_cost = base_cost + extra_cost
    return total_hotel_cost