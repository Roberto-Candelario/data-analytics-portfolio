# Instacart Market Basket Analysis Dataset

## Dataset Overview
Source: https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis
Description: Anonymized data of 3 million grocery orders from more than 200,000 Instacart users

## File Structure

### Raw Data (data/raw/)
- orders.csv - Order-level information (3.4M orders)
- products.csv - Product catalog (50K products)  
- order_products__prior.csv - Products in prior orders (32M records)
- departments.csv - Department categories (21 departments)
- aisles.csv - Aisle categories (134 aisles)

### Processed Data (data/processed/)
- master_dataset.csv - Complete joined dataset with all features
- snacks_dataset.csv - Filtered dataset for snacks category analysis
- reorder_stats.csv - Product-level reorder statistics
- sales_forecasts.csv - 4-week sales predictions
- 4p_scorecard.csv - Marketing mix analysis results
- promotion_simulation_results.csv - Promotional campaign analysis
- market_share_by_department.csv - Department market share data
- strategic_recommendations.csv - Business recommendations

## Key Fields Explained

### Orders Data
- order_id: Unique order identifier
- user_id: Customer identifier (anonymized)
- order_number: Sequence number for user (1 = first order)
- order_dow: Day of week (0=Sunday, 6=Saturday)
- order_hour_of_day: Hour of day (0-23)
- days_since_prior_order: Days since last order

### Products Data
- product_id: Unique product identifier
- product_name: Product name
- aisle_id: Aisle category
- department_id: Department category

### Order Products Data
- order_id: Links to orders.csv
- product_id: Links to products.csv
- add_to_cart_order: Order product was added to cart
- reordered: 1 if reordered, 0 if first time

## Usage Notes

1. Download raw data from Kaggle and place in data/raw/
2. Run data_preprocessing.py to create processed datasets
3. Use processed datasets for analysis in Jupyter notebooks
4. All visualizations saved to reports/visualizations/

## Data Quality
- No missing values in key fields
- All foreign keys properly linked
- Anonymized for privacy compliance
- Represents real shopping behavior patterns 