contacts = {
    "Ola" : "ola@ing.pl",
    "Bartek" : "bartek@ing.pl",
    "Daniel" : 30
}

contacts["Rafał"] = "rafal@ing.pl"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts))
print(len(contacts))

print(contacts.keys())
print(contacts.values())

for key in contacts:
    print(key+" "+ str(contacts[key]))

for key, value in contacts.items():
    print(key, " ", value)