import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the patients dataset
# Ensure your CSV file is in the same folder as this script
try:
    df = pd.read_csv('patients_data.csv')
except FileNotFoundError:
    print("Error: The file 'patients_data.csv' was not found.")
    exit()

# 2. Function to calculate Body Mass Index (BMI)
def calculate_bmi(row):
    # BMI = weight(kg) / height(m)^2
    bmi = row['Weight_kg'] / (row['Height_cm'] / 100)**2
    return round(bmi, 2)

# 3. Advanced Clinical Triage Logic
# Evaluates vital signs to categorize patient priority
def evaluate_triage(row):
    # URGENT: Critical thresholds requiring immediate medical attention
    if (row['SpO2'] < 90 or 
        row['Heart_Rate'] > 120 or row['Heart_Rate'] < 40 or
        row['Resp_Rate'] > 30 or row['Resp_Rate'] < 8 or
        row['SBP'] < 90 or row['SBP'] >= 180):
        return 'URGENT'
    
    # OBSERVATION: Abnormal thresholds requiring monitoring
    elif (90 <= row['SpO2'] <= 94 or 
          100 < row['Heart_Rate'] <= 120 or 
          20 < row['Resp_Rate'] <= 30 or 
          140 <= row['SBP'] < 180):
        return 'OBSERVATION'
    
    # STABLE: Normal physiological parameters
    else:
        return 'STABLE'

# 4. Apply the clinical functions to the dataset (Batch Processing)
df['BMI'] = df.apply(calculate_bmi, axis=1)
df['Triage_Status'] = df.apply(evaluate_triage, axis=1)

# 5. Save the processed data to a new CSV file
df.to_csv('advanced_triage_results.csv', index=False)
print("Data processing complete. Results saved to 'advanced_triage_results.csv'.")
print("-" * 40)
print(df[['Name', 'Triage_Status']].head(10)) # Display the first 10 results

# 6. Data Visualization: Generate a bar chart for the triage distribution
status_counts = df['Triage_Status'].value_counts()

# Assign specific medical colors to each triage category
color_map = {'STABLE': '#2ecc71', 'OBSERVATION': '#f39c12', 'URGENT': '#e74c3c'}
bar_colors = [color_map.get(status, '#3498db') for status in status_counts.index]

# Plotting the data
plt.figure(figsize=(8, 6))
status_counts.plot(kind='bar', color=bar_colors, edgecolor='black')
plt.title('Clinical Triage Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Triage Category', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the chart as an image for the portfolio
plt.savefig('triage_chart.png')
print("Chart generated and saved as 'triage_chart.png'.")
plt.show()