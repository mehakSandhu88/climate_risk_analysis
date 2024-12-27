# climate_risk_analysis_tool.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Function to load and preprocess data
def load_and_preprocess_data(file_path):
    # Load the climate data
    data = pd.read_csv(file_path)
    
    # Basic data preprocessing
    data.dropna(inplace=True)  # Remove rows with missing values
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')  # Ensure the 'Year' column is in datetime format
    
    # For simplicity, assume we're predicting 'Risk Score' based on 'Temperature' and 'Precipitation'
    # You may need to adjust this depending on your dataset's actual columns
    return data[['Year', 'Temperature', 'Precipitation', 'RiskScore']]

# Function to train a machine learning model
def train_model(data):
    # Split data into features (X) and target (y)
    X = data[['Temperature', 'Precipitation']]
    y = data['RiskScore']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model, X_test, y_test, y_pred

# Function to visualize the results
def visualize_results(y_test, y_pred, X_test):
    # Visualize the predictions vs actual risk scores
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test['Temperature'], y_test, color='blue', label='Actual Risk')
    plt.scatter(X_test['Temperature'], y_pred, color='red', label='Predicted Risk')
    plt.xlabel('Temperature')
    plt.ylabel('Risk Score')
    plt.title('Climate Risk vs Temperature')
    plt.legend()
    plt.show()

    # Plotting the actual vs predicted risk score
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label='Actual Risk')
    plt.plot(y_pred, label='Predicted Risk', linestyle='--')
    plt.xlabel('Test Samples')
    plt.ylabel('Risk Score')
    plt.title('Actual vs Predicted Risk Scores')
    plt.legend()
    plt.show()

# Main function to run the analysis
def run_climate_risk_analysis(file_path):
    # Load and preprocess data
    data = load_and_preprocess_data(file_path)
    
    # Train the model
    model, X_test, y_test, y_pred = train_model(data)
    
    # Visualize the results
    visualize_results(y_test, y_pred, X_test)

# Run the analysis with your dataset
if __name__ == "__main__":
    file_path = 'climate_data.csv'  # Example CSV file path
    run_climate_risk_analysis(file_path)
