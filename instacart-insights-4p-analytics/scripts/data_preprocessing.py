# Project: Instacart 4P Analytics & Promotion Strategy
# Author: Roberto Candelario
# Date: 2024-12-19
# Description: Data preprocessing utilities for Instacart analysis

import pandas as pd
import os


def load_instacart_data(data_path='../data/raw/'):
    """
    Load all Instacart dataset files
    
    Args:
        data_path (str): Path to raw data directory
        
    Returns:
        dict: Dictionary containing all loaded datasets
    """
    datasets = {}
    
    try:
        # Load core datasets
        datasets['orders'] = pd.read_csv(f'{data_path}orders.csv')
        datasets['products'] = pd.read_csv(f'{data_path}products.csv')
        datasets['order_products_prior'] = pd.read_csv(f'{data_path}order_products__prior.csv')
        datasets['departments'] = pd.read_csv(f'{data_path}departments.csv')
        datasets['aisles'] = pd.read_csv(f'{data_path}aisles.csv')
        
        print("✅ All datasets loaded successfully!")
        
        # Display dataset info
        for name, df in datasets.items():
            print(f"📊 {name}: {df.shape[0]:,} rows, {df.shape[1]} columns")
            
    except FileNotFoundError as e:
        print(f"❌ Error loading data: {e}")
        print("📥 Please download the Instacart dataset from Kaggle")
        
    return datasets


def create_master_dataset(datasets):
    """
    Join all datasets to create comprehensive master dataset
    
    Args:
        datasets (dict): Dictionary of loaded datasets
        
    Returns:
        pd.DataFrame: Master dataset with all joined information
    """
    print("🔗 Creating master dataset...")
    
    # Join order_products with products to get product details
    order_products_full = datasets['order_products_prior'].merge(
        datasets['products'], on='product_id', how='left'
    )
    
    # Add department and aisle information
    order_products_full = order_products_full.merge(
        datasets['departments'], on='department_id', how='left'
    )
    order_products_full = order_products_full.merge(
        datasets['aisles'], on='aisle_id', how='left'
    )
    
    # Join with orders to get order timing and user info
    master_df = order_products_full.merge(
        datasets['orders'], on='order_id', how='left'
    )
    
    print(f"✅ Master dataset created: {master_df.shape[0]:,} rows, {master_df.shape[1]} columns")
    
    return master_df

def clean_data(df):
    """
    Clean and validate the master dataset
    
    Args:
        df (pd.DataFrame): Master dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    print("🧼 Cleaning data...")
    
    # Handle missing values
    df['days_since_prior_order'] = df['days_since_prior_order'].fillna(0)
    
    # Remove any rows with missing essential information
    initial_rows = len(df)
    df = df.dropna(subset=['product_name', 'department', 'aisle'])
    final_rows = len(df)
    
    if initial_rows != final_rows:
        print(f"🗑️ Removed {initial_rows - final_rows:,} rows with missing essential data")
    
    # Data validation
    print("✅ Data validation:")
    print(f"   📦 Unique products: {df['product_id'].nunique():,}")
    print(f"   🛒 Unique orders: {df['order_id'].nunique():,}")
    print(f"   👥 Unique users: {df['user_id'].nunique():,}")
    print(f"   🏪 Departments: {df['department'].nunique()}")
    
    return df

def engineer_features(df):
    """
    Engineer features for analysis
    
    Args:
        df (pd.DataFrame): Master dataset
        
    Returns:
        pd.DataFrame: Dataset with engineered features
    """
    print("🛠️ Engineering features...")
    
    # 1. Create synthetic date column for time series analysis
    df['synthetic_date'] = pd.to_datetime('2017-01-01') + pd.to_timedelta(df['order_number'] // 1000, unit='D')
    
    # 2. Order day of week names
    df['order_dow_name'] = df['order_dow'].map({
        0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 
        4: 'Thursday', 5: 'Friday', 6: 'Saturday'
    })
    
    # 3. Order hour categories
    df['hour_category'] = pd.cut(df['order_hour_of_day'], 
                               bins=[0, 6, 12, 18, 24], 
                               labels=['Night', 'Morning', 'Afternoon', 'Evening'],
                               include_lowest=True)
    
    # 4. Calculate basket size per order
    basket_size = df.groupby('order_id').size().reset_index(name='basket_size')
    df = df.merge(basket_size, on='order_id', how='left')
    
    # 5. Create time periods for trend analysis
    df['time_period'] = pd.cut(df['order_number'], 
                              bins=4, 
                              labels=['Period 1', 'Period 2', 'Period 3', 'Period 4'])
    
    print("✅ Feature engineering completed")
    
    return df

def create_snacks_dataset(df):
    """
    Create focused dataset for snacks category
    
    Args:
        df (pd.DataFrame): Master dataset
        
    Returns:
        pd.DataFrame: Snacks-focused dataset
    """
    print("🍿 Creating snacks-focused dataset...")
    
    # Define snack categories
    snack_categories = ['snacks', 'cookies cakes', 'candy chocolate', 'chips pretzels']
    snacks_df = df[df['department'].str.lower().isin(snack_categories)].copy()
    
    print(f"✅ Snacks dataset: {snacks_df.shape[0]:,} rows ({len(snacks_df['product_id'].unique())} unique products)")
    
    return snacks_df

def calculate_reorder_stats(df):
    """
    Calculate reorder statistics for products
    
    Args:
        df (pd.DataFrame): Master dataset
        
    Returns:
        pd.DataFrame: Reorder statistics by product
    """
    print("🔄 Calculating reorder statistics...")
    
    reorder_stats = df.groupby('product_id').agg({
        'reordered': ['sum', 'count', 'mean'],
        'product_name': 'first',
        'department': 'first'
    }).round(3)
    
    reorder_stats.columns = ['total_reorders', 'total_orders', 'reorder_rate', 'product_name', 'department']
    reorder_stats = reorder_stats.reset_index()
    
    print(f"✅ Reorder stats calculated for {len(reorder_stats)} products")
    
    return reorder_stats

def save_processed_data(master_df, snacks_df, reorder_stats, output_path='../data/processed/'):
    """
    Save all processed datasets
    
    Args:
        master_df (pd.DataFrame): Master dataset
        snacks_df (pd.DataFrame): Snacks dataset
        reorder_stats (pd.DataFrame): Reorder statistics
        output_path (str): Output directory path
    """
    print("💾 Saving processed datasets...")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Save datasets
    master_df.to_csv(f'{output_path}master_dataset.csv', index=False)
    snacks_df.to_csv(f'{output_path}snacks_dataset.csv', index=False)
    reorder_stats.to_csv(f'{output_path}reorder_stats.csv', index=False)
    
    print(f"✅ All processed datasets saved to {output_path}")

def main():
    """
    Main preprocessing pipeline
    """
    print("🚀 Starting Instacart data preprocessing pipeline...")
    
    # Load data
    datasets = load_instacart_data()
    
    if not datasets:
        return
    
    # Create master dataset
    master_df = create_master_dataset(datasets)
    
    # Clean data
    master_df = clean_data(master_df)
    
    # Engineer features
    master_df = engineer_features(master_df)
    
    # Create snacks dataset
    snacks_df = create_snacks_dataset(master_df)
    
    # Calculate reorder stats
    reorder_stats = calculate_reorder_stats(master_df)
    
    # Save processed data
    save_processed_data(master_df, snacks_df, reorder_stats)
    
    print("✅ Preprocessing pipeline completed successfully!")

if __name__ == "__main__":
    main() 