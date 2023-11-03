

def createUser(name, contact):
    user = {
        "name" : name,
        "email" : None,
        "telephone" : None
    }
    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact
    return user

user1 = createUser("Ola", "ola@example.com")
user2 = createUser("Kasia", 789987767)

print(user1)
print(user2)