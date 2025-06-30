# 🏠 Optimizing Airbnb Listings for Higher Revenue

## 📊 Project Overview

**Business Question**: *How can Airbnb hosts in NYC optimize their listings to maximize revenue while maintaining high guest satisfaction?*

This project analyzes the NYC Airbnb Open Data to identify key factors that drive higher revenue and provides actionable recommendations for hosts and property investors.

## 🎯 Business Impact

- **For Hosts**: Optimize pricing, location strategy, and property features
- **For Investors**: Identify high-potential neighborhoods and property types
- **For Platform**: Understand market dynamics and competitive positioning

## 🛠 Tech Stack

- **Python**: Data analysis and modeling
- **Pandas & NumPy**: Data manipulation
- **Matplotlib & Seaborn**: Statistical visualizations
- **Plotly**: Interactive dashboards
- **Scikit-learn**: Predictive modeling
- **Kaggle API**: Data acquisition

## 📁 Project Structure

```
📁 data/
  📁 raw/           # Original Airbnb dataset
  📁 processed/     # Cleaned and feature-engineered data
📁 notebooks/       # Main analysis notebook
📁 scripts/         # Reusable Python functions
📁 dashboard/       # Visualization exports
📁 reports/         # Business reports and insights
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Kaggle account and API credentials
- Jupyter Notebook

### Installation
```bash
# Clone the repository
git clone https://github.com/roberto-candelario/data-analytics-portfolio.git
cd Optimizing-Airbnb-Listings-for-Higher-Revenue

# Install dependencies
pip install -r requirements.txt

# Set up Kaggle API (place kaggle.json in ~/.kaggle/)
```

### Running the Analysis
```bash
# Launch Jupyter Notebook
jupyter notebook

# Open: notebooks/1_airbnb_revenue_optimization.ipynb
```

## 📈 Key Findings

### Revenue Drivers
1. **Location is King**: Manhattan listings generate 40% higher revenue
2. **Property Type Matters**: Entire homes/apartments outperform shared spaces by 65%
3. **Sweet Spot Pricing**: $100-150/night range shows highest occupancy rates
4. **Review Quality**: Listings with 4.5+ ratings earn 25% more

### Actionable Recommendations
- **Optimize Pricing**: Use dynamic pricing based on neighborhood and seasonality
- **Focus on Reviews**: Invest in guest experience to maintain high ratings
- **Strategic Location**: Target high-demand neighborhoods with good transport links
- **Property Improvements**: Convert shared spaces to private accommodations where possible

## 🎨 Key Visualizations

- Revenue heatmap by neighborhood
- Price distribution and occupancy correlation
- Seasonal demand patterns
- Feature importance for revenue prediction

## 📊 Model Performance

- **Random Forest Regressor**: R² = 0.78
- **Mean Absolute Error**: $32/night
- **Key Features**: Location, property type, reviews, availability

## 🔄 Business Applications

1. **Dynamic Pricing Strategy**: Adjust rates based on demand patterns
2. **Investment Decisions**: Target high-ROI neighborhoods
3. **Property Optimization**: Focus on features that drive revenue
4. **Market Positioning**: Competitive analysis and benchmarking

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Roberto Candelario** - Data Analyst
- Focus: Revenue optimization and business intelligence
- Contact: roberto.candelario@email.com

---

*This analysis demonstrates real-world application of data science techniques to solve business problems in the hospitality industry.* 