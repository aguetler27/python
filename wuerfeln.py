# wuerfeln.py
from random import randint
# 100 mal würfel simulieren
# anzahl der 1er, 2er usw. ausgeben

print("Wuerfel-Simulator")
anzahl = int(input("Wie oft soll gewuerfelt werden? "))

einser = 0
zweier = 0
dreier = 0
vierer = 0
fuenfer = 0
sechser = 0

for i in range(0,anzahl):
    zahl = randint(1,6)
    if (zahl == 1):
        einser+= 1
    if (zahl == 2):
        zweier+= 1
    if (zahl == 3):
        dreier+= 1
    if (zahl == 4):
        vierer+= 1
    if (zahl == 5):
        fuenfer+= 1
    if (zahl == 6):
        sechser+= 1

print("Anzahl Wuerfe: ", anzahl)
print("1er : ", einser)
print("2er : ", zweier)
print("3er : ", dreier)
print("4er : ", vierer)
print("5er : ", fuenfer)
print("6er : ", sechser)
