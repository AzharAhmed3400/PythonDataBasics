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
c = np.array([1,2,3], [4,5,6])
print("The dimensions of c "+ c.ndim)
    #Can call certain elements using indexes. Must specify which array and which element based on dimesnions
print("The second number of the first array in the 2D array C is", c[0,1])
print("The overall shape of C is " + str(c.shape))
print("Number of 2d arrays " + str(c[0].shape))
print("Number of elements in array " + str(c[1].shape))