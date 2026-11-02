#Engineering Data Acquisition Framework - validation.py

#This module defines the validate_data() function which
#determines if recorded readings are valid



#Specify the valid ranges by assigning minimum and maximum values

MIN_PRESSURE = 0
MAX_PRESSURE = 300

MIN_TEMPERATURE = -50
MAX_TEMPERATURE = 200

MIN_FLOW_RATE = 0
MAX_FLOW_RATE = 10




#The validate_data() function assigns a True value to Valid readings
#and assigns False to Invalid readings

def validate_data(dataInput):

    #Retrieve p,t,f from dataInput dictionary:
    pressure = dataInput["Pressure_Sensor"]["Reading"]
    temperature = dataInput["Temperature_Sensor"]["Reading"]
    flow_rate = dataInput["Flow_Rate_Sensor"]["Reading"]

    #Validate pressure, add indicator to dictionary
    if MIN_PRESSURE <= pressure <= MAX_PRESSURE:
        dataInput["Pressure_Sensor"]["Valid"] = True
    else:
        dataInput["Pressure_Sensor"]["Valid"] = False

    #Validate temperature, add indicator to dictionary
    if MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
        dataInput["Temperature_Sensor"]["Valid"] = True
    else:
        dataInput["Temperature_Sensor"]["Valid"] = False

    #Validate flow rate, add indicator to dictionary
    if MIN_FLOW_RATE <= flow_rate <= MAX_FLOW_RATE:
        dataInput["Flow_Rate_Sensor"]["Valid"] = True
    else:
        dataInput["Flow_Rate_Sensor"]["Valid"] = False
    
    return dataInput















    #Loop through the dataInput dictionary keys: p_check,t_check,f_check
#    for sensor, Reading in dataInput.items():

#        #validate each reading, add a key to each dictionary, indicates pass or fail
 #       match dataInput[i]:

#            case dataInput[0]:
            
 #               if pressure < MIN_PRESSURE or pressure > MAX_PRESSURE:
  #                  status = "Fail'
   #             else:
   #                 status = "Pass"
        
    #        case dataInput[1]:
            
     #           if temperature < MIN_TEMPERATURE or temperature > MAX_TEMPERATURE:
      #              status = "Fail'
      #          else:
       #             status = "Fail'
        
        #    case dataInput[2]:
                
         #       if flow_rate < MIN_FLOW_RATE or flow_rate > MAX_FLOW_RATE:
          #          status = "Fail'
           #     else:
            #        status = "Fail'
    
    #return dataInput 




    
    
    
    
    
    