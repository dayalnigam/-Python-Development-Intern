#3: Write a Python program to convert the Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
import json  
dictionary ={  
  "id": "04",  
  "name": "sunil",  
  "depatment": "HR"
}  
for i in sorted(dictionary.values()):
    json_object = json.dumps(i, indent = 4)
    print(json_object) 