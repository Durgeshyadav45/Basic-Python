# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Durgesh'
Dict[2] = 'Kumar'
Dict[3] = 'Yadav'
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print(Dict)


# Deleting Elements using del Keyword
# Creating a Dictionary
Dict = {1: 'Durgesh', 'name': 'Kumar', 3: 'Yadav'}
print("Dictionary =")
print(Dict)
del (Dict[1])
print(Dict)