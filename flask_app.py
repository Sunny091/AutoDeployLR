"""
Flask Interactive Linear Regression Visualizer

This application demonstrates linear regression following the CRISP-DM methodology
with a Flask backend and HTML/JavaScript frontend.

Usage: python flask_app.py
Then open http://localhost:5000 in your browser
"""

from flask import Flask, render_template, request, jsonify
import json
from linear_regression_model import LinearRegressionVisualizer

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate data and fit model based on user parameters

    Expected JSON input:
    {
        "n_points": int,
        "coefficient_a": float,
        "noise_variance": float,
        "random_seed": int
    }

    Returns JSON with plot data and model evaluation
    """
    try:
        # Get parameters from request
        data = request.get_json()

        n_points = int(data.get('n_points', 100))
        coefficient_a = float(data.get('coefficient_a', 2.0))
        noise_variance = float(data.get('noise_variance', 1.0))
        random_seed = int(data.get('random_seed', 42))

        # Validate inputs
        if not (20 <= n_points <= 500):
            return jsonify({'error': 'n_points must be between 20 and 500'}), 400
        if not (-5.0 <= coefficient_a <= 5.0):
            return jsonify({'error': 'coefficient_a must be between -5.0 and 5.0'}), 400
        if not (0.0 <= noise_variance <= 10.0):
            return jsonify({'error': 'noise_variance must be between 0.0 and 10.0'}), 400

        # Create visualizer and generate data
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

        # Get model coefficients
        coefficients = visualizer.get_model_coefficients()

        # Get outliers
        outliers_df = visualizer.get_outliers(n_outliers=5)

        # Prepare response
        response = {
            'plot_data': {
                'x': plot_data['x'].tolist(),
                'y': plot_data['y'].tolist(),
                'y_pred': plot_data['y_pred'].tolist(),
                'outlier_indices': plot_data['outlier_indices'].tolist(),
                'x_line': plot_data['x_line'].tolist(),
                'y_line': plot_data['y_line'].tolist()
            },
            'coefficients': {
                'coefficient_a': round(coefficients['coefficient_a'], 4),
                'intercept_b': round(coefficients['intercept_b'], 4),
                'r_squared': round(coefficients['r_squared'], 4)
            },
            'outliers': outliers_df.to_dict('records'),
            'target_coefficient': coefficient_a
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
