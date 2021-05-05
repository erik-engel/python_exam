# Creating a Dictionary
#
# Dictionaries can be created using the flower braces or using the dict() function.
# You need to add the key-value pairs whenever you work with dictionaries.

myDict = {} #empty dictionary
print(myDict)
# {}
myDict  = {1: 'Python', 2: 'Java'}
print(myDict)
# {1: 'Python', 2: 'Java'}

# Changing and Adding key, value pairs
# To cange the values of the dictionary, you need to do that using the keys. So, you firstly
# access the key and then change the value accordingly. To add values, you simply just add
# another key-value
myDict  = {'first': 'Python', 'second': 'Java'}
print(myDict)
# {'first': 'Python', 'second': 'Java'}
myDict['second'] = 'C++' #changing element
print(myDict)
# {'first': 'Python', 'second': 'C++'}
myDict['third'] = 'Ruby' #adding key-value pair
print(myDict)
# {'first': 'Python', 'second': 'C++', 'third': 'Ruby'}

# Deleting key, value pairs
# To delete the values, you use the pop() function which returns the value that has been deleted.
myDict = {'first': 'Python', 'second': 'Java', 'third': 'Ruby'}
a = myDict.pop('third') #pop element
print('Value: ', a)
# Value: Ruby
print('Dictionary:', myDict)
# {'first': 'Python', 'second': 'Java'}
b = myDict.popitem() #pop the key-value pair
print('Key, value pair:', b)
# Key, value pair: ('second', 'Java'
print('Dictionary', myDict)
# Dictionary {'first': 'Python'}
myDict.clear() #empty dictionary
print(myDict)
# {}

# Accessing Elements
# You can access elements using the keys only. You can use either the get() function or just pass
# the key values and you will be retrieving the values.
myDict = {'first': 'Python', 'second': 'Java'}
print(myDict['first']) #access elements using keys
# Python
print(myDict.get('second'))
# Java

# Other functions
# you have different functions which return to us the keys or the values of the key-value pair
# accordingly to the keys(), values(), items() functions accordingly.
myDict = {'first': 'Python', 'second': 'Java', 'third': 'Ruby'}
print(myDict.keys()) #get keys
# dict_keys(['first', 'second', 'third'])
print(myDict.values()) #get values
# dict_values(['Python', 'Java', 'Ruby'])
print(myDict.items()) #get key-value pairs
# dict_items([('first', 'Python'), ('second', 'Java'), ('third', 'Ruby')])
print(myDict.get('first'))
# Python