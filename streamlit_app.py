"""
Streamlit Interactive Linear Regression Visualizer

This application demonstrates linear regression following the CRISP-DM methodology
with real-time interactive controls.

Usage: streamlit run streamlit_app.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from linear_regression_model import LinearRegressionVisualizer

# Configure page
st.set_page_config(
    page_title="Linear Regression Visualizer",
    page_icon="📈",
    layout="wide"
)

# Title and description
st.title("📈 Interactive Linear Regression Visualizer")
st.markdown("""
This tool demonstrates **Linear Regression** following the **CRISP-DM** methodology.
Adjust the parameters to see how the model adapts to different data characteristics.
""")

# Sidebar for CRISP-DM methodology explanation
with st.sidebar:
    st.header("🔄 CRISP-DM Methodology")
    st.markdown("""
    1. **Business Understanding**
       - Build interactive regression tool
    
    2. **Data Understanding**
       - Synthetic data: y = ax + b + noise
    
    3. **Data Preparation**
       - Adjust parameters below
    
    4. **Modeling**
       - Fit linear regression model
    
    5. **Evaluation**
       - View coefficients & residuals
    
    6. **Deployment**
       - This Streamlit app!
    """)

# Main layout: two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("⚙️ Parameters")

    # User input controls
    n_points = st.slider(
        "Number of Data Points (n)",
        min_value=20,
        max_value=500,
        value=100,
        step=10,
        help="Number of synthetic data points to generate"
    )

    coefficient_a = st.slider(
        "Coefficient a (in y = ax + b + noise)",
        min_value=-5.0,
        max_value=5.0,
        value=2.0,
        step=0.1,
        help="Slope of the linear relationship"
    )

    noise_variance = st.slider(
        "Noise Variance",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="Variance of Gaussian noise added to data"
    )

    random_seed = st.number_input(
        "Random Seed",
        min_value=0,
        max_value=1000,
        value=42,
        step=1,
        help="Seed for reproducible random number generation"
    )

    # Generate button (optional, since we auto-update)
    generate_button = st.button("🔄 Regenerate Data", type="primary")

with col2:
    st.header("📊 Visualization")

    # Create and fit model
    visualizer = LinearRegressionVisualizer(
        n_points=n_points,
        coefficient_a=coefficient_a,
        noise_variance=noise_variance,
        random_seed=random_seed
    )

    # Generate data and fit model
    visualizer.generate_data()
    visualizer.fit_model()

    # Get plot data
    plot_data = visualizer.get_plot_data()

    # Create interactive plot with Plotly
    fig = go.Figure()

    # Add scatter plot for normal points
    normal_mask = [i not in plot_data['outlier_indices']
                   for i in range(len(plot_data['x']))]
    fig.add_trace(go.Scatter(
        x=plot_data['x'][normal_mask],
        y=plot_data['y'][normal_mask],
        mode='markers',
        name='Data Points',
        marker=dict(size=8, color='blue', opacity=0.6),
        hovertemplate='<b>X:</b> %{x:.2f}<br><b>Y:</b> %{y:.2f}<extra></extra>'
    ))

    # Add scatter plot for outliers
    fig.add_trace(go.Scatter(
        x=plot_data['x'][plot_data['outlier_indices']],
        y=plot_data['y'][plot_data['outlier_indices']],
        mode='markers',
        name='Outliers (Top 5)',
        marker=dict(size=12, color='red', symbol='diamond'),
        hovertemplate='<b>Outlier</b><br><b>X:</b> %{x:.2f}<br><b>Y:</b> %{y:.2f}<extra></extra>'
    ))

    # Add regression line
    fig.add_trace(go.Scatter(
        x=plot_data['x_line'],
        y=plot_data['y_line'],
        mode='lines',
        name='Regression Line',
        line=dict(color='green', width=3),
        hovertemplate='<b>Regression Line</b><br><b>X:</b> %{x:.2f}<br><b>Y:</b> %{y:.2f}<extra></extra>'
    ))

    # Update layout
    fig.update_layout(
        title="Linear Regression: Data Points vs Fitted Line",
        xaxis_title="X",
        yaxis_title="Y",
        hovermode='closest',
        height=500,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    st.plotly_chart(fig, use_container_width=True)

# Model evaluation section
st.header("📋 Model Evaluation")

eval_col1, eval_col2 = st.columns(2)

with eval_col1:
    st.subheader("🎯 Model Coefficients")

    coefficients = visualizer.get_model_coefficients()

    # Display metrics
    st.metric(
        label="Coefficient (a)",
        value=f"{coefficients['coefficient_a']:.4f}",
        delta=f"Target: {coefficient_a:.4f}"
    )

    st.metric(
        label="Intercept (b)",
        value=f"{coefficients['intercept_b']:.4f}",
        delta="Target: 5.0000"
    )

    st.metric(
        label="R² Score",
        value=f"{coefficients['r_squared']:.4f}",
        help="Coefficient of determination (1.0 is perfect fit)"
    )

with eval_col2:
    st.subheader("🔴 Top 5 Outliers")

    outliers_df = visualizer.get_outliers(n_outliers=5)

    # Format the dataframe for better display
    outliers_display = outliers_df.copy()
    outliers_display['X'] = outliers_display['X'].round(3)
    outliers_display['Y (Actual)'] = outliers_display['Y (Actual)'].round(3)
    outliers_display['Y (Predicted)'] = outliers_display['Y (Predicted)'].round(
        3)
    outliers_display['Residual'] = outliers_display['Residual'].round(3)

    st.dataframe(
        outliers_display,
        hide_index=True,
        use_container_width=True
    )

# Additional information
st.markdown("---")
st.markdown("""
### 💡 About This Tool

**Data Generation Formula:** `y = ax + b + noise`
- `a`: Coefficient (slope) - controllable via slider
- `b`: Intercept - fixed at 5.0
- `noise`: Gaussian noise with controllable variance

**Outliers:** Points with the largest absolute residuals (prediction errors)

**Model:** Uses scikit-learn's LinearRegression with ordinary least squares
""")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Following CRISP-DM Methodology")
