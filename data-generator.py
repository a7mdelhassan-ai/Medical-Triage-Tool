import pandas as pd
import numpy as np

# Define the number of patients
n_patients = 500

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic medical data (normal distribution)
data = {
    'Name': [f'Patient_{i}' for i in range(1, n_patients + 1)],
    'Weight_kg': np.random.normal(75, 15, n_patients).round(1),
    'Height_cm': np.random.normal(170, 10, n_patients).round(1),
    'Temp_C': np.random.normal(37.0, 0.8, n_patients).round(1),
    'Heart_Rate': np.random.normal(85, 20, n_patients).astype(int),
    'SpO2': np.clip(np.random.normal(96, 4, n_patients), 70, 100).astype(int),
    'Resp_Rate': np.random.normal(18, 5, n_patients).astype(int),
    'SBP': np.random.normal(125, 20, n_patients).astype(int),
    'DBP': np.random.normal(80, 12, n_patients).astype(int)
}

# Convert dictionary to a DataFrame and save as a CSV file
df = pd.DataFrame(data)
df.to_csv('patients_data.csv', index=False)

print(f"Successfully created 'patients_data.csv' with {n_patients} medical records.")