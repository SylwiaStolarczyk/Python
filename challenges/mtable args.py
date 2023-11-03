employee = {
    "name": "Adam",
    "email": "adam@example.com", 
    "rank": "programmer", 
    "salary": 8000
}

def promoteToManager(user):
    if user["rank"] == "manager":
        print("Pracownik jest już managerem")
        return
    user["rank"] = "manager"
    salary = user["salary"]
    user["salary"] = salary + (salary * 1.5)

promoteToManager(employee)
print(employee)