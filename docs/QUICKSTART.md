# Quick Start Guide

## Installation Steps

1. **Navigate to project directory**

    ```bash
    cd "/Users/chenzhixuan/Public/碩一上/物聯網/HW1"
    ```

2. **Create virtual environment (recommended)**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Test the model (optional)**
    ```bash
    python test_model.py
    ```
    This will verify everything works and create a test plot.

## Running the Applications

### Option 1: Streamlit (Recommended - Easier & More Interactive)

```bash
streamlit run streamlit_app.py
```

-   Automatically opens in your browser at `http://localhost:8501`
-   Real-time updates as you adjust sliders
-   Clean, modern interface

### Option 2: Flask (Traditional Web App)

```bash
python flask_app.py
```

-   Open your browser to `http://localhost:5000`
-   Click "Generate & Visualize" button to update
-   More customizable interface

## Features to Try

1. **Adjust Number of Points (20-500)**

    - See how sample size affects model fit

2. **Change Coefficient 'a' (-5.0 to 5.0)**

    - Positive values: upward slope
    - Negative values: downward slope
    - Zero: horizontal line

3. **Modify Noise Variance (0.0 to 10.0)**

    - Low noise: points closer to line, higher R²
    - High noise: scattered points, lower R²

4. **Change Random Seed**
    - Get different random datasets

## Understanding the Output

### Model Coefficients

-   **Coefficient (a)**: Slope of the fitted line
-   **Intercept (b)**: Y-intercept (target is 5.0)
-   **R² Score**: How well the model fits (1.0 = perfect)

### Outliers Table

-   Shows the 5 points with largest prediction errors
-   **Residual**: Absolute difference between actual and predicted Y

## Troubleshooting

**Import errors?**

```bash
pip install --upgrade -r requirements.txt
```

**Port already in use?**

-   For Streamlit: Change port with `streamlit run streamlit_app.py --server.port 8502`
-   For Flask: Edit `flask_app.py` and change `port=5000` to another port

**Permission denied?**

```bash
chmod +x flask_app.py streamlit_app.py
```

## CRISP-DM Methodology Implemented

1. ✅ **Business Understanding**: Interactive regression demonstration
2. ✅ **Data Understanding**: Synthetic data with known properties
3. ✅ **Data Preparation**: User-controlled parameters
4. ✅ **Modeling**: Scikit-learn LinearRegression
5. ✅ **Evaluation**: R², residuals, outlier detection
6. ✅ **Deployment**: Web applications (Streamlit/Flask)

## Next Steps

-   Experiment with different parameter combinations
-   Observe how noise affects model performance
-   Try to achieve R² > 0.95 with low noise
-   Find parameters that create interesting outlier patterns
