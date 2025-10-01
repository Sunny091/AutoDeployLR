# 📈 Linear Regression Interactive Visualizer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

An interactive web application for demonstrating **Linear Regression** following the **CRISP-DM** methodology. Built with Python, scikit-learn, and provides both Streamlit and Flask implementations.

<div align="center">
  <img src="screenshots/test_regression_plot.png" alt="Linear Regression Visualization" width="600"/>
</div>

## ✨ Features

-   🎯 **Real-time Auto-Update** - No button clicks needed!
-   📊 **Interactive Visualizations** - Powered by Plotly
-   🎛️ **Adjustable Parameters**:
    -   Number of data points (20-500)
    -   Coefficient `a` in `y = ax + b + noise`
    -   Noise variance (0-10)
    -   Random seed for reproducibility
-   🔴 **Outlier Detection** - Automatically highlights top 5 outliers
-   📈 **Model Metrics** - Display R², coefficients, and residuals
-   ⚡ **Smart Debounce** - 500ms delay for smooth performance
-   🌐 **Dual Deployment** - Choose Streamlit or Flask

## 🔄 CRISP-DM Methodology

This project follows the complete CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology:

1. **Business Understanding** - Interactive tool for demonstrating linear regression
2. **Data Understanding** - Synthetic data with formula `y = ax + b + noise`
3. **Data Preparation** - User-controlled parameters for data generation
4. **Modeling** - Ordinary Least Squares (OLS) linear regression
5. **Evaluation** - R² score, residuals, and outlier analysis
6. **Deployment** - Web applications with Streamlit and Flask

## 🚀 Quick Start

### Prerequisites

-   Python 3.11+
-   pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/linear-regression-visualizer.git
cd linear-regression-visualizer

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Streamlit (Recommended)

```bash
streamlit run streamlit_app.py
```

-   Opens at `http://localhost:8501`
-   Real-time updates
-   Modern interface

#### Option 2: Flask

```bash
python3 flask_app.py
```

-   Opens at `http://localhost:3000`
-   Auto-update enabled
-   Custom styled interface

### Testing

```bash
# Run unit tests
python3 test_model.py
```

## 📊 How It Works

### Data Generation

The application generates synthetic data using the formula:

```
y = ax + b + ε

where:
  a = coefficient (user-controlled, range: -5.0 to 5.0)
  b = intercept (fixed at 5.0)
  ε = Gaussian noise ~ N(0, σ²)
  x = uniform random in [0, 10]
```

### Model Training

Uses scikit-learn's `LinearRegression` with Ordinary Least Squares (OLS):

-   Fast computation with closed-form solution
-   No hyperparameters to tune
-   Interpretable coefficients

### Evaluation Metrics

-   **Coefficient (a)** - Estimated slope
-   **Intercept (b)** - Y-intercept (target: 5.0)
-   **R² Score** - Goodness of fit (0 to 1)
-   **Residuals** - Absolute prediction errors
-   **Top 5 Outliers** - Points with largest residuals

## 📁 Project Structure

```
linear-regression-visualizer/
│
├── 📄 Core Application
│   ├── linear_regression_model.py    # Core regression logic
│   ├── streamlit_app.py               # Streamlit web app
│   ├── flask_app.py                   # Flask backend
│   └── templates/
│       └── index.html                 # Flask frontend
│
├── 🧪 Testing
│   └── test_model.py                  # Unit tests
│
├── 📚 Documentation
│   ├── README.md                      # This file
│   └── docs/
│       ├── CRISP_DM_DOCUMENTATION.md  # Methodology details
│       ├── QUICKSTART.md              # Quick setup guide
│       ├── AUTO_UPDATE_FEATURE.md     # Auto-update feature docs
│       ├── PROJECT_STRUCTURE.md       # Code architecture
│       ├── PROJECT_SUMMARY.txt        # Project summary
│       ├── QUICK_REFERENCE.txt        # Quick reference card
│       └── UPDATE_SUMMARY.txt         # Update history
│
├── 📦 Configuration
│   ├── requirements.txt               # Python dependencies
│   └── .gitignore                     # Git ignore rules
│
└── 🖼️ Assets
    └── screenshots/
        └── test_regression_plot.png   # Sample visualization
```

## 🎮 Usage Examples

### Example 1: Perfect Fit

```
Set: noise_variance = 0
Result: R² ≈ 1.0 (perfect fit)
```

### Example 2: High Scatter

```
Set: noise_variance = 10
Result: R² < 0.5 (scattered data, many outliers)
```

### Example 3: Negative Correlation

```
Set: coefficient_a = -3.0
Result: Downward sloping line
```

### Example 4: Sample Size Effects

```
Set: n_points = 20 (small) vs 500 (large)
Observation: Larger samples give more stable coefficients
```

## 🛠️ Technology Stack

| Category            | Technologies                      |
| ------------------- | --------------------------------- |
| **Language**        | Python 3.11                       |
| **ML Library**      | scikit-learn 1.3.0                |
| **Data Processing** | NumPy 1.24.3, Pandas 2.0.3        |
| **Visualization**   | Plotly 5.15.0, Matplotlib 3.7.2   |
| **Web Frameworks**  | Streamlit 1.25.0, Flask 2.3.2     |
| **Frontend**        | HTML5, CSS3, JavaScript (Vanilla) |

## 📖 Documentation

Detailed documentation is available in the `docs/` directory:

-   **[CRISP-DM Documentation](docs/CRISP_DM_DOCUMENTATION.md)** - Complete methodology implementation
-   **[Quick Start Guide](docs/QUICKSTART.md)** - Step-by-step setup instructions
-   **[Auto-Update Feature](docs/AUTO_UPDATE_FEATURE.md)** - Real-time update functionality
-   **[Project Structure](docs/PROJECT_STRUCTURE.md)** - Code architecture and data flow
-   **[Quick Reference](docs/QUICK_REFERENCE.txt)** - One-page command reference

## 🔬 Testing

The project includes comprehensive unit tests:

```bash
python3 test_model.py
```

**Test Coverage:**

-   ✅ Data generation
-   ✅ Model training
-   ✅ Coefficient calculation
-   ✅ Outlier detection
-   ✅ Visualization generation

## 🎯 Learning Objectives

This project demonstrates:

1. **Linear Regression Fundamentals** - Understanding OLS regression
2. **CRISP-DM Methodology** - Following industry-standard data mining process
3. **Interactive Visualization** - Building engaging data applications
4. **Web Development** - Creating full-stack data science applications
5. **Statistical Analysis** - Interpreting R², residuals, and outliers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Chen Zhixuan**

-   GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

-   Built for IoT Course Assignment
-   Inspired by statistical learning principles
-   Uses scikit-learn for robust ML implementation
-   Visualization powered by Plotly

## 📊 Performance

-   **Data Generation**: < 50ms (500 points)
-   **Model Training**: < 10ms (OLS)
-   **Visualization**: < 100ms
-   **Total Response**: < 200ms ⚡

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐!

---

<div align="center">
  <strong>Built with ❤️ using Python, Flask, Streamlit, and scikit-learn</strong>
  <br>
  <sub>Following CRISP-DM Methodology</sub>
</div>
