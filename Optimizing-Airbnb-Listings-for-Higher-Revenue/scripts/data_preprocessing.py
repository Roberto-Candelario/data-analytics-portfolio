# Project: Optimizing Airbnb Listings for Higher Revenue
# Author: Roberto Candelario
# Date: 2024-12-19
# Description: Modular data preprocessing functions for Airbnb analysis

import pandas as pd
import numpy as np
import os
from typing import Tuple, Optional

def download_kaggle_dataset(dataset_name: str, output_path: str) -> bool:
    """
    Download Airbnb dataset from Kaggle
    
    Args:
        dataset_name: Kaggle dataset identifier
        output_path: Local path to save dataset
        
    Returns:
        bool: Success status
    """
    try:
        import zipfile
        
        # Create directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download dataset
        os.system(f'kaggle datasets download -d {dataset_name} -p {output_path}')
        
        # Extract zip file
        zip_path = os.path.join(output_path, f'{dataset_name.split("/")[-1]}.zip')
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        
        return False
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        return False

def clean_airbnb_data(df: pd.DataFrame, 
                     price_min: float = 10, 
                     price_max: float = 1000) -> pd.DataFrame:
    """
    Clean and prepare Airbnb data for analysis
    
    Args:
        df: Raw Airbnb dataframe
        price_min: Minimum realistic price
        price_max: Maximum realistic price
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    df_clean = df.copy()
    
    # Remove price outliers
    df_clean = df_clean[
        (df_clean['price'] >= price_min) & 
        (df_clean['price'] <= price_max)
    ]
    
    # Remove rows with missing critical information
    critical_columns = ['neighbourhood_group', 'room_type', 'price']
    df_clean = df_clean.dropna(subset=critical_columns)
    
    # Fill missing values with business logic
    df_clean['number_of_reviews'] = df_clean['number_of_reviews'].fillna(0)
    df_clean['reviews_per_month'] = df_clean['reviews_per_month'].fillna(0)
    df_clean['calculated_host_listings_count'] = df_clean['calculated_host_listings_count'].fillna(1)
    
    return df_clean

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features for revenue analysis
    
    Args:
        df: Cleaned Airbnb dataframe
        
    Returns:
        pd.DataFrame: Feature-engineered dataframe
    """
    df_features = df.copy()
    
    # Revenue potential metric
    df_features['revenue_potential'] = (
        df_features['price'] * 
        (365 - df_features['availability_365']) / 365
    )
    
    # Host type categorization
    df_features['host_type'] = df_features['calculated_host_listings_count'].apply(
        lambda x: 'Single Listing' if x == 1 
        else 'Multiple Listings' if x <= 5 
        else 'Super Host'
    )
    
    # Review activity categories
    df_features['review_activity'] = pd.cut(
        df_features['number_of_reviews'],
        bins=[0, 0, 10, 50, float('inf')],
        labels=['No Reviews', 'Few Reviews', 'Many Reviews', 'Highly Reviewed']
    )
    
    # Availability categories
    df_features['availability_category'] = pd.cut(
        df_features['availability_365'],
        bins=[0, 90, 180, 365],
        labels=['Low Available', 'Medium Available', 'High Available']
    )
    
    # Price categories
    df_features['price_category'] = pd.cut(
        df_features['price'],
        bins=[0, 75, 150, 300, float('inf')],
        labels=['Budget', 'Mid-Range', 'Premium', 'Luxury']
    )
    
    return df_features

def create_sample_data(n_samples: int = 1000, random_state: int = 42) -> pd.DataFrame:
    """
    Create sample Airbnb data for testing
    
    Args:
        n_samples: Number of sample listings
        random_state: Random seed for reproducibility
        
    Returns:
        pd.DataFrame: Sample dataframe
    """
    np.random.seed(random_state)
    
    sample_data = pd.DataFrame({
        'id': range(1, n_samples + 1),
        'name': [f'Listing {i}' for i in range(1, n_samples + 1)],
        'host_id': np.random.randint(1, 500, n_samples),
        'host_name': [f'Host {i}' for i in np.random.randint(1, 500, n_samples)],
        'neighbourhood_group': np.random.choice(
            ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'], 
            n_samples, 
            p=[0.3, 0.25, 0.2, 0.15, 0.1]
        ),
        'neighbourhood': np.random.choice(
            ['East Village', 'Williamsburg', 'Harlem', 'LES', 'Chelsea'], 
            n_samples
        ),
        'latitude': np.random.uniform(40.5, 40.9, n_samples),
        'longitude': np.random.uniform(-74.3, -73.7, n_samples),
        'room_type': np.random.choice(
            ['Entire home/apt', 'Private room', 'Shared room'], 
            n_samples, 
            p=[0.5, 0.4, 0.1]
        ),
        'price': np.random.lognormal(4.5, 0.8, n_samples).astype(int),
        'minimum_nights': np.random.choice(
            [1, 2, 3, 7, 30], 
            n_samples, 
            p=[0.3, 0.2, 0.2, 0.2, 0.1]
        ),
        'number_of_reviews': np.random.poisson(20, n_samples),
        'last_review': pd.date_range('2019-01-01', '2019-12-31', periods=n_samples),
        'reviews_per_month': np.random.uniform(0.1, 5, n_samples),
        'calculated_host_listings_count': np.random.poisson(3, n_samples),
        'availability_365': np.random.randint(0, 366, n_samples)
    })
    
    return sample_data

def load_and_prepare_data(file_path: Optional[str] = None) -> pd.DataFrame:
    """
    Main function to load and prepare Airbnb data
    
    Args:
        file_path: Path to Airbnb CSV file
        
    Returns:
        pd.DataFrame: Prepared dataframe
    """
    if file_path and os.path.exists(file_path):
        print(f"Loading data from: {file_path}")
        df = pd.read_csv(file_path)
    else:
        print("Creating sample data for demonstration...")
        df = create_sample_data()
    
    # Clean and engineer features
    df_clean = clean_airbnb_data(df)
    df_final = engineer_features(df_clean)
    
    print(f"Data preparation complete! Final shape: {df_final.shape}")
    return df_final

if __name__ == "__main__":
    # Example usage
    data = load_and_prepare_data()
    print("\nSample of prepared data:")
    print(data.head())
    
    # Save processed data
    output_path = "../data/processed/airbnb_processed.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"\nProcessed data saved to: {output_path}") 