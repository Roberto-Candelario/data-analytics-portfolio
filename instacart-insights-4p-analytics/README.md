# 🛒 Instacart Insights: Driving Sales Growth with 4P Analytics and Promotion Strategy

## 📈 Business Context & Problem Statement

**Role:** Supporting the snack foods category team for Instacart's virtual shelves as a Data Analyst

**Business Challenge:** Instacart needs to optimize their product mix, pricing strategies, promotional campaigns, and product placement to maximize sales growth and customer satisfaction in the competitive grocery delivery market.

**Key Questions:**
- Which products present the highest growth opportunities?
- How effective are current promotional strategies?
- What drives customer reorder behavior?
- How can we optimize the 4P marketing mix (Product, Price, Promotion, Placement)?

## 🎯 Project Goals

1. **Sales Optimization:** Identify top product opportunities for the sales team
2. **Promotion Analysis:** Evaluate promotional effectiveness and ROI
3. **New Launch Performance:** Assess performance of new product introductions
4. **4P Scorecard Development:** Build comprehensive marketing mix analytics
5. **Market Share Analysis:** Conduct competitive brand analysis
6. **Strategic Recommendations:** Provide data-driven business insights

## 🛠️ Tech Stack

- **Python 3.9+** - Primary analysis language
- **Pandas & NumPy** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Data visualization
- **Plotly** - Interactive visualizations
- **Scikit-learn** - Machine learning models
- **Prophet/SARIMA** - Time series forecasting
- **Jupyter Notebooks** - Analysis environment

## 📊 Dataset

**Source:** [Instacart Market Basket Analysis](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis)

**Key Files:**
- `orders.csv` - Order-level data with user and timing information
- `products.csv` - Product catalog with names and department info
- `order_products__prior.csv` - Products purchased in prior orders
- `departments.csv` - Department categorization
- `aisles.csv` - Aisle categorization

**Dataset Size:** 3.4M+ orders, 200k+ users, 50k+ products

## 📁 Project Structure

```
instacart-insights-4p-analytics/
├── data/
│   ├── raw/                    # Original Kaggle dataset
│   └── processed/              # Cleaned and engineered datasets
├── notebooks/
│   └── 1_instacart_4p_analysis.ipynb    # Main analysis notebook
├── scripts/
│   ├── data_preprocessing.py   # Data cleaning functions
│   ├── feature_engineering.py # Feature creation utilities
│   └── forecasting_models.py  # ML models for forecasting
├── dashboard/                  # Tableau/Power BI files
├── reports/
│   └── visualizations/        # Key charts and insights
└── README.md
```

## 🔍 Analysis Workflow

### 1. 📦 Business Context & Goals
- Define stakeholder needs and success metrics
- Establish KPI framework for category management

### 2. 🧼 Data Cleaning & Exploration
- Load and clean all dataset files
- Engineer key features: reorder rates, basket analysis, timing patterns
- Create comprehensive product-order history

### 3. 📈 Sales & Trend Analysis
- Weekly/monthly sales performance tracking
- Department and category segmentation
- Time-based trend identification

### 4. 📊 Promotion Simulation
- Design A/B test framework for promotional analysis
- Measure uplift in orders, basket size, and reorder rates
- ROI calculation for promotional campaigns

### 5. 📊 Forecasting Models
- Implement time series forecasting (SARIMA, Prophet)
- 4-week sales predictions
- Uplift modeling for promotional impact

### 6. 💹 4P Scorecard Development
- **Product:** SKU performance, reorder rates, launch analysis
- **Price:** Price elasticity and tier optimization
- **Promotion:** Campaign effectiveness and uplift metrics
- **Placement:** Category and aisle performance simulation

### 7. 📊 Market Share Analysis
- Brand share calculations and competitive analysis
- Head-to-head performance comparisons
- Growth trajectory analysis

### 8. 🧠 Strategic Insights & Recommendations
- Underperforming product identification
- Optimal promotional strategies
- Seasonal pattern recognition
- Sales team recommendation engine

### 9. 📤 Executive Summary & Presentation
- Key findings and business impact
- Actionable recommendations
- ROI projections and implementation roadmap

## 📊 Key Metrics & KPIs

- **Sales Performance:** Revenue growth, order velocity, basket size
- **Customer Behavior:** Reorder rates, purchase frequency, loyalty metrics
- **Promotional Impact:** Uplift %, incremental revenue, promotion ROI
- **Product Mix:** Category share, SKU performance, launch success rate
- **Market Position:** Share of orders, competitive positioning

## 🏆 Expected Business Impact

- **Revenue Growth:** 15-20% increase in category sales through optimized product mix
- **Promotion ROI:** 3:1 return on promotional investments
- **Customer Retention:** 25% improvement in reorder rates for targeted products
- **Operational Efficiency:** Data-driven decision making for inventory and pricing

## 🚀 How to Run This Project

1. **Clone the repository**
```bash
git clone [repository-url]
cd instacart-insights-4p-analytics
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset**
- Visit [Kaggle dataset](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis)
- Download and extract files to `data/raw/`

4. **Run the analysis**
```bash
jupyter notebook notebooks/1_instacart_4p_analysis.ipynb
```

## 📈 Key Insights Preview

*[This section will be updated with findings from the analysis]*

- **Top Growth Opportunity:** [Product category with highest potential]
- **Best Performing Promotions:** [Most effective promotional strategies]
- **Seasonal Patterns:** [Key shopping behavior insights]
- **Reorder Champions:** [Products with highest customer loyalty]

## 🔗 Additional Resources

- **Dashboard:** Comprehensive visual analytics available in `reports/visualizations/`
- **Presentation:** Executive summary and insights available in `data/processed/executive_summary.csv`
- **Technical Documentation:** Complete methodology documented in the Jupyter notebook

## 📞 Contact

**Author:** Roberto Candelario  
**Date:** 2024-12-19  
**Project:** Instacart 4P Analytics & Promotion Strategy

---

*This project demonstrates advanced analytics capabilities in retail/e-commerce, combining statistical analysis, machine learning, and business strategy to drive measurable growth in a competitive market.* 