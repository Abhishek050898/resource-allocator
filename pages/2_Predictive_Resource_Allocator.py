import streamlit as st
import os
from datetime import datetime
import json
from utils.preprocessing import preprocess_input_1, preprocess_input_2, preprocess_input_3, preprocess_input_4
from utils.models import predict_department_count, predict_department_names, predict_total_employees, predict_department_employees
from utils.logger import log_data, ensure_csv_exists
from utils.fileupload import upload_file_to_sharepoint
import pandas as pd

CSV_FILE = "data_log.csv" # CSV file to store inputs and outputs
document_library = "PowerBI_Equans_Data"  # Change to the correct document library name
upload_folder = "Live_Logs"  # Target folder in SharePoint

# def main():
#     st.title('🏗️ Dynamic Resource Planning Tool for Construction Projects 🏗️')
#     st.markdown("---")

#     with st.container():
#         project_name = st.text_input("Project Name", placeholder="Enter project name")
#         order_intake_value = st.number_input("Order Intake (Cost in '000 EUR)", value=None, placeholder="Enter order intake value")
#         duration_hours = st.number_input("Duration (Project Hours)", value=None, placeholder="Enter project duration")
#         start_date = st.date_input("Start Date (YYYY/MM/DD)")
#         end_date = st.date_input("End Date (YYYY/MM/DD)")

#     if not project_name or order_intake_value is None or duration_hours is None or start_date is None or end_date is None:
#         st.error('Please fill in all the input fields.')
#         return
    
#     if duration_hours <= 0 or order_intake_value <= 0:
#         st.error('Duration and Order Intake value must be greater than zero.')
#         return
    
#     if start_date >= end_date:
#         st.error('Start date must be before the end date.')
#         return

#     user_inputs = {
#         "Project Name": project_name,
#         "Order Intake": order_intake_value,
#         "Duration Hours": duration_hours,
#         "Start Date": start_date.strftime("%Y-%m-%d"),
#         "End Date": end_date.strftime("%Y-%m-%d")
#     }

#     try:
#         input_data_1 = preprocess_input_1(duration_hours, start_date, end_date, order_intake_value)
#     except ValueError as e:
#         st.error(str(e))
#         return
    
#     output_1 = predict_department_count(input_data_1)
#     input_data_2 = preprocess_input_2(duration_hours, input_data_1[0][1], order_intake_value, output_1)
#     predicted_names, predicted_indices = predict_department_names(input_data_2)
#     total_employees = predict_total_employees(preprocess_input_3(duration_hours, order_intake_value, input_data_1[0][1], output_1, predicted_indices[0]))
#     department_employees = predict_department_employees(preprocess_input_4(duration_hours, order_intake_value, input_data_1[0][1], total_employees, predicted_indices[0], output_1))

#     if st.button('Predict Department Count'):
#         st.success(f'Number of predicted departments: {output_1}')
#         log_data(user_inputs, "Department Count", output_1)

#     if st.button('Predict Department Names'):
#         st.success(f'Predicted department names:\n{predicted_names}')
#         log_data(user_inputs, "Department Names", predicted_names)

#     if st.button('Predict Total Number of Employees'):
#         st.success(f'Total predicted employees: {int(total_employees)}')
#         log_data(user_inputs, "Total Employees", int(total_employees))

#     if st.button('Predict Number of Employees in Each Department'):
#         st.success(f'Predicted employees per department:\n{department_employees}')
#         log_data(user_inputs, "Department Employees", department_employees)


# ensure_csv_exists()

# if __name__ == '__main__':
#     main()
#     result = upload_file_to_sharepoint(CSV_FILE, document_library, upload_folder)

def ensure_csv_exists():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=[
            "Project Name", "Order Intake", "Duration Hours", "Start Date", "End Date",
            "Department Count", "Department Names", "Total Employees", "Department Employees", "Timestamp"
        ])
        df.to_csv(CSV_FILE, index=False)
        print("Created 'data_log.csv' as it was missing.")

# Main Function
def main():
    st.title('🏗️ Dynamic Resource Planning Tool for Construction Projects 🏗️')
    st.markdown("---")

    with st.container():
        project_name = st.text_input("Project Name", placeholder="Enter project name")
        order_intake_value = st.number_input("Order Intake (Cost in '000 EUR)", value=None, placeholder="Enter order intake value")
        duration_hours = st.number_input("Duration (Project Hours)", value=None, placeholder="Enter project duration")
        start_date = st.date_input("Start Date (YYYY/MM/DD)")
        end_date = st.date_input("End Date (YYYY/MM/DD)")

    if not project_name or order_intake_value is None or duration_hours is None or start_date is None or end_date is None:
        st.error('Please fill in all the input fields.')
        return
    
    if duration_hours <= 0 or order_intake_value <= 0:
        st.error('Duration and Order Intake value must be greater than zero.')
        return
    
    if start_date >= end_date:
        st.error('Start date must be before the end date.')
        return

    user_inputs = {
        "Project Name": project_name,
        "Order Intake": order_intake_value,
        "Duration Hours": duration_hours,
        "Start Date": start_date.strftime("%Y-%m-%d"),
        "End Date": end_date.strftime("%Y-%m-%d")
    }

    try:
        input_data_1 = preprocess_input_1(duration_hours, start_date, end_date, order_intake_value)
    except ValueError as e:
        st.error(str(e))
        return
    
    output_1 = predict_department_count(input_data_1)
    input_data_2 = preprocess_input_2(duration_hours, input_data_1[0][1], order_intake_value, output_1)
    predicted_names, predicted_indices = predict_department_names(input_data_2)
    total_employees = predict_total_employees(preprocess_input_3(duration_hours, order_intake_value, input_data_1[0][1], output_1, predicted_indices[0]))
    department_employees = predict_department_employees(preprocess_input_4(duration_hours, order_intake_value, input_data_1[0][1], total_employees, predicted_indices[0], output_1))

    if st.button('Predict Department Count'):
        st.success(f'Number of predicted departments: {output_1}')
        log_data(user_inputs, "Department Count", output_1)

    if st.button('Predict Department Names'):
        st.success(f'Predicted department names:\n{predicted_names}')
        log_data(user_inputs, "Department Names", predicted_names)

    if st.button('Predict Total Number of Employees'):
        st.success(f'Total predicted employees: {int(total_employees)}')
        log_data(user_inputs, "Total Employees", int(total_employees))

    if st.button('Predict Number of Employees in Each Department'):
        st.success(f'Predicted employees per department:\n{department_employees}')
        log_data(user_inputs, "Department Employees", department_employees)


ensure_csv_exists()


# Run the main application
if __name__ == '__main__':
    main()
     # Upload the CSV file to SharePoint only after ensuring it exists
    result = upload_file_to_sharepoint(CSV_FILE, document_library, upload_folder)
    print(result)

   