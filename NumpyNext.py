import numpy as np

#Broadcasting: Add values to the entire array
A = np.array([1,2,3,4])
print("Array before broadcasting:", A)
A = A + 5
print("Array after broadcasting:", A)

#Important functions
    #.hstack(n, m): stack arrays n and m horizonatlly
    #above applies to .vstack(n,m)
q = np.round(10*np.random.rand(2,2))
print(q)
w = np.round(10* np.random.rand(2, 3))
print(w)
print("They are stacked:", np.hstack((q,w)))

    #.sort(): sorts
print()
R = np.random.permutation(np.arange(10))
print("Random:", R)
print("Now sorted:",np.sort(R))
print()

#Seed: ufuncs
T = np.random.rand(100000)
    #.sum() is faster than regular python sum(B). Can only be used for numpy
print("A sum:",T.sum())
