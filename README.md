## 📋 Overview

The Travel Pricing Engine is a robust data engineering project that transforms travel contract data into structured pricing data and provides modular pricing engines for calculating comprehensive travel package quotes. The system supports multi-city itineraries with customizable hotel accommodations and sightseeing services.

## ✨ Features

### 🔄 Data Pipeline
- **Data Processing**: Reads and validates travel contract data
- **Data Cleaning**: Standardizes date formats, handles missing values, and ensures data integrity
- **Structured Storage**: Efficiently stores processed data for fast querying
- **Modular Design**: Separate processing for hotel and land service data

### 🏨 Hotel Pricing Engine
- **Dynamic Pricing**: Calculates costs based on room types, meal plans, and passenger counts
- **Date Validation**: Ensures contracts are valid for selected travel dates
- **Extra Charges**: Handles additional adult, child, and infant pricing
- **Multi-City Support**: Processes packages spanning multiple destinations

### 🚗 Land Service Pricing
- **Transport Options**: Supports Private (PVT) and Shared (SIC) transportation
- **Sightseeing Packages**: Multiple sightseeing options per destination
- **Vehicle Capacity**: Automatic vehicle allocation based on passenger counts
- **Area-Based Selection**: Services organized by geographic areas

## 🛠️ Tech Stack

- **Backend**: Python 3.9+
- **Data Processing**: Pandas, DuckDB
- **Version Control**: Git

## 📁 Project Structure

```
travel-pricing-engine/
├── app.py                 # Main Streamlit application
├── data_pipeline.py       # Data processing and cleaning pipeline
├── hotel_engine.py        # Hotel pricing calculations
├── land_engine.py         # Land service pricing calculations
├── pricing_engine.py      # Final pricing and markup logic
├── requirements.txt       # Python dependencies
├── data/
│   ├── raw/              # Raw Excel data files
│   ├── staging/          # Intermediate processed data
│   └── marts/            # Final structured data for pricing
└── README.md             # Project documentation
```


## 🏗️ Architecture

### Data Flow
1. **Data Processing** → Cleaning, validation, and structuring
2. **Pricing Engines** → Business logic for cost calculations
4. **Web Interface** → User interaction and quote generation

### Modular Design
- **Separation of Concerns**: Data, business logic, and presentation layers
- **Reusable Components**: Engines can be used independently
- **Scalable Structure**: Easy to add new services or destinations
