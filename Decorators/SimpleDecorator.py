def f(x):
    def g(y):
        print("Y is " + str(y))
        print("X is " + str(x))
        return y + x + 3
    return g


nf1 = f(1)
nf2 = f(4)

print(f(1))
print(nf1(0))
print(nf2(10))
