# Travel Pricing Engine

A comprehensive data engineering solution for processing travel contract data and generating dynamic pricing quotes for multi-city travel packages.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF?style=for-the-badge&logo=duckdb&logoColor=black)

## 🌟 Live Demo

[🚀 View Live Application](https://harshchandan-travel-business-data-platform.streamlit.app/)

## 📋 Overview

The Travel Pricing Engine is a robust data engineering project that transforms raw travel contract spreadsheets into structured pricing data and provides an interactive web interface for creating comprehensive travel package quotes. The system supports multi-city itineraries with customizable hotel accommodations and sightseeing services.

## ✨ Features

### 🔄 Data Pipeline
- **Excel Processing**: Reads and validates travel contract data from Excel spreadsheets
- **Data Cleaning**: Standardizes date formats, handles missing values, and ensures data integrity
- **Parquet Storage**: Efficiently stores processed data in Parquet format for fast querying
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

### 🌐 Interactive Web Interface
- **Cascading Dropdowns**: Intelligent selection based on previous choices
- **Multi-Segment Packages**: Build complex itineraries with multiple cities
- **Real-Time Editing**: Modify existing segments without recreation
- **Comprehensive Quotes**: Detailed cost breakdowns with markup calculations

## 🛠️ Tech Stack

- **Backend**: Python 3.9+
- **Data Processing**: Pandas, DuckDB
- **File Formats**: Excel (openpyxl), Parquet
- **Web Framework**: Streamlit
- **Deployment**: Streamlit Cloud
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

4. **Launch the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📊 Data Sources

### Hotel Data
- **Source**: Excel spreadsheet (`The Vietnam DMC Data Mart.xlsx`)
- **Sheet**: `Hotel Prices`
- **Fields**: City, hotel name, room type, meal plan, pricing, validity dates

### Land Service Data
- **Source**: Excel spreadsheet (`The Vietnam DMC Data Mart.xlsx`)
- **Sheet**: `Land Prices`
- **Fields**: Airport, service type, transport options, pricing, validity dates

### Data Processing
- **Input**: Raw Excel files
- **Output**: Cleaned Parquet files optimized for querying
- **Validation**: Date range checks, data type conversions, null handling

## 🏗️ Architecture

### Data Flow
1. **Raw Data** → Excel files with contract information
2. **Data Pipeline** → Cleaning, validation, and structuring
3. **Pricing Engines** → Business logic for cost calculations
4. **Web Interface** → User interaction and quote generation

### Modular Design
- **Separation of Concerns**: Data, business logic, and presentation layers
- **Reusable Components**: Engines can be used independently
- **Scalable Structure**: Easy to add new services or destinations

## 💡 Usage

### Creating a Travel Package

1. **Set Trip Details**
   - Travel and booking dates
   - Number of passengers (adults, children, infants)

2. **Add Hotel Segments**
   - Select destination city
   - Choose hotel, room type, and meal plan
   - Specify number of rooms and nights
   - Configure land services for that destination

3. **Review and Calculate**
   - View all package components
   - Edit segments as needed
   - Generate final pricing quote

### Supported Destinations
- **Hanoi**: Hotels and city services
- **Da Nang**: Beach resort options
- **Ho Chi Minh City**: Urban accommodations

## 🚀 Deployment

The application is deployed on Streamlit Cloud with automatic updates from the GitHub repository.

### Deployment Features
- **Auto-deployment**: Changes to `main` branch deploy automatically
- **Public Access**: No authentication required
- **Scalable**: Handles multiple concurrent users
- **Data Security**: All processing happens server-side

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