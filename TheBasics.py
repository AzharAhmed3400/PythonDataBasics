#Some unfamiliar operands: % mod: means remainder; **: exponent
# //: Floor division ex. instead of 10//3 = 3.333 it is 3 (truncated)

#Types
    #Some types include int, String, float, complex, etc.
p = 34
print(type(p))
print()

#Common functions:
#Round(x, y)
r = 3.323232
print("Rounded to int (default): " + str(round(r)))
print("Rounded to three decimal places (specified) " + str(round(r, 3)))
print()

#Divmod(x, y): outputs quotient and remainder (int that order)
e = divmod(27, 5)
print(e)
    #Sidenote: tuple can be referenced as a list
print("First element in tuple: " + str(e[0]))
print()

#isInstance(): returns true if an instance of that type
print("Is 4 an instance of int?: " + str(isinstance(4, int)))
print("Is 3.45 a float OR an integer?: " + str(isinstance(3.45, (float, int))))
print()

#pow(x,y,z): x raised to power y and the product is remainded by z
print("3 to the power of 2: " + str(pow(3, 2)))
print("5 to the power of 6 modded by 4: " + str(pow(5,6,4)))

#Input(): take value from user
a = input("Whats your name?")
print("You said your name was: " + a)
    #Can cast to a different type
q = int(input("How many fingers do you have?"))
print("You said you had " + str(q) + " fingers")
print()

#IF STATEMENTS
d = int(input("Whats your favorite number"))
if(d > 89):
    print("Thats a wack number")
elif(d < 89 & d > 45):
    print("Thats aii")
else:
    print("Not bad but could be worse")
print()
    #Shorthand if of above
t = 99
print("meh") if t < 45 else print("aii") if t > 45 & t>89 else print("Wack")
print()

#while loops
n = 3
i = 0
while(i < n):
    print("Lolol")
    i+=1
    #can use "pass" or "continue" to do nothing and proceed
print()

#For loops
L =[]
for i in range(10):
    L.append(i)
else:
    #Else only goes after the for loops iterations are done
    print(L)

