# factorial.py

# 1! = 1
# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4

n = int(input("factorial: n = "))
f = 1
for i in range (1, n+1):
    f = f * i

print(n,"! = ", f, sep="")