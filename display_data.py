#Engineering Data Acquisition Framework - display_data.py

#This module defines the get_report() function




#The get_report() function generates and displays 
#the formatted sensor data input measurement report

def get_report(dataInput):

    #Print banner
    print("\n============================\n"
          "EDAF REPORT\n"
          "============================\n")

    #Print timestamp
    timestamp = dataInput["Timestamp"]
    print(f"Timestamp: {timestamp}\n")

    #Print sensor readings, units, and validity for each sensor
    for key, value in dataInput.items():

        #Use an 'if' statement and 'continue' keyword to skip the timestamp key
        if key == "Timestamp":
            continue
        else:
            display_key = key.replace("_", " ")

            reading = value["Reading"]
            units = value["Units"]
            valid = value["Valid"]
            status = "PASS" if valid else "FAIL" 
            
            #this prints in one line:
            #print(f"{key} {reading} {units} {valid}")

            #Format the output
            print(f"{display_key:<25} {reading:<5} {units:<6} {status}")