raining = False
haveUmbrella = True
temperature = 11

if not(0<= temperature <40):
    print("Zostań w domu")
elif 0< temperature <=10 and haveUmbrella and raining:
    print("Weź parasolkę")
elif not raining and temperature >=10:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")

