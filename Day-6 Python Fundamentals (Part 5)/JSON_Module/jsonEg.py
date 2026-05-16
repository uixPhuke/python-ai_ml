import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string) #Converts JSON string to Python dictionary

print(data)
print(type(data))

py_object = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(py_object) #Converts Python dictionary to JSON string
print(json_string)
print(type(json_string))