"""
Test script to verify the linear regression model functionality
Run this to ensure the core model works before launching the web apps
"""

from linear_regression_model import LinearRegressionVisualizer
import matplotlib.pyplot as plt


def test_basic_functionality():
    """Test basic model functionality"""
    print("="*60)
    print("Testing Linear Regression Model")
    print("="*60)

    # Create visualizer
    print("\n1. Creating visualizer with default parameters...")
    visualizer = LinearRegressionVisualizer(
        n_points=100,
        coefficient_a=2.0,
        noise_variance=1.0,
        random_seed=42
    )
    print("✓ Visualizer created")

    # Generate data
    print("\n2. Generating synthetic data...")
    x, y = visualizer.generate_data()
    print(f"✓ Generated {len(x)} data points")
    print(f"  X range: [{x.min():.2f}, {x.max():.2f}]")
    print(f"  Y range: [{y.min():.2f}, {y.max():.2f}]")

    # Fit model
    print("\n3. Fitting linear regression model...")
    model = visualizer.fit_model()
    print("✓ Model fitted")

    # Get coefficients
    print("\n4. Model Evaluation:")
    coefficients = visualizer.get_model_coefficients()
    print(
        f"  Coefficient (a): {coefficients['coefficient_a']:.4f} (target: 2.0)")
    print(
        f"  Intercept (b):   {coefficients['intercept_b']:.4f} (target: 5.0)")
    print(f"  R² Score:        {coefficients['r_squared']:.4f}")

    # Get outliers
    print("\n5. Top 5 Outliers:")
    outliers = visualizer.get_outliers(n_outliers=5)
    print(outliers.to_string(index=False))

    # Create visualization
    print("\n6. Creating visualization...")
    plot_data = visualizer.get_plot_data()

    plt.figure(figsize=(10, 6))

    # Plot normal points
    normal_mask = [i not in plot_data['outlier_indices']
                   for i in range(len(plot_data['x']))]
    plt.scatter(plot_data['x'][normal_mask], plot_data['y'][normal_mask],
                alpha=0.6, c='blue', label='Data Points', s=50)

    # Plot outliers
    plt.scatter(plot_data['x'][plot_data['outlier_indices']],
                plot_data['y'][plot_data['outlier_indices']],
                alpha=0.8, c='red', marker='D', label='Outliers (Top 5)', s=100)

    # Plot regression line
    plt.plot(plot_data['x_line'], plot_data['y_line'],
             'g-', linewidth=2, label='Regression Line')

    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.title('Linear Regression: Data Points vs Fitted Line',
              fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save plot
    plt.savefig('test_regression_plot.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_regression_plot.png'")

    print("\n" + "="*60)
    print("All tests passed! ✓")
    print("="*60)
    print("\nYou can now run the web applications:")
    print("  Streamlit: streamlit run streamlit_app.py")
    print("  Flask:     python flask_app.py")
    print("="*60)


if __name__ == "__main__":
    test_basic_functionality()
