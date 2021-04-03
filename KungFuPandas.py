import pandas as pd
#Indexes are default 0, 1, 2,3 ..
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a','b','c','d'])
print("Data vals:", data.values)
print("Data indexes: ", data.index)
print()

#Can turn dictionaries into Panda series'
the_dict = {'A': 67,'U':87,'R':9876}
print("The printed dictionary", the_dict)
pandad = pd.Series(the_dict)
print("The dictionary got pandad:", pandad)

#DataFrame: usually used for 2D arrays or tables
marks = {'A': 21, 'U': 89, 'R': 56}
oi = pd.Series(marks)
rs = pd.DataFrame({'P': pandad, 'O': oi})
print(rs)
print(rs.T)
    #rs.values[]
print("The values are in 2D form that can be referenced using indexes", rs.values)
print('The columns', rs.columns)
rs['T'] = 100*(rs['P'] -20)
print('Added columns\n', rs)
    #delete columns using del rs['P']
#Index: rs[rs['P'] > 70]--> would lead to deleting rows within 'p' with value less than 70
print()

#Pandas NaN
    #If they have diff key values, you will see a Nan
H = pd.DataFrame([{'a': 67, 'b': 45}, {'b': 99, 'c': 89}])
print(H)
print('Fixed it\n', H.fillna(0))
print()

#Pandas Indexing
date = pd.Series(['a', 'b', 'c'] , index=[1,3,5])
print('Explicit (defined indexes)\n', date[1])
print('Implicit (regular indexing instead of user defining: default fro slicing)\n', date[1:3])
print('Explicit indeces:\n', date.loc[1:3])
print('Implicit Indeces:\n', date.iloc[1:3])
'''Can be used in dataFrame'''
print('Implicit indexing in dataframe\n', H.iloc[1,:])