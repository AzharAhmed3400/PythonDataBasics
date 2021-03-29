#Changeable == mutable
"""List: ordered,  changable,  duplicates
   Tuple: ordered, unchangable, duplicates
   Set:  unordered, addable/removable, no duplicates
   Dictionary: unordered, changeable, no duplicates"""
L =[1,3,4,9,"name",3]
T = (1,3,4,9,"name",3)
S = {1,3,4,9,"name",3}
D = {23: "twothree", 'B': 43, 'C':'CCD'}

print("This is for list: " + str(L[1]))
print("This is for tuple: " + str(T[1]))
print("This is for set: " + str(3 in S))
print("This is for dict: " + D[23])
print()

#Indexing Tuples and Lists: similar to strings
print(L[1:3])
print(T[:3])
print(L[::-1])
print()

#List functions
L.append(9090)
print('New look L: ' + str(L))
print()
    #Add strings: it is mutable so it changes L directly
L2 = [3, 5, 2, 3]
print("Added successfully " + str(L + L2))
    #del
del L[3]
print("Deleted successfully")
    #Changes in list from equated result in change in original
    #Avoid this by using .copy() on list you wanted copied into a new one
L2 = L
L2[2] = "hello good sir"
print("L got changed" + str(L))
    #New list
L5 = [x**2 for x in range(10)]
print("A new list pulled up " + str(L5))
print()


#Tuples: can be added but original will not change
T2 = (3, 5, 2 ,1)
print("Original: " + str(T))
print("After addition: " + str(T + T2))
print()

#Set functions
    #.add(param): self -explanatory
    #.update({e, r, w, r}): add multiple items
print("Before: " + str(S))
S.update({5, 7, 6, 8})
print("Updated: " + str(S))
    #.remove(param): remove a specified elements in set. Not index as param but an actual element
S.remove("name")
print("Recently deleted:" + str(S))

#Dictionary functions
    #Can use .update(another Dict) as well as one below
D['checkers'] = 99999
print('New look: ' + str(D))
del D['C']
print("Recently deleted: " + str(D))
    #can place list, tuples, and other data structures in dictionary
D2 = {'A': L, 'B': T, 'C':S, 'D': D}
print(D2['B'])
    #Can even change values in there
D2['B'][3] = "I have been changed"
print(D2['B'][3])
