import pandas as pd
import os

def load_and_clean_data():
    # Read Excel file
    excel_file = 'data/raw/The Vietnam DMC Data Mart.xlsx'
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"Excel file not found: {excel_file}")
    
    # Read sheets
    hotel_df = pd.read_excel(excel_file, sheet_name='Hotel Prices')
    land_df = pd.read_excel(excel_file, sheet_name='Land Prices')
    
    # Clean and standardize hotel data
    hotel_df['travel_valid_from'] = pd.to_datetime(hotel_df['travel_valid_from'])
    hotel_df['travel_valid_to'] = pd.to_datetime(hotel_df['travel_valid_to'])
    hotel_df['booking_valid_from'] = pd.to_datetime(hotel_df['booking_valid_from'])
    hotel_df['booking_valid_to'] = pd.to_datetime(hotel_df['booking_valid_to'])
    
    # Convert price columns to float
    price_cols = ['price_2pax', 'extra_adult_price', 'extra_child_price', 'extra_infant_price']
    for col in price_cols:
        hotel_df[col] = pd.to_numeric(hotel_df[col], errors='coerce')
    
    # Clean and standardize land data
    land_df['travel_valid_from'] = pd.to_datetime(land_df['travel_valid_from'])
    land_df['travel_valid_to'] = pd.to_datetime(land_df['travel_valid_to'])
    land_df['booking_valid_from'] = pd.to_datetime(land_df['booking_valid_from'])
    land_df['booking_valid_to'] = pd.to_datetime(land_df['booking_valid_to'])
    
    land_df['price'] = pd.to_numeric(land_df['price'], errors='coerce')
    
    return hotel_df, land_df

def save_to_staging(hotel_df, land_df):
    # Ensure staging directory exists
    os.makedirs('data/staging', exist_ok=True)
    
    # Save to Parquet
    hotel_df.to_parquet('data/staging/hotel.parquet')
    land_df.to_parquet('data/staging/land.parquet')

def create_pricing_marts(hotel_df, land_df):
    # Ensure marts directory exists
    os.makedirs('data/marts', exist_ok=True)
    
    # For now, pricing marts are the cleaned data
    # In a real scenario, this might involve aggregations or transformations
    hotel_df.to_parquet('data/marts/hotel_rates.parquet')
    land_df.to_parquet('data/marts/land_services.parquet')

if __name__ == "__main__":
    hotel_df, land_df = load_and_clean_data()
    save_to_staging(hotel_df, land_df)
    create_pricing_marts(hotel_df, land_df)
    print("Data pipeline completed successfully.")