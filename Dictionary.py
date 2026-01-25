info={
    "name":"Phuke",
    "cgpa":8.5,
    "subjects":["PDS","os"],
    99:"number"
}

print(info)

#Access particulary key's value
infoCgpa=info["cgpa"]
print(infoCgpa)

#find dictionary keys
dict_keys=info.keys()
print(dict_keys)

#convert keys in a list

list_of_keys=list(dict_keys)
print(list_of_keys)

#find dictionary values

dict_values=info.values()
print(dict_values)

#items

dict_items=info.items()
print(dict_items)

#get the key's value 
#if key is not present return none

dict_get_values=info.get("cgpa2") #as this is wrong key ----->return none
print(dict_get_values)

#update existing dictionary
info.update({
    "city":"Sivasagar"
})

print(info)