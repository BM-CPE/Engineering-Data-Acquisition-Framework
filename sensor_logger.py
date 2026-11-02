#Engineering Data Acquisition Framework - sensor_logger.py

#This module defines the log_data() function



#Import the 'os' and 'csv' modules
import os
import csv

#Assign the CSV file name and header
CSV_FILE = "data/sensor_log.csv"
CSV_HEADER = [
    "Date/Time",
    "Pressure (psi)",
    "Pressure Status",
    "Temperature (°C)",
    "Temperature Status",
    "Flow Rate (kg/s)",
    "Flow Rate Status"
]


#The log_data function accepts the dataInput sensor measurement information and logs it to a CSV file

def log_data(dataInput):

    timestamp = dataInput["Timestamp"]

    pressure = dataInput["Pressure_Sensor"]["Reading"]
    pressure_status = dataInput["Pressure_Sensor"]["Valid"]
    pressure_status = "PASS" if pressure_status else "FAIL"

    temperature = dataInput["Temperature_Sensor"]["Reading"]
    temperature_status = dataInput["Temperature_Sensor"]["Valid"]
    temperature_status = "PASS" if temperature_status else "FAIL"

    flow_rate = dataInput["Flow_Rate_Sensor"]["Reading"]
    flow_rate_status = dataInput["Flow_Rate_Sensor"]["Valid"]
    flow_rate_status = "PASS" if flow_rate_status else "FAIL"

    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADER)
            writer.writerow([timestamp, pressure, pressure_status, 
                             temperature, temperature_status, 
                             flow_rate, flow_rate_status])

        print("\nNew CSV File Created\nSensor Data Logged Successfully")   

    else:
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, pressure, pressure_status, 
                             temperature, temperature_status, 
                             flow_rate, flow_rate_status])

        print("\nSensor Data Logged Successfully")