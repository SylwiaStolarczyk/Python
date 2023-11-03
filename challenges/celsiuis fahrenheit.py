def CToF(celsius):
    fahrenheit = celsius * 9 / 5 +32
    print(celsius, "\xB0 Celsiusza to", fahrenheit, "\xB0 Fahrenheita")

def FToC(fahrenheit):
    celsius = (fahrenheit -32) * 5 / 9
    print(fahrenheit, "\xB0 Fahrenheita to", celsius, "\xB0 Celsiusza")


print(CToF(20))
print(FToC(86))