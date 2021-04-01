import numpy as np

#Type must be same for all elements in the numpy arrays
    #Can specify datatype of array in it
a = np.array([1,2,3,4,5], dtype='i')
b = np.array([1,6,3,4,9], dtype='f')
print(a)
print(type(a))
print("The type of a " + str(a.dtype))
print()

#numpy array dimensions: EACH DIMESNION MUST HAVE SAME NUMBER OF ELEMENTS OR ELSE THE DIMENSION IS ALWAYS 1
    #There must be [] marks to show that it is an array otherwise .ndim won't work
c = np.array([[1,2,3], [4,5,6]])
print("The dimensions of c: "+ str(c.ndim))
    #Can call certain elements using indexes. Must specify which array and which element based on dimesnions
print("The second number of the first array in the 2D array C is", c[0,1])
print("The overall shape of C is: " + str(c.shape))
print("Number of 1D arrays: " + str(c.shape[0]))
print("Number of elements in array: " + str(c.shape[1]))
print()

#np.arange(n): creates an array of n values starting from 0
    #also np.arange(start, end, step)
D = np.arange(25)
print("This is arange function:", D)
print()

#np.random.permutation(a): randomizes order of array a
print("Random array:", np.random.permutation(np.arange(10)))
print()

#np.random.randint(low, high): random int between the low and high(exclusive)
print("Random number between 10 and 100:", np.random.randint(10, 100))
print()

#np.random.rand(): returns array of size n with numbers between 0 and 1(exclusive)
we = np.random.rand(10)
print("Random array: ", we)
    #can specify matrices of list
print("Random specified matrix array", np.random.rand(2,3))
print()

#np.reshape(n, m): Can reshape array into different matrices with n rows and m columns
q = np.arange(10).reshape(2, 5)
print("The shape of q:",q.shape)
print()

#Numpy Slicing: similar to way you access substrings or sublists
print("Not in reverse:", np.arange(10))
print("In reverse:", np.arange(10)[::-1])
"""When a variable is equal to part of a numpy array, it refers to the memory location, 
    so changes made in the new variable happen in the original array. Avoid using .copy() after the
    equated part. Ex: J = G[0:10].copy()"""
G = np.arange(20)
print("Original:", G)
J = G[0:10]
print("Copy:", J)
J[0] = 333
print("Change in copy:", J)
print("Change in original:", G)
print()

#np.argwhere(arrayName == value): return 2D array of where the index of the value(use [0][0] at end to get only the number
print("Where is the value of 333 in array G:", np.argwhere(G == 333)[0][0])
print()

#numpyArray[n,:]: access the entire column n
Y = np.round(10*np.random.rand(5, 4))
print("The full array:", Y)
print("The second row:", Y[1,:])
print("Columns 3 and 4 from rows 1 and 2", Y[1:3, 2:4])
print("Transposed version of the whole array(reversed rows and columns; now 4 rows 5 columns)", Y.T)
print()

#Another way to index: a[index_array]: returns values at specific indexes within the array: you get a copy everytime
Tb = np.arange(40)
U = Tb[0, 3, 4]
print("Full array:", Tb)
print("This is some index values of Tb:", U)
print("Values less than 24 in the array:", Tb[Tb < 24])
"""1st: used in arrays; 2nd: used in comparing single objects
(&, and), (|, or), (~, not)"""
print()
