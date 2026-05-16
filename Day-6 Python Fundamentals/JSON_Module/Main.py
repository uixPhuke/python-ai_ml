import json

with open("data.json", "r") as file:
    data = json.load(file) #Converts JSON file to Python dictionary
print(data)
print(type(data))

py_object = {"name": "Alice", "age": 25, "city": "Los Angeles"}
with open("data.json", "w") as f:
    json.dump(py_object, f, indent=4,sort_keys=True) #Converts Python dictionary to JSON file 

