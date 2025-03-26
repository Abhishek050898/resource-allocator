import pandas as pd
import os
from datetime import datetime
import json
import streamlit as st
from utils.constants import DATA_LOG_CSV

def ensure_csv_exists():
    if not os.path.exists(DATA_LOG_CSV):
        df = pd.DataFrame(columns=[
            "Project Name", "Order Intake", "Duration Hours", "Start Date", "End Date",
            "Department Count", "Department Names", "Total Employees", "Department Employees", "Timestamp"
        ])
        df.to_csv(DATA_LOG_CSV, index=False)
        print("Created 'data_log.csv' as it was missing.")

# Log Data Function
def log_data(user_inputs, prediction_type, prediction_value):
    
    user_inputs["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Convert dictionary to JSON string if storing department employees
    if prediction_type == "Department Employees":
        prediction_value = json.dumps(prediction_value)
    if prediction_type == "Department Names":
        prediction_value = json.dumps(prediction_value)

    # Load existing data if CSV exists
    if os.path.exists(DATA_LOG_CSV):
        df = pd.read_csv(DATA_LOG_CSV)
    else:
        df = pd.DataFrame()

    # Check if project already exists
    if not df.empty and "Project Name" in df.columns:
        existing_row = df[df["Project Name"] == user_inputs["Project Name"]]
        if not existing_row.empty:
            row_index = existing_row.index[0]
            df.loc[row_index, prediction_type] = prediction_value
            df.loc[row_index, "Timestamp"] = user_inputs["Timestamp"]
        else:
            df = pd.concat([df, pd.DataFrame([{**user_inputs, prediction_type: prediction_value}])], ignore_index=True)
    else:
        df = pd.DataFrame([{**user_inputs, prediction_type: prediction_value}])

    # Save to CSV
    df.to_csv(DATA_LOG_CSV, index=False)
    st.success("Prediction logged successfully!")
