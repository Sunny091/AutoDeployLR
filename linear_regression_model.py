"""
Linear Regression Model Module
Implements core functionality for synthetic data generation and linear regression
following CRISP-DM methodology
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd


class LinearRegressionVisualizer:
    """
    A class to handle linear regression modeling and visualization

    CRISP-DM Steps:
    - Data Preparation: generate_data()
    - Modeling: fit_model()
    - Evaluation: calculate_residuals(), get_outliers()
    """

    def __init__(self, n_points=100, coefficient_a=2.0, noise_variance=1.0, random_seed=42):
        """
        Initialize the visualizer with data generation parameters

        Args:
            n_points (int): Number of data points to generate
            coefficient_a (float): Coefficient 'a' in y = ax + b + noise
            noise_variance (float): Variance of the noise term
            random_seed (int): Random seed for reproducibility
        """
        self.n_points = n_points
        self.coefficient_a = coefficient_a
        self.noise_variance = noise_variance
        self.random_seed = random_seed

        # Data attributes
        self.x = None
        self.y = None
        self.x_reshaped = None

        # Model attributes
        self.model = None
        self.y_pred = None
        self.residuals = None

    def generate_data(self):
        """
        Generate synthetic data following y = ax + b + noise

        Data Understanding & Preparation (CRISP-DM):
        - Creates x values uniformly distributed
        - Generates y values with linear relationship plus Gaussian noise
        """
        np.random.seed(self.random_seed)

        # Generate x values uniformly distributed between 0 and 10
        self.x = np.random.uniform(0, 10, self.n_points)

        # True intercept (b) is set to 5
        true_b = 5.0

        # Generate noise with specified variance
        noise = np.random.normal(0, np.sqrt(
            self.noise_variance), self.n_points)

        # Generate y values: y = ax + b + noise
        self.y = self.coefficient_a * self.x + true_b + noise

        # Reshape x for sklearn (needs 2D array)
        self.x_reshaped = self.x.reshape(-1, 1)

        return self.x, self.y

    def fit_model(self):
        """
        Fit linear regression model to the generated data

        Modeling (CRISP-DM):
        - Uses sklearn's LinearRegression
        - Fits model to capture relationship between x and y
        """
        if self.x is None or self.y is None:
            self.generate_data()

        # Initialize and fit the model
        self.model = LinearRegression()
        self.model.fit(self.x_reshaped, self.y)

        # Generate predictions
        self.y_pred = self.model.predict(self.x_reshaped)

        return self.model

    def calculate_residuals(self):
        """
        Calculate residuals (prediction errors)

        Evaluation (CRISP-DM):
        - Computes difference between actual and predicted values
        """
        if self.y_pred is None:
            self.fit_model()

        self.residuals = np.abs(self.y - self.y_pred)
        return self.residuals

    def get_model_coefficients(self):
        """
        Get the fitted model coefficients

        Returns:
            dict: Dictionary containing coefficient (a) and intercept (b)
        """
        if self.model is None:
            self.fit_model()

        return {
            'coefficient_a': self.model.coef_[0],
            'intercept_b': self.model.intercept_,
            'r_squared': self.model.score(self.x_reshaped, self.y)
        }

    def get_outliers(self, n_outliers=5):
        """
        Identify top n outliers based on residuals

        Evaluation (CRISP-DM):
        - Identifies points with largest prediction errors

        Args:
            n_outliers (int): Number of top outliers to return

        Returns:
            pandas.DataFrame: DataFrame with outlier information
        """
        if self.residuals is None:
            self.calculate_residuals()

        # Get indices of top outliers
        outlier_indices = np.argsort(self.residuals)[-n_outliers:][::-1]

        # Create DataFrame with outlier information
        outliers_df = pd.DataFrame({
            'Point': outlier_indices + 1,  # 1-indexed for display
            'X': self.x[outlier_indices],
            'Y (Actual)': self.y[outlier_indices],
            'Y (Predicted)': self.y_pred[outlier_indices],
            'Residual': self.residuals[outlier_indices]
        })

        return outliers_df

    def get_plot_data(self):
        """
        Get all data needed for plotting

        Returns:
            dict: Dictionary containing x, y, predictions, and outliers
        """
        if self.model is None:
            self.fit_model()

        if self.residuals is None:
            self.calculate_residuals()

        # Get outlier indices (top 5)
        outlier_indices = np.argsort(self.residuals)[-5:]

        return {
            'x': self.x,
            'y': self.y,
            'y_pred': self.y_pred,
            'outlier_indices': outlier_indices,
            'x_line': np.array([self.x.min(), self.x.max()]),
            'y_line': self.model.predict(np.array([[self.x.min()], [self.x.max()]]))
        }
