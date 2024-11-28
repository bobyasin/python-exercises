# key value pair,
customer = {
    "name": "yasin",
    "email": "b@gmail.com",
    "age": 34
}

print(customer["name"])

customer["age"] = 35
print(customer["age"])

customer["birth_date"] = "Jan 3 1990"
print(customer.get("birth_date"))

print(customer)