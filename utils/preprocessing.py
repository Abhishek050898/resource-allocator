import math
from datetime import datetime

total_departments = 24  # Total number of departments in the company

# Convert inputs for Model 1
def preprocess_input_1(duration_hours, start_date, end_date, order_intake_value):
    duration_days = (end_date - start_date).days
    if duration_days == 0:
        raise ValueError("Duration cannot be zero.")
    work_intensity = duration_hours / duration_days
    return [[duration_hours, duration_days, order_intake_value, work_intensity]]

# Convert inputs for Model 2
def preprocess_input_2(duration_hours, duration_days, order_intake_value, output_1):
    work_intensity = duration_hours / duration_days
    department_diversity = output_1 / total_departments
    avg_work_per_department = duration_hours / output_1
    return [[duration_hours, order_intake_value, duration_days, work_intensity, department_diversity, avg_work_per_department, output_1]]

# Convert inputs for Model 3
def preprocess_input_3(duration_hours, total_order_intake, duration_days, num_of_departments, predicted_indices):
    work_intensity = duration_hours / duration_days
    department_diversity = num_of_departments / total_departments
    avg_work_per_department = duration_hours / total_order_intake
    input_data = [duration_hours, total_order_intake, duration_days, work_intensity, department_diversity, avg_work_per_department]
    input_data.extend(predicted_indices)
    input_data.append(num_of_departments)
    return [input_data]

# Convert inputs for Model 4
def preprocess_input_4(duration_hours, total_order_intake, duration_days, num_of_employees, predicted_indices, num_of_departments):
    work_intensity = duration_hours / duration_days
    avg_work_per_department = duration_hours / total_order_intake
    duration_to_employees_ratio = duration_days / num_of_employees
    department_diversity = num_of_departments / total_departments
    input_data = [duration_hours, total_order_intake, duration_days, num_of_employees,
                  duration_to_employees_ratio, work_intensity, department_diversity,
                  avg_work_per_department]
    input_data.extend(predicted_indices)
    input_data.append(num_of_departments)
    return [input_data]
