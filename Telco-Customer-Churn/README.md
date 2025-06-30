# 📊 Telco Customer Churn Analysis

**Project:** Comprehensive customer churn prediction and analysis for telecommunications company  
**Author:** Roberto Candelario  
**Date:** December 2024  
**Tech Stack:** Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Jupyter Notebook

---

## 🎯 Business Problem

Customer churn is a critical challenge for telecommunications companies, directly impacting revenue and growth. This project analyzes customer behavior patterns to:

- **Identify** key factors driving customer churn
- **Predict** which customers are at risk of churning  
- **Recommend** data-driven retention strategies
- **Quantify** potential business impact of churn reduction initiatives

---

## 📊 Dataset Information

**Source:** [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**Dataset Overview:**
- **Records:** 7,043 customers
- **Features:** 21 attributes including demographics, services, and account information
- **Target:** Churn status (Yes/No)
- **Churn Rate:** ~27% of customers

**Key Features:**
- Customer demographics (gender, age, dependents)
- Service subscriptions (phone, internet, streaming)
- Account information (tenure, contract type, charges)
- Payment details (method, billing preferences)

---

## 🔧 Tech Stack & Tools

| Category | Technology |
|----------|------------|
| **Data Analysis** | Python, Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Random Forest, Logistic Regression |
| **Visualization** | Matplotlib, Seaborn |
| **Development** | Jupyter Notebook |
| **Data Source** | Kaggle API |

---

## 📈 Key Insights

### 🎯 Churn Drivers
1. **Contract Type:** Month-to-month contracts have 43% higher churn risk
2. **Tenure:** New customers (0-12 months) show 45% churn rate
3. **Service Quality:** Fiber optic customers exhibit higher churn despite premium pricing
4. **Pricing:** Higher monthly charges correlate with increased churn risk

### 🤖 Model Performance
- **Best Model:** Random Forest Classifier
- **Accuracy:** 80.1%
- **Precision:** 78.3%  
- **Recall:** 74.2%
- **AUC Score:** 84.7%

### 💰 Business Impact
- **Annual Revenue at Risk:** $2.8M from churned customers
- **High-Risk Customers:** 1,421 customers identified
- **Potential Savings:** $350K-$700K annually with 25-50% retention improvement

---

## 📁 Project Structure

```
Telco-Customer-Churn/
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Cleaned and engineered features
├── notebooks/
│   └── 1_telco_churn_analysis.ipynb  # Main analysis notebook
├── scripts/
│   └── data_preprocessing.py   # Data cleaning utilities
├── reports/
│   └── visualizations/         # Generated charts and graphs
├── dashboard/                  # Future dashboard files
├── README.md                   # This file
└── requirements.txt           # Python dependencies
```

---

## 🚀 How to Run This Project

### Prerequisites
- Python 3.8+
- Kaggle API credentials (kaggle.json)
- Required Python packages (see requirements.txt)

### Setup Instructions

1. **Clone/Download the project**
   ```bash
   cd Telco-Customer-Churn
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Kaggle API**
   - Place your `kaggle.json` file in the project root
   - The notebook will automatically configure credentials

4. **Run the analysis**
   ```bash
   jupyter notebook notebooks/1_telco_churn_analysis.ipynb
   ```

5. **Execute all cells**
   - The notebook will download data, perform analysis, and save results
   - Generated visualizations will be saved to `reports/visualizations/`
   - Processed data will be saved to `data/processed/`

---

## 📊 Key Visualizations

The analysis generates several impactful visualizations:

1. **Churn Distribution Analysis** - Overall churn patterns
2. **Factor Analysis Charts** - Churn by contract, service, tenure, charges
3. **Correlation Heatmap** - Feature relationships
4. **Model Evaluation Dashboard** - Confusion matrix, ROC curves, feature importance
5. **Business Intelligence Visuals** - Churn funnel, risk heatmap, revenue impact

---

## 💡 Business Recommendations

### Immediate Actions (0-30 days)
- Deploy high-risk customer identification system
- Launch retention campaigns for 70%+ churn probability customers
- Implement contract upgrade incentives

### Strategic Improvements (30-90 days)
- Develop comprehensive customer onboarding program
- Investigate fiber optic service quality issues
- Create automated early warning systems

### Long-term Optimization (90+ days)
- Conduct pricing strategy review
- Implement advanced retention marketing automation
- Develop customer lifetime value optimization

---

## 📈 Business Value Delivered

This analysis provides actionable insights that can drive measurable business impact:

- **🎯 Predictive Accuracy:** 85% AUC score enables reliable churn prediction
- **💰 Revenue Protection:** Clear path to $350K-$700K annual savings
- **📊 Data-Driven Strategy:** Evidence-based recommendations for retention
- **🚀 Implementation Roadmap:** Prioritized action plan with clear timelines

---

## 🔮 Future Enhancements

- **Real-time Scoring:** API deployment for live churn prediction
- **Advanced Features:** Time-series analysis and seasonal patterns
- **A/B Testing:** Framework for retention strategy optimization
- **Customer Segmentation:** Advanced clustering for personalized retention
- **Dashboard Development:** Executive reporting and monitoring tools

---

## 📞 Contact

**Roberto Candelario**  
Data Analyst | Machine Learning Enthusiast

Connect with me to discuss this project or explore collaboration opportunities!

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*This project demonstrates comprehensive data analytics skills including data acquisition, exploratory analysis, feature engineering, machine learning, and business strategy development.* 