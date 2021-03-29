def printSuccess():
    """Can be used as comments"""
    print("The task is completed. Moving on to the next one")

def printMessage(msg):
    print(msg)

def myAdd(a, b):
    return a + b


v = 9
def varChange(v):
    """Can access global variables. Change is terminated once function finishes"""
    v = 7
    print(v)

print("The function prints ")
varChange(v)
print("The regular variable accessible gives us " + str(v))
print()


def add(*args):
    sum = 0
    for i in range(len(args)):
        sum+= args[i]
    return sum

def f(**c):
    """Dictionaries with function
    x is the key while c[x] is the value"""
    for x in c:
        print(x, c[x])
f(c1 = 4, c2 = 7, c3 = 9)
print()
