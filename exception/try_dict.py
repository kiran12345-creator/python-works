d = {"name": "arun", "age": 23, "place": "ekm"}

try:
    key = input("Enter a key: ")
    print("Value:", d[key])

except KeyError:
    print("Key does not exist")