## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
# 📈 Sales Horizon

An intuitive sales forecasting dashboard built with Python and Streamlit. Sales Horizon provides powerful time series forecasting capabilities with an easy-to-use interface for visualizing sales trends and predicting future performance.

## Features

- **Multiple Forecasting Methods**
  - Exponential Smoothing (Holt-Winters)
  - Moving Average
  - Naive Forecasting

- **Interactive Dashboard**
  - Real-time sales visualization
  - Customizable forecast horizons (7-90 days)
  - Confidence intervals for predictions
  - Historical trend analysis

- **Comprehensive Analytics**
  - Sales distribution analysis
  - Weekly and monthly patterns
  - Forecast accuracy metrics (MAE, RMSE, MAPE)
  - Residual analysis

- **Flexible Data Input**
  - Generate sample data for testing
  - Upload your own CSV files
  - Filter by product category and region

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sales-horizon.git
cd sales-horizon
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Using Your Own Data

Your CSV file should have the following structure:
```csv
date,sales,product_category,region
2023-01-01,15000,Electronics,North
2023-01-02,18500,Electronics,South
2023-01-03,12000,Clothing,East
```

**Required columns:**
- `date`: Date in YYYY-MM-DD format
- `sales`: Numerical sales values

**Optional columns:**
- `product_category`: Product categories for filtering
- `region`: Geographic regions for filtering

### Configuration Options

#### Sidebar Controls

- **Data Source**: Choose between sample data or CSV upload
- **Forecast Horizon**: Select prediction period (7-90 days)
- **Forecasting Method**: Choose your preferred algorithm
- **Filters**: Filter data by category and region

#### Forecasting Methods

1. **Exponential Smoothing**: Best for data with trend and seasonality
2. **Moving Average**: Simple method for stable trends
3. **Naive Forecast**: Uses last known value as prediction

## Features Explanation

### Dashboard Tabs

#### 📊 Forecast Tab
- Visual representation of historical and forecasted sales
- 95% confidence intervals
- Forecast summary table
- Key insights and metrics

#### 📈 Trends Tab
- Sales distribution histogram
- Day-of-week analysis
- Monthly trend visualization

#### 🎯 Accuracy Tab
- Forecast accuracy metrics
- Residuals analysis
- Actual vs Predicted scatter plot

#### 📋 Data Tab
- View historical data
- Download data as CSV
- Data statistics

## Project Structure
```
sales-horizon/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
├── LICENSE               # License file
└── data/                 # Sample data directory (optional)
    └── sample_sales.csv
```

## Metrics Explained

- **MAE (Mean Absolute Error)**: Average magnitude of forecast errors
- **RMSE (Root Mean Square Error)**: Standard deviation of forecast errors
- **MAPE (Mean Absolute Percentage Error)**: Average percentage error

Lower values indicate better forecast accuracy.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue**: Insufficient data error
- **Solution**: Ensure your dataset has at least 14 days of historical data

**Issue**: Forecast generation fails
- **Solution**: Check for missing values or inconsistent date formatting in your data

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Time series forecasting powered by [statsmodels](https://www.statsmodels.org/)
- Visualizations created with [Plotly](https://plotly.com/)

## Roadmap

Future enhancements planned:
- [ ] ARIMA and Prophet forecasting methods
- [ ] Multi-product forecasting
- [ ] Export forecast reports to PDF
- [ ] API integration for real-time data
- [ ] Seasonal decomposition analysis
- [ ] Anomaly detection
- [ ] Collaborative forecasting with team comments

---

Made with ❤️ using Python and Streamlit
```

## .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/
.venv

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Jupyter Notebooks
.ipynb_checkpoints

# Environment variables
.env
.env.local

# OS
.DS_Store
Thumbs.db

# Data files (optional - uncomment if you don't want to track data)
# data/*.csv
# data/*.xlsx

# Streamlit
.streamlit/secrets.toml

# Logs
*.log

# Testing
.pytest_cache/
.coverage
htmlcov/
```

## 📂 Project Structure


