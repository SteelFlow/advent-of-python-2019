import math
import io

def partOne(mass):
    return math.floor(mass / 3) - 2

def calculateFuel(mass):
    fuel = math.floor(mass / 3) - 2
    
    if fuel > 0:
        fuelMass = calculateFuel(fuel)
        return (fuelMass + fuel)
    else:
        return 0


f = open("0102.txt", "r")
input = f.readlines()
f.close()

allFuel = 0

for mass in input:
    if mass == '\n':
        break
    mass = mass.replace('\n','')
    allFuel += calculateFuel(int(mass))

print (allFuel)
