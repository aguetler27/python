# factorial recursive

def fact(n):
    print("calc fact for", n)
    if (n == 1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("n! von: "))
print(fact(n))

