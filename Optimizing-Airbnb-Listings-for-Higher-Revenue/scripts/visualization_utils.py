# Project: Optimizing Airbnb Listings for Higher Revenue
# Author: Roberto Candelario
# Date: 2024-12-19
# Description: Visualization utilities for Airbnb revenue analysis

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple

# Set default style
plt.style.use('default')
sns.set_palette("husl")

def create_revenue_dashboard(df: pd.DataFrame) -> plt.Figure:
    """
    Create comprehensive revenue visualization dashboard
    
    Args:
        df: Processed Airbnb dataframe
        
    Returns:
        plt.Figure: Dashboard figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('🏠 Airbnb Revenue Optimization Dashboard - NYC Market Analysis', 
                 fontsize=16, fontweight='bold')
    
    # 1. Neighborhood Revenue Comparison
    ax1 = axes[0, 0]
    neighborhood_revenue = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=True)
    bars1 = ax1.barh(neighborhood_revenue.index, neighborhood_revenue.values, color='skyblue')
    ax1.set_title('💰 Average Price by Neighborhood', fontweight='bold')
    ax1.set_xlabel('Average Price ($)')
    
    # Add value labels
    for i, v in enumerate(neighborhood_revenue.values):
        ax1.text(v + 5, i, f'${v:.0f}', va='center', fontweight='bold')
    
    # 2. Room Type Revenue Distribution
    ax2 = axes[0, 1]
    room_revenue = df.groupby('room_type')['price'].mean().sort_values(ascending=False)
    bars2 = ax2.bar(room_revenue.index, room_revenue.values, 
                   color=['coral', 'lightgreen', 'gold'])
    ax2.set_title('🏠 Revenue by Property Type', fontweight='bold')
    ax2.set_ylabel('Average Price ($)')
    ax2.set_xticklabels(room_revenue.index, rotation=45, ha='right')
    
    # Add value labels
    for i, v in enumerate(room_revenue.values):
        ax2.text(i, v + 5, f'${v:.0f}', ha='center', fontweight='bold')
    
    # 3. Price Distribution Analysis
    ax3 = axes[1, 0]
    ax3.hist(df['price'], bins=50, alpha=0.7, color='mediumpurple', edgecolor='black')
    ax3.axvline(df['price'].mean(), color='red', linestyle='--', linewidth=2, 
               label=f'Mean: ${df["price"].mean():.0f}')
    ax3.axvline(df['price'].median(), color='orange', linestyle='--', linewidth=2, 
               label=f'Median: ${df["price"].median():.0f}')
    ax3.set_title('📊 Price Distribution Analysis', fontweight='bold')
    ax3.set_xlabel('Price per Night ($)')
    ax3.set_ylabel('Number of Listings')
    ax3.legend()
    
    # 4. Reviews vs Revenue Relationship
    ax4 = axes[1, 1]
    review_bins = pd.cut(df['number_of_reviews'], 
                        bins=[0, 0, 10, 50, 200], 
                        labels=['No Reviews', '1-10', '11-50', '50+'])
    review_price = df.groupby(review_bins)['price'].mean()
    bars4 = ax4.bar(review_price.index, review_price.values, color='lightcoral')
    ax4.set_title('⭐ Reviews Impact on Revenue', fontweight='bold')
    ax4.set_ylabel('Average Price ($)')
    ax4.set_xlabel('Review Count Category')
    
    # Add value labels
    for i, v in enumerate(review_price.values):
        ax4.text(i, v + 5, f'${v:.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_interactive_heatmap(df: pd.DataFrame) -> go.Figure:
    """
    Create interactive revenue heatmap
    
    Args:
        df: Processed Airbnb dataframe
        
    Returns:
        go.Figure: Plotly heatmap figure
    """
    # Create pivot table
    pivot_data = df.pivot_table(
        values='price',
        index='neighbourhood_group',
        columns='room_type',
        aggfunc='mean'
    ).round(0)
    
    # Create heatmap
    fig = px.imshow(
        pivot_data,
        labels=dict(x="Room Type", y="Neighborhood", color="Avg Price ($)"),
        title="💰 NYC Airbnb Revenue Heatmap: Neighborhood vs Room Type",
        color_continuous_scale="RdYlBu_r",
        text_auto=True
    )
    
    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        width=800,
        height=500
    )
    
    return fig

def create_scatter_analysis(df: pd.DataFrame) -> go.Figure:
    """
    Create interactive scatter plot for revenue analysis
    
    Args:
        df: Processed Airbnb dataframe
        
    Returns:
        go.Figure: Plotly scatter figure
    """
    fig = px.scatter(
        df,
        x='number_of_reviews',
        y='price',
        color='neighbourhood_group',
        size='availability_365',
        hover_data=['room_type', 'revenue_potential'],
        title="🎯 Revenue Optimization Analysis: Reviews vs Price",
        labels={'number_of_reviews': 'Number of Reviews', 'price': 'Price per Night ($)'},
        width=900,
        height=600
    )
    
    fig.update_layout(title_x=0.5)
    return fig

def plot_feature_importance(feature_importance: pd.DataFrame) -> plt.Figure:
    """
    Create feature importance visualization
    
    Args:
        feature_importance: DataFrame with feature names and importance scores
        
    Returns:
        plt.Figure: Feature importance plot
    """
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['Feature'], feature_importance['Importance'])
    plt.title('🎯 Revenue Prediction: Feature Importance', fontsize=14, fontweight='bold')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    return plt.gcf()

def create_model_validation_plots(y_test: np.ndarray, y_pred: np.ndarray, 
                                 r2: float, mae: float) -> plt.Figure:
    """
    Create model validation visualizations
    
    Args:
        y_test: Actual test values
        y_pred: Predicted values
        r2: R-squared score
        mae: Mean absolute error
        
    Returns:
        plt.Figure: Validation plots
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Actual vs Predicted
    ax1.scatter(y_test, y_pred, alpha=0.5)
    ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    ax1.set_xlabel('Actual Price ($)')
    ax1.set_ylabel('Predicted Price ($)')
    ax1.set_title(f'Model Accuracy (R² = {r2:.3f})')
    
    # Residuals
    residuals = y_test - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.5)
    ax2.axhline(y=0, color='r', linestyle='--')
    ax2.set_xlabel('Predicted Price ($)')
    ax2.set_ylabel('Residuals ($)')
    ax2.set_title(f'Residual Analysis (MAE = ${mae:.0f})')
    
    plt.tight_layout()
    return fig

