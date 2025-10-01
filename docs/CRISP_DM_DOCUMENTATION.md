# CRISP-DM Methodology Implementation

## Detailed Documentation

### 1. Business Understanding 🎯

**Objective**: Create an interactive web-based tool that demonstrates linear regression concepts in an educational and intuitive way.

**Key Requirements**:

-   User-friendly interface for parameter adjustment
-   Real-time visualization of regression results
-   Clear presentation of model performance metrics
-   Identification of outliers for quality assessment

**Success Criteria**:

-   Application is accessible via web browser
-   Users can modify parameters and see immediate results
-   Model coefficients and predictions are displayed clearly
-   Educational value through interactive exploration

---

### 2. Data Understanding 📊

**Data Generation Process**:

-   **Formula**: `y = ax + b + ε` where:
    -   `a`: Coefficient (slope) - user controllable
    -   `b`: Intercept = 5.0 (fixed)
    -   `ε`: Gaussian noise ~ N(0, σ²)
    -   `x`: Uniformly distributed in [0, 10]

**Data Characteristics**:

-   Synthetic data ensures reproducibility
-   Linear relationship with controlled noise
-   Random seed for consistent results
-   Sample size: 20-500 points (user adjustable)

**Statistical Properties**:

```python
# Expected relationship
E[Y|X] = ax + 5.0
Var(Y|X) = σ² (noise_variance)
```

---

### 3. Data Preparation 🔧

**Parameter Controls**:

1. **Number of Points (n)**: 20-500

    - Smaller n → Higher variance in estimates
    - Larger n → More stable model coefficients

2. **Coefficient a**: -5.0 to 5.0

    - Positive → Upward trend
    - Negative → Downward trend
    - Zero → Horizontal line

3. **Noise Variance**: 0.0 to 10.0

    - Low variance → Tight fit, high R²
    - High variance → Scattered points, low R²

4. **Random Seed**: 0-1000
    - Controls randomness for reproducibility

**Data Quality Checks**:

-   Validation of parameter ranges
-   Handling of edge cases (e.g., zero variance)
-   Automatic reshaping for sklearn compatibility

---

### 4. Modeling 🤖

**Algorithm**: Ordinary Least Squares (OLS) Linear Regression

**Implementation**:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
```

**Model Assumptions**:

1. Linearity between X and Y
2. Independence of errors
3. Homoscedasticity (constant variance)
4. Normally distributed errors

**Why OLS?**:

-   Closed-form solution (fast computation)
-   Interpretable coefficients
-   Well-established theory
-   Appropriate for demonstration purposes

**Model Training**:

-   No hyperparameters to tune
-   Direct calculation via matrix operations
-   Guaranteed convergence
-   Computationally efficient

---

### 5. Evaluation 📈

**Metrics Implemented**:

1. **Coefficient (a)**

    - Estimated slope of the relationship
    - Should approximate target coefficient
    - Sign indicates direction of relationship

2. **Intercept (b)**

    - Y-intercept of fitted line
    - Target value: 5.0
    - Deviation indicates bias

3. **R² Score (Coefficient of Determination)**

    - Range: [0, 1] (higher is better)
    - Interpretation:
        - R² > 0.9: Excellent fit
        - 0.7 < R² < 0.9: Good fit
        - 0.5 < R² < 0.7: Moderate fit
        - R² < 0.5: Poor fit
    - Formula: `R² = 1 - (SS_res / SS_tot)`

4. **Residual Analysis**
    - Residual = |Actual Y - Predicted Y|
    - Identifies prediction errors
    - Highlights outliers

**Outlier Detection**:

-   Top 5 points with largest residuals
-   Displayed in table with:
    -   Point index
    -   X and Y coordinates
    -   Predicted Y value
    -   Absolute residual

**Visual Evaluation**:

-   Scatter plot of data points
-   Regression line overlay
-   Color-coded outliers (red diamonds)
-   Interactive hover information

---

### 6. Deployment 🚀

**Two Deployment Options**:

#### **Option A: Streamlit (Recommended)**

**Advantages**:

-   Simpler setup (no HTML/CSS needed)
-   Real-time updates as sliders move
-   Built-in caching for performance
-   Mobile-friendly responsive design

**Features**:

-   Interactive sliders with live feedback
-   Plotly charts with zoom/pan capabilities
-   Automatic layout management
-   Session state management

**Launch Command**:

```bash
streamlit run streamlit_app.py
```

**Technical Stack**:

-   Backend: Python + Streamlit
-   Visualization: Plotly
-   Port: 8501 (default)

---

#### **Option B: Flask**

**Advantages**:

-   Full control over frontend
-   Traditional web architecture
-   Better for integration with existing systems
-   Customizable styling

**Features**:

-   RESTful API endpoint (/generate)
-   Custom HTML/CSS design
-   JavaScript for interactivity
-   Explicit "Generate" button

**Launch Command**:

```bash
python3 flask_app.py
```

**Technical Stack**:

-   Backend: Python + Flask
-   Frontend: HTML5, CSS3, JavaScript
-   Visualization: Plotly.js
-   Port: 5000 (default)

**API Endpoint**:

```
POST /generate
Content-Type: application/json

