#!/usr/bin/env python3
"""
Fixed Data Exploration Code
Author: Roberto Candelario
Date: 2024-12-19
Description: Corrected version of data exploration with proper print syntax
"""

import pandas as pd
import numpy as np

# Example with simulated data for demonstration
def create_sample_data():
    """Create sample datasets for demonstration"""
    np.random.seed(42)
    
    orders = pd.DataFrame({
        'order_id': range(1, 101),
        'user_id': np.random.randint(1, 21, 100),
        'order_dow': np.random.randint(0, 7, 100),
        'order_hour_of_day': np.random.randint(6, 23, 100)
    })
    
    products = pd.DataFrame({
        'product_id': range(1, 21),
        'product_name': [f'Product {i}' for i in range(1, 21)],
        'department_id': np.random.randint(1, 6, 20)
    })
    
    order_products_prior = pd.DataFrame({
        'order_id': np.random.randint(1, 101, 200),
        'product_id': np.random.randint(1, 21, 200),
        'reordered': np.random.choice([0, 1], 200)
    })
    
    departments = pd.DataFrame({
        'department_id': range(1, 6),
        'department': ['produce', 'snacks', 'dairy', 'beverages', 'frozen']
    })
    
    aisles = pd.DataFrame({
        'aisle_id': range(1, 11),
        'aisle': [f'aisle_{i}' for i in range(1, 11)]
    })
    
    return orders, products, order_products_prior, departments, aisles

def data_exploration_corrected():
    """
    CORRECTED VERSION: Data Exploration & Quality Assessment
    Fixed all print statement syntax errors
    """
    
    # Create sample data
    orders, products, order_products_prior, departments, aisles = create_sample_data()
    
    # === CORRECTED CODE STARTS HERE ===
    print("🔍 Exploring dataset structure and quality...")
    
    # Check for missing values
    print("\n❓ Missing Values Check:")
    datasets = {
        'orders': orders, 
        'products': products, 
        'order_products_prior': order_products_prior, 
        'departments': departments, 
        'aisles': aisles
    }
    
    for name, df in datasets.items():
        missing = df.isnull().sum().sum()
        print(f"{name}: {missing} missing values")
    
    # Display sample data from each dataset
    print("\n📋 Sample Data Preview:")
    
    print("\n🛒 Orders Sample:")
    print(orders.head(3))
    
    print("\n🛍️ Products Sample:")
    print(products.head(3))
    
    print("\n📦 Order Products Sample:")
    print(order_products_prior.head(3))
    
    print("\n🏪 Departments:")
    print(departments.head())
    
    print("\n🚶 Aisles (sample):")
    print(aisles.head())
    # === CORRECTED CODE ENDS HERE ===
    
    print("\n✅ Data exploration completed successfully!")
    print("🎯 All print statements now use proper syntax")

def show_the_fix():
    """Show the specific fixes made"""
    print("🔧 SYNTAX FIXES APPLIED:")
    print("=" * 50)
    
    print("\n❌ BEFORE (broken syntax):")
    print('print("')
    print('📋 Sample Data Preview:")')
    print("# ↑ This causes 'unterminated string literal' error")
    
    print("\n✅ AFTER (correct syntax):")
    print('print("\\n📋 Sample Data Preview:")')
    print("# ↑ Proper newline escape character")
    
    print("\n🎯 KEY CHANGES:")
    print("1. Replace broken newlines with \\n escape characters")
    print("2. Ensure all string literals are properly terminated")
    print("3. Use consistent formatting for better readability")
    
    print("\n📝 PATTERN:")
    print("Old: print(\"")
    print("     Text here\")")
    print("New: print(\"\\nText here\")")

if __name__ == "__main__":
    print("🛒 INSTACART DATA EXPLORATION - SYNTAX FIXED VERSION")
    print("=" * 60)
    
    # Show the fixes
    show_the_fix()
    
    print("\n" + "=" * 60)
    print("📊 RUNNING CORRECTED CODE:")
    
    # Run the corrected exploration
    data_exploration_corrected() 