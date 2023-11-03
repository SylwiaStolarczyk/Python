capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

zwrot = capital*rateOfInterest
spadek = capital*inflationRate

print("zwrot inwestycji:", zwrot)
print("spadek wartości kapitalu jest o", spadek)

print("wartość kapitału rok po inwestycji", capital + zwrot - spadek)