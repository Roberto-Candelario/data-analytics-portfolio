# Project: Telco Customer Churn Analysis
# Author: Roberto Candelario
# Date: 2024-12-19
# Description: Modular data preprocessing utilities for churn analysis

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')


class TelcoDataPreprocessor:
    """
    Comprehensive data preprocessing pipeline for Telco customer churn analysis.
    
    This class handles data cleaning, feature engineering, and preparation
    for machine learning models.
    """
    
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='median')
        
    def clean_data(self, df):
        """
        Clean the raw Telco dataset by handling missing values and data type issues.
        
        Args:
            df (pd.DataFrame): Raw Telco dataset
            
        Returns:
            pd.DataFrame: Cleaned dataset
        """
        df_clean = df.copy()
        
        # Fix TotalCharges data type issue (common in this dataset)
        if df_clean['TotalCharges'].dtype == 'object':
            df_clean['TotalCharges'] = df_clean['TotalCharges'].replace(' ', np.nan)
            df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'])
            
            # Fill missing values with median
            df_clean['TotalCharges'].fillna(df_clean['TotalCharges'].median(), inplace=True)
        
        # Remove duplicates
        df_clean = df_clean.drop_duplicates()
        
        print(f"✅ Data cleaning complete. Shape: {df_clean.shape}")
        return df_clean
    
    def engineer_features(self, df):
        """
        Create new features to improve model performance and business insights.
        
        Args:
            df (pd.DataFrame): Cleaned dataset
            
        Returns:
            pd.DataFrame: Dataset with engineered features
        """
        df_features = df.copy()
        
        # 1. Senior citizen flag
        df_features['Is_Senior'] = df_features['SeniorCitizen'].apply(
            lambda x: 'Yes' if x == 1 else 'No'
        )
        
        # 2. Tenure groups
        df_features['Tenure_Group'] = pd.cut(
            df_features['tenure'], 
            bins=[0, 12, 24, 48, float('inf')], 
            labels=['New (0-12m)', 'Growing (13-24m)', 'Mature (25-48m)', 'Loyal (48m+)']
        )
        
        # 3. High charges indicator
        charges_75th = df_features['MonthlyCharges'].quantile(0.75)
        df_features['High_Charges'] = df_features['MonthlyCharges'].apply(
            lambda x: 'Yes' if x >= charges_75th else 'No'
        )
        
        # 4. Service count
        service_cols = ['PhoneService', 'MultipleLines', 'InternetService', 
                       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                       'TechSupport', 'StreamingTV', 'StreamingMovies']
        
        def count_services(row):
            count = 0
            for col in service_cols:
                if col in row.index and row[col] == 'Yes':
                    count += 1
            return count
        
        df_features['Service_Count'] = df_features.apply(count_services, axis=1)
        
        # 5. Monthly to total ratio
        df_features['Monthly_to_Total_Ratio'] = (
            df_features['MonthlyCharges'] / (df_features['TotalCharges'] + 1)
        )
        
        # 6. Family status
        df_features['Has_Partner_Dependents'] = (
            (df_features['Partner'] == 'Yes') | (df_features['Dependents'] == 'Yes')
        ).astype(str).replace({'True': 'Yes', 'False': 'No'})
        
        # 7. High-value internet customers
        df_features['Internet_Plus_Streaming'] = (
            (df_features['InternetService'] != 'No') & 
            ((df_features['StreamingTV'] == 'Yes') | (df_features['StreamingMovies'] == 'Yes'))
        ).astype(str).replace({'True': 'Yes', 'False': 'No'})
        
        # 8. Risk score
        def calculate_risk_score(row):
            score = 0
            
            # Contract risk
            if row['Contract'] == 'Month-to-month':
                score += 3
            elif row['Contract'] == 'One year':
                score += 1
            
            # Tenure risk
            if row['tenure'] <= 12:
                score += 2
            
            # Charges risk
            if row['MonthlyCharges'] > charges_75th:
                score += 1
            
            # Internet service risk
            if row['InternetService'] == 'Fiber optic':
                score += 1
            
            # Payment method risk
            if row['PaymentMethod'] == 'Electronic check':
                score += 1
            
            return score
        
        df_features['Risk_Score'] = df_features.apply(calculate_risk_score, axis=1)
        df_features['Risk_Category'] = pd.cut(
            df_features['Risk_Score'], 
            bins=[-1, 2, 4, 8], 
            labels=['Low Risk', 'Medium Risk', 'High Risk']
        )
        
        print(f"✅ Feature engineering complete. New features: 9")
        return df_features
    
    def prepare_for_modeling(self, df, target_column='Churn'):
        """
        Prepare dataset for machine learning by encoding categorical variables
        and scaling numerical features.
        
        Args:
            df (pd.DataFrame): Dataset with engineered features
            target_column (str): Name of target column
            
        Returns:
            tuple: (X_processed, y_processed, feature_names)
        """
        df_model = df.copy()
        
        # Separate features and target
        features_to_exclude = ['customerID', target_column, 'Risk_Score']
        feature_columns = [col for col in df_model.columns if col not in features_to_exclude]
        
        X = df_model[feature_columns].copy()
        y = df_model[target_column].copy()
        
        # Encode categorical variables
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
        numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        # Label encode categorical features
        for col in categorical_features:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
            X[col] = self.label_encoders[col].fit_transform(X[col].astype(str))
        
        # Encode target variable
        if target_column not in self.label_encoders:
            self.label_encoders[target_column] = LabelEncoder()
        y_encoded = self.label_encoders[target_column].fit_transform(y)
        
        # Scale numerical features
        X_scaled = X.copy()
        if numerical_features:
            X_scaled[numerical_features] = self.scaler.fit_transform(X[numerical_features])
        
        print(f"✅ Model preparation complete.")
        print(f"   Features: {len(feature_columns)}")
        print(f"   Categorical: {len(categorical_features)}")
        print(f"   Numerical: {len(numerical_features)}")
        
        return X_scaled, y_encoded, feature_columns
    
    def get_feature_summary(self, df):
        """
        Generate a summary of features for analysis reporting.
        
        Args:
            df (pd.DataFrame): Dataset to summarize
            
        Returns:
            pd.DataFrame: Feature summary statistics
        """
        summary_data = []
        
        for column in df.columns:
            if column != 'customerID':
                dtype = str(df[column].dtype)
                missing_count = df[column].isnull().sum()
                missing_percent = (missing_count / len(df)) * 100
                unique_count = df[column].nunique()
                
                if df[column].dtype in ['int64', 'float64']:
                    stats = {
                        'Feature': column,
                        'Type': 'Numerical',
                        'Missing_Count': missing_count,
                        'Missing_Percent': missing_percent,
                        'Unique_Values': unique_count,
                        'Mean': df[column].mean(),
                        'Std': df[column].std(),
                        'Min': df[column].min(),
                        'Max': df[column].max()
                    }
                else:
                    stats = {
                        'Feature': column,
                        'Type': 'Categorical',
                        'Missing_Count': missing_count,
                        'Missing_Percent': missing_percent,
                        'Unique_Values': unique_count,
                        'Most_Common': df[column].mode().iloc[0] if not df[column].empty else None,
                        'Mean': None,
                        'Std': None,
                        'Min': None,
                        'Max': None
                    }
                
                summary_data.append(stats)
        
        return pd.DataFrame(summary_data)


