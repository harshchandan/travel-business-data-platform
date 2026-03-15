# Travel Pricing Engine

A comprehensive data engineering solution for processing travel contract data and generating dynamic pricing quotes for multi-city travel packages.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF?style=for-the-badge&logo=duckdb&logoColor=black)

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

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/harshchandan/travel-business-data-platform.git
   cd travel-business-data-platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the data pipeline**
   ```bash
   python data_pipeline.py
   ```

4. **Run the pricing engines**
   ```bash
   # Import and use the pricing engines in your Python code
   from hotel_engine import calculate_hotel_cost
   from land_engine import calculate_land_cost
   from pricing_engine import calculate_total_cost
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

## 💡 Usage

### Using the Pricing Engines

```python
from hotel_engine import calculate_hotel_cost
from land_engine import calculate_land_cost
from pricing_engine import calculate_total_cost
import pandas as pd

# Load processed data
hotel_df = pd.read_parquet('data/marts/hotel_rates.parquet')
land_df = pd.read_parquet('data/marts/land_services.parquet')

# Calculate hotel cost
hotel_cost = calculate_hotel_cost(
    city="Hanoi",
    hotel_name="hanoi_hotel_1",
    room_name="room_name_1",
    meal_plan="CP",
    rooms=2,
    nights=3,
    travel_date=pd.Timestamp("2026-03-20"),
    booking_date=pd.Timestamp("2026-03-15"),
    adults=2,
    child_4_5=1,
    child_6_8=0,
    child_9_11=0,
    infants=0
)

# Calculate land cost
land_cost = calculate_land_cost(
    airport="HAN",
    selected_services=["HAN Airport Pick Up - Hanoi"],
    transport_type="PVT",
    vehicle_type="4 Seater",
    travel_date=pd.Timestamp("2026-03-20"),
    booking_date=pd.Timestamp("2026-03-15"),
    adults=2,
    child_4_5=1,
    child_6_8=0,
    child_9_11=0,
    infants=0
)

# Calculate final price with markup
total_cost, final_price = calculate_total_cost(hotel_cost, land_cost, markup_percentage=10.0)
```

### Supported Destinations
- **Hanoi**: Hotels and city services
- **Da Nang**: Beach resort options
- **Ho Chi Minh City**: Urban accommodations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Ensure data pipeline handles edge cases

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web app framework
- **Pandas**: For powerful data manipulation capabilities
- **Vietnam DMC Data**: For providing the sample travel data
- **Open Source Community**: For the incredible tools that make this possible

## 📞 Contact

**Harsh Chandan**
- GitHub: [@harshchandan](https://github.com/harshchandan)
- LinkedIn: [Your LinkedIn Profile]
- Email: your.email@example.com

---

⭐ **Star this repository** if you find it useful!

*Built with ❤️ for the data engineering community*