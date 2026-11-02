#Engineering Data Acquisition Framework - utils.py


#This module defines reusable functions: get_float() and get_dataInput()





#Define the get_float() function to validate input, handle errors/exception, and return a float value

def get_float(prompt):

    while True:

        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print("Invalid number format. Please try again")	






#Define the get_dataInput() function: will convert the input into a dictionary with nested dictionaries
#Adds formatted/corresponding units of measurement

from datetime import datetime

def get_dataInput(pressure, temperature, flow_rate):
    
    #Retrieve date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #create the new dictionary
    dataInput = {
        "Timestamp" : timestamp,
        "Pressure_Sensor" : {"Reading" : pressure, "Units" : 'psi'},
        "Temperature_Sensor" : {"Reading" : temperature, "Units" : '°C'},
        "Flow_Rate_Sensor" : {"Reading" : flow_rate, "Units" : 'kg/s'}
    }
    return dataInput