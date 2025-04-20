dict = {
    "name": "Shubham",
    True: "Angu",
    "age": 3,
    345: "Suresh"
}

print(dict[True])
print(dict[345])
print(dict)

# With get syntax the difference is that if no key is present with the name then None will be returned
print(dict.get("name"))

# to access all the keys
print(dict.keys())

for key in dict.keys():
    print(dict[key])
    
# To access all the values
print(dict.values())

# to print key value pairs
print(dict.items())

for key,value in dict.items():
    print(f"Value corresponding to key {key} is {value}")