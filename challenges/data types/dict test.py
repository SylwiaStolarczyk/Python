config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"

}

print("Ilość elementów słownika:", len(config))
print(config["dbType"])

#print(config.keys())
#print(config.values())
for key, values in config.items():
    print("Klucz w config:", key, "z wartością", values)