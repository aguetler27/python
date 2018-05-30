# fibonacci-numbers.py

#1,1 => 1+1 = 2
#1,1,2 => 1+2 = 3
#1,1,2,3 => 2+3 = 5
#1,1,2,3,5 => 3+5 = 8
#1,1,2,3,5,8 => 5+8 = 13
#....

n = 6
fz = ""

letzteZahl = 1
vorletzteZahl = 1
fz = str(letzteZahl)+","+str(vorletzteZahl)
fibonacci = 0
for i in range (1,n-1):
    fibonacci = vorletzteZahl + letzteZahl
    fz = fz + "," + str(fibonacci)
    vorletzteZahl = letzteZahl
    letzteZahl = fibonacci

print("fibonacci series for",n," = ",fz)
