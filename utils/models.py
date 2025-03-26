import pickle
import os
import json
import math
from utils.constants import DEPARTMENT_COLUMNS

# Load pre-trained models
loaded_model1 = pickle.load(open('models/model1_pipe_cv.pkl', 'rb'))
loaded_model2 = pickle.load(open('models/model2_pipe_cv.pkl', 'rb'))
loaded_model3 = pickle.load(open('models/model3_pipe_cv.pkl', 'rb'))
loaded_model4 = pickle.load(open('models/model4_pipe_cv.pkl', 'rb'))


# Preprocessing Functions (Original Logic)
def preprocess_input_1(duration_hours, start_date, end_date, order_intake_value):
    duration_days = (end_date - start_date).days
    if duration_days == 0:
        raise ValueError("Duration cannot be zero.")
    else:
        work_intensity = duration_hours / duration_days
        return [[duration_hours, duration_days, order_intake_value, work_intensity]]

def preprocess_input_2(duration_hours, duration_days, order_intake_value, output_1):
    work_intensity = duration_hours / duration_days
    department_diversity = output_1 / total_departments
    average_work_quantity_per_department = duration_hours / output_1
    return [[duration_hours, order_intake_value, duration_days, work_intensity, department_diversity, average_work_quantity_per_department, output_1]]

def preprocess_input_3(duration_hours, total_order_intake, duration_days, num_of_departments, predicted_indices):
    work_intensity = duration_hours / duration_days
    department_diversity = num_of_departments / total_departments
    average_work_quantity_per_department = duration_hours / total_order_intake
    input_data = [duration_hours, total_order_intake, duration_days, work_intensity, department_diversity, average_work_quantity_per_department]
    input_data.extend(predicted_indices)
    input_data.append(num_of_departments)
    return [input_data]

def preprocess_input_4(duration_hours, total_order_intake, duration_days, num_of_employees, predicted_indices, num_of_departments):
    work_intensity = duration_hours / duration_days
    average_work_quantity_per_department = duration_hours / total_order_intake
    duration_to_employees_ratio = duration_days / num_of_employees
    department_diversity = num_of_departments / total_departments
    input_data = [duration_hours, total_order_intake, duration_days, num_of_employees,
                  duration_to_employees_ratio, work_intensity, department_diversity,
                  average_work_quantity_per_department]
    input_data.extend(predicted_indices)
    input_data.append(num_of_departments)
    return [input_data]

# Prediction Functions (Original Logic)
def predict_department_count(input_data):
    return loaded_model1.predict(input_data)[0]



def predict_department_names(input_data):
    predicted_indices = loaded_model2.predict(input_data)
    predicted_names = []

    for prediction in predicted_indices:
        names = [DEPARTMENT_COLUMNS[i] for i, val in enumerate(prediction) if val == 1]
        predicted_names.extend(names)

    # Convert list to JSON format
    department_names_json = json.dumps(predicted_names)

    return department_names_json, predicted_indices

def predict_total_employees(input_data):
    return loaded_model3.predict(input_data)[0]


def predict_department_employees(input_data):
    predicted_employees = loaded_model4.predict(input_data)
    rounded_employees = [math.ceil(emp) for emp in predicted_employees[0]]

    # Create dictionary for department-employee mapping
    department_employee_dict = {
        DEPARTMENT_COLUMNS[i]: rounded_employees[i]
        for i in range(len(rounded_employees)) if rounded_employees[i] > 0
    }
    # Convert dictionary to JSON string
    department_employee_json = json.dumps(department_employee_dict)
    return department_employee_json  # Return JSON-formatted string