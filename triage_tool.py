import datetime

print("--- Digital Health Assistant: Triage & BMI Tool ---")

# Step 1: Patient Information
patient_name = input("Enter Patient Name: ")

# Step 2: BMI Calculation
print("\n[Section 1: Body Mass Index (BMI)]")
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
bmi_result = round(bmi, 2)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal weight"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

# Step 3: Vital Signs Assessment
print("\n[Section 2: Vital Signs Assessment]")
temp = float(input("Enter Body Temperature (°C): "))
heart_rate = int(input("Enter Heart Rate (BPM): "))
spo2 = int(input("Enter Oxygen Saturation (SpO2 %): "))

# Triage Logic
if temp > 38.0 or spo2 < 92 or heart_rate > 100:
    health_status = "URGENT"
    recommendation = "Clinical consultation or ER visit is advised."
elif 36.5 <= temp <= 37.5 and spo2 >= 95 and 60 <= heart_rate <= 100:
    health_status = "STABLE"
    recommendation = "All parameters are within the normal range."
else:
    health_status = "OBSERVATION REQUIRED"
    recommendation = "Minor deviations detected. Rest and re-check later."

# Step 4: Generating the Report Content
report_content = f"""
=========================================
MEDICAL ASSESSMENT REPORT
=========================================
Patient Name: {patient_name}
Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

[BMI ANALYSIS]
- BMI: {bmi_result}
- Classification: {status}

[VITAL SIGNS]
- Temperature: {temp} C
- Heart Rate: {heart_rate} BPM
- SpO2: {spo2} %

[FINAL ASSESSMENT]
- Health Status: {health_status}
- Recommendation: {recommendation}
=========================================
"""

# Print to Terminal
print(report_content)

# Step 5: Save to File
file_name = f"{patient_name.replace(' ', '_')}_Report.txt"
with open(file_name, "w") as file:
    file.write(report_content)

print(f"Success! Report saved as: {file_name}")