def load_and_preprocess_data(file_path):
    """
    Convenience function to load and preprocess Telco data in one step.
    
    Args:
        file_path (str): Path to the raw CSV file
        
    Returns:
        tuple: (cleaned_data, featured_data, model_ready_data)
    """
    # Initialize preprocessor
    preprocessor = TelcoDataPreprocessor()
    
    # Load data
    print(f"📊 Loading data from: {file_path}")
    df_raw = pd.read_csv(file_path)
    print(f"✅ Data loaded. Shape: {df_raw.shape}")
    
    # Clean data
    df_clean = preprocessor.clean_data(df_raw)
    
    # Engineer features
    df_features = preprocessor.engineer_features(df_clean)
    
    # Prepare for modeling
    X, y, feature_names = preprocessor.prepare_for_modeling(df_features)
    
    model_data = {
        'X': X,
        'y': y,
        'feature_names': feature_names,
        'preprocessor': preprocessor
    }
    
    return df_clean, df_features, model_data


if __name__ == "__main__":
    """
    Example usage of the preprocessing pipeline
    """
    # Example usage
    try:
        data_path = "../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
        cleaned, featured, model_ready = load_and_preprocess_data(data_path)
        
        print("\n📋 PREPROCESSING SUMMARY:")
        print("="*40)
        print(f"Original data shape: {cleaned.shape}")
        print(f"Featured data shape: {featured.shape}")
        print(f"Model features: {len(model_ready['feature_names'])}")
        print(f"Target distribution: {pd.Series(model_ready['y']).value_counts().to_dict()}")
        
    except FileNotFoundError:
        print("⚠️ Data file not found. Please ensure the dataset is available.")
        print("💡 This script is designed to work with the Telco Customer Churn dataset.") 