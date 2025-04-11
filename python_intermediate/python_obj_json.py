#program to demostrate a json module 

import json 

employee_dict = {'id': '09', 'name': 'samarth', 'department': 'digital'} 
print("This is Python", type(employee_dict)) 

print("\nNow Convert from Python to JSON") 

json_object = json.dumps(employee_dict, indent=4) 
print("Converted to JSON", type(json_object)) 
print(json_object) 
