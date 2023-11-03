#operatory logiczne

print( True and True) #True
print( True and False) #False
print( False and True) #False
print( False and False) #False

taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >=50:
    print("Go home")

print( True or True) #True   
print( True or False) #True   
print( False or False) #False   

if 10>5 or "Ania" != "Ola":
    print("true or true")

if 3==5 or "Ania" == "Ola":
    print("false or false")

taskCompleted = True
if taskCompleted == True:
    print("Go home")

if not taskCompleted:
    print("Stay a bit longer and finish")