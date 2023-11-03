age = 18
weight = 47
if ((age >= 18) and (weight>=50)):
    print("Kandydat może oddać krew")
elif ((age<18) and (weight >=50)):
    print ("Kandydat nie może oddać krwi ponieważ jego wiek jest poniżej 18 rż")
elif ((age>=18) and (weight <50)):
    print("kandydat nie może oddać krwi bo jego waga jest poniżej 50 kg")
else:
    print("Kandydat nie może oddać krwi bo jego wiek jest poniżej 18 i waga poniżej 50 kg")