def create_business_insight_charts(df: pd.DataFrame) -> Dict[str, plt.Figure]:
    """
    Create specific charts for business insights
    
    Args:
        df: Processed Airbnb dataframe
        
    Returns:
        Dict[str, plt.Figure]: Dictionary of insight charts
    """
    charts = {}
    
    # 1. Revenue by Host Type
    fig1, ax = plt.subplots(figsize=(10, 6))
    host_revenue = df.groupby('host_type')['price'].mean().sort_values(ascending=False)
    bars = ax.bar(host_revenue.index, host_revenue.values, color='lightblue')
    ax.set_title('👥 Revenue by Host Type', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Price ($)')
    ax.set_xlabel('Host Type')
    
    # Add value labels
    for i, v in enumerate(host_revenue.values):
        ax.text(i, v + 5, f'${v:.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    charts['host_type_revenue'] = fig1
    
    # 2. Availability vs Price Relationship
    fig2, ax = plt.subplots(figsize=(10, 6))
    availability_price = df.groupby('availability_category')['price'].mean()
    bars = ax.bar(availability_price.index, availability_price.values, color='lightgreen')
    ax.set_title('📅 Availability Strategy vs Revenue', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Price ($)')
    ax.set_xlabel('Availability Category')
    
    # Add value labels
    for i, v in enumerate(availability_price.values):
        ax.text(i, v + 5, f'${v:.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    charts['availability_revenue'] = fig2
    
    # 3. Price Category Distribution
    fig3, ax = plt.subplots(figsize=(10, 6))
    price_dist = df['price_category'].value_counts()
    colors = ['gold', 'lightcoral', 'lightblue', 'plum']
    wedges, texts, autotexts = ax.pie(price_dist.values, labels=price_dist.index, 
                                     autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title('💰 Market Distribution by Price Category', fontsize=14, fontweight='bold')
    
    charts['price_distribution'] = fig3
    
    return charts

def save_all_visualizations(df: pd.DataFrame, output_dir: str = "../dashboard/") -> None:
    """
    Generate and save all visualizations
    
    Args:
        df: Processed Airbnb dataframe
        output_dir: Directory to save visualizations
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Create and save main dashboard
    dashboard = create_revenue_dashboard(df)
    dashboard.savefig(f"{output_dir}/revenue_dashboard.png", dpi=300, bbox_inches='tight')
    print(f"✅ Dashboard saved to: {output_dir}/revenue_dashboard.png")
    
    # Create and save business insight charts
    insight_charts = create_business_insight_charts(df)
    for name, chart in insight_charts.items():
        chart.savefig(f"{output_dir}/{name}.png", dpi=300, bbox_inches='tight')
        print(f"✅ {name} chart saved to: {output_dir}/{name}.png")
    
    plt.close('all')  # Close all figures to free memory

if __name__ == "__main__":
    # Example usage with sample data
    from data_preprocessing import create_sample_data, engineer_features
    
    # Create sample data
    sample_df = create_sample_data()
    processed_df = engineer_features(sample_df)
    
    # Generate visualizations
    save_all_visualizations(processed_df)
    print("All visualizations saved successfully!") 