{
  "n_points": 100,
  "coefficient_a": 2.0,
  "noise_variance": 1.0,
  "random_seed": 42
}

Response:
{
  "plot_data": {...},
  "coefficients": {...},
  "outliers": [...]
}
```

---

## Code Structure

```
HW1/
├── linear_regression_model.py    # Core logic (CRISP-DM steps 2-5)
│   ├── LinearRegressionVisualizer class
│   ├── generate_data()           # Data Understanding
│   ├── fit_model()                # Modeling
│   ├── calculate_residuals()      # Evaluation
│   └── get_outliers()             # Evaluation
│
├── streamlit_app.py               # Deployment (Streamlit)
│   ├── UI components
│   ├── Real-time visualization
│   └── Interactive controls
│
├── flask_app.py                   # Deployment (Flask backend)
│   └── REST API endpoints
│
├── templates/
│   └── index.html                 # Flask frontend
│
├── test_model.py                  # Verification script
├── requirements.txt               # Dependencies
├── README.md                      # Overview
├── QUICKSTART.md                  # Quick setup guide
└── CRISP_DM_DOCUMENTATION.md     # This file
```

---

## Testing Strategy

### Unit Testing (test_model.py)

-   Verifies data generation
-   Confirms model training
-   Validates coefficient calculation
-   Checks outlier detection
-   Creates test visualization

### Integration Testing

1. Launch application
2. Test parameter ranges
3. Verify visual updates
4. Check edge cases (e.g., zero noise)
5. Validate calculations

### User Acceptance Testing

1. Non-technical users can adjust parameters
2. Results update appropriately
3. Visualizations are clear
4. Metrics are understandable

---

## Performance Considerations

**Optimization Techniques**:

1. **Numpy vectorization** for fast computation
2. **Efficient data structures** (numpy arrays)
3. **Streamlit caching** (@st.cache_data for large computations)
4. **Client-side rendering** (Plotly) for interactive charts

**Scalability**:

-   Handles up to 500 points efficiently
-   Sub-second response time for typical use
-   Minimal memory footprint
-   No database required (stateless)

---

## Educational Value

**Learning Objectives**:

1. Understand linear regression fundamentals
2. Explore impact of sample size on model stability
3. Observe effect of noise on prediction accuracy
4. Recognize outliers and their influence
5. Interpret R² and other metrics

**Exploration Activities**:

-   Set noise to 0 → observe perfect fit (R² ≈ 1.0)
-   Increase noise → watch R² decrease
-   Change coefficient → see slope adjustment
-   Vary sample size → notice confidence changes
-   Different seeds → explore random variation

---

## Future Enhancements

**Potential Additions**:

1. Multiple regression (multiple X variables)
2. Polynomial regression option
3. Cross-validation implementation
4. Residual plots (Q-Q plot, residuals vs fitted)
5. Confidence intervals for predictions
6. Export data/results to CSV
7. Compare multiple models side-by-side
8. Advanced outlier detection methods
9. Model diagnostics (VIF, condition number)
10. User data upload capability

---

## References

**CRISP-DM**:

-   Chapman et al. (2000). CRISP-DM 1.0 Step-by-step data mining guide

**Linear Regression**:

-   James, G. et al. (2013). An Introduction to Statistical Learning
-   Hastie, T. et al. (2009). The Elements of Statistical Learning

**Libraries**:

-   scikit-learn: https://scikit-learn.org/
-   Streamlit: https://streamlit.io/
-   Flask: https://flask.palletsprojects.com/
-   Plotly: https://plotly.com/

---

## License & Credits

**Author**: Created for IoT Course Assignment
**Date**: October 2025
**License**: Educational use

**Technologies**:

-   Python 3.11
-   scikit-learn 1.3.0
-   Streamlit 1.25.0
-   Flask 2.3.2
-   Plotly 5.15.0
