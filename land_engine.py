import pandas as pd
import math

# Load land services data
land_df = pd.read_parquet('data/marts/land_services.parquet')

def get_vehicle_capacity(vehicle_type):
    """
    Get vehicle capacity from vehicle_type string.
    """
    if pd.isna(vehicle_type) or vehicle_type == 'NA':
        return 1
    if '4' in vehicle_type:
        return 4
    elif '7' in vehicle_type:
        return 7
    elif '16' in vehicle_type:
        return 16
    elif '29' in vehicle_type:
        return 29
    else:
        return 1  # Default

def calculate_land_cost(airport, selected_services, transport_type, vehicle_type, travel_date, booking_date, adults, child_4_5, child_6_8, child_9_11, infants):
    """
    Calculate land services cost.
    selected_services: list of service_name strings
    """
    # Filter valid contracts
    valid_contracts = land_df[
        (land_df['travel_valid_from'] <= travel_date) &
        (land_df['travel_valid_to'] >= travel_date) &
        (land_df['booking_valid_from'] <= booking_date) &
        (land_df['booking_valid_to'] >= booking_date) &
        (land_df['airport'] == airport)
    ]
    
    total_land_cost = 0.0
    
    # Pax counts
    pax_counts = {
        'adult': adults,
        'child_4_5': child_4_5,
        'child_6_8': child_6_8,
        'child_9_11': child_9_11,
        'infant': infants  # Assuming 'infant' for infants, or adjust if different
    }
    
    total_pax = sum(pax_counts.values())
    
    for service in selected_services:
        service_rows = valid_contracts[valid_contracts['service_name'] == service]
        
        if transport_type == 'SIC':
            # Per passenger
            for _, row in service_rows.iterrows():
                if row['transport_type'] == 'SIC':
                    pax_type = row['pax_type']
                    if pax_type in pax_counts:
                        total_land_cost += row['price'] * pax_counts[pax_type]
        
        elif transport_type == 'PVT':
            # Per vehicle
            matching_rows = service_rows[
                (service_rows['transport_type'] == 'PVT') &
                (service_rows['vehicle_type'] == vehicle_type)
            ]
            if not matching_rows.empty:
                row = matching_rows.iloc[0]  # Assume one
                capacity = get_vehicle_capacity(vehicle_type)
                num_vehicles = math.ceil(total_pax / capacity) if capacity > 0 else 1
                total_land_cost += row['price'] * num_vehicles
    
    return total_land_cost