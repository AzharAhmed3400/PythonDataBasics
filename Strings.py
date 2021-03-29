#Don't combine 'this' with "this"

#Commas autospace it
print("Hi", 89, "I could be better you", 2, "legged freak")

#Have to change type to print diff things
print()
print("She likes " + str(5) + " guys")

print()
#Multiline
r = """Bya is a big gay
He likes men
He is a gegg
And he sucks"""
print(r)
print()

#Indexing & Slicing: s[start, end, step]
s = "YousuckODboi"
print(s[3:8])
print(s[-6: -1])
    #Intervals
print(s[0:12:2])
    #reverse a string
print(s[::-1])
print()

#String functions
    #.strip(): replaces unecessary whitespace at end
    #.lower() & .upper(): self explanatory
    #.replace("". ""): replace all instances of first param with the second param
    #.split(""): splits thr string and returns a List

#Use in and not in to check if part is in a string
print("abc" in "gsyssbsabaabc")
print()

#Backslahes to use quotes around words or use " " embedded within ' '
print("Hi I'm \"cool\"")
print('I heard you "love" him')
print()
#New line
print("This is a \nnew line")
print()
#A tab
print("This is \ttrippy")
#print \n without going to new line
print(r"c:\name\dream")