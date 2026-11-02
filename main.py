#Engineering Data Acquisition Framework - main.py
#Bryan Martinez

#This software tool logs pressure readings, validates sensor data, 
#and stores the results in a CSV file.


#Import the required functions

from utils import get_float
from utils import get_dataInput
from validation import validate_data
from display_data import get_report
from sensor_logger import log_data



#1. Call the get_float() function
#Obtains Pressure, Temperature, and Flow Rate float inputs
pressure = get_float("Enter recorded pressure: ")
temperature = get_float("Enter recorded temperature: ")
flow_rate = get_float("Enter recorded flow rate: ")



#2. Call the get_dataInput() function
#Stores timestamp and the input data: pressure, temperature, flow rate
dataInput = get_dataInput(pressure, temperature, flow_rate)
#print(dataInput)



#3. Call the validate_data() function
#Determines if the data readings/measurments are within a valid range
dataInput = validate_data(dataInput)
#print(dataInput)



#4. Call the get_report() function
#Generates a formatted data report and adds a PASS/FAIL status for each recorded reading
get_report(dataInput)



#5. Call the log_data() function 
#Logs the formatted data report to a CSV file 
log_data(dataInput)