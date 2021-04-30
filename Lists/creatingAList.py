# Creating a list
#
# To create a list, you use the square brackets and add elements into it accordingly.
# if you do not pass any elements inside the square brackets, you get an empty list as the output.

myList = [] # create empty list
print(myList)
# []
myList = [1, 2, 3, 'example', 3.14] # creating list with data
print(myList)
# [1, 2, 3]

# Adding Elements
#
# The append() function adds all the elements passed to it as a single element.
# The extend() function adds the elements one-by-one into the list.
# The insert() function adds the element passed to the index value and increase
# the size of the list too
myListAdd = [1, 2, 3]
print(myListAdd)
# [1, 2, 3]
myListAdd.append([555, 12]) #add as a single element
print(myListAdd)
# [1, 2, 3, [555, 12]]
myListAdd.extend([234, 'more_example']) #add as different elements
print(myListAdd)
# [1, 2, 3, [555, 12], 234, 'more_example']
myListAdd.insert(1, 'insert_example') #add elment i
print(myListAdd)
# [1, 'insert_example', 2, 3, [555, 12], 234, 'more_example']

# Deleting Elements
#
# To delete elements, use the 'del' keyword which is built-in into python but does not return
# anything back to us.
# To remove an element by its value, you use the remove() function
# if you want the element back, you use the pop() function which takes the index value.
myListDelete = [1, 2, 3, 'example', 3.14, 10]
del myListDelete[4] #delete element at index 5
print(myListDelete)
# [1, 2, 3, 'example', 10]
myListDelete.remove('example') #remove element with value
print(myListDelete)
# [1, 2, 3, 10]
a = myListDelete.pop(1) #pop element from list
print('Popped Element:', a, ' List remaining; ', myListDelete)
print(myListDelete)
# Popped Element: 2 List remaining; [1, 3, 10]
# [1, 3, 10]
myListDelete.clear() #empty the list
print(myListDelete)
# []

# Accessing Elements
# Accessing elements is the same as accessing String in Python. You pass the index values and
# hence can obtain the values as needed.
myListAccessing = [1, 2, 3, 'example', 3.132, 10, 30]
for element in myListAccessing: #access elements one by one
    print(element)
# output:
# 1
# 2
# 3
# example
# 3.132
# 10
# 30

print(myListAccessing) #access all elements
# [1, 2, 3, 'example', 3.132, 10, 30]
print(myListAccessing[3]) #access index 3 element
# example
print(myListAccessing[0:2]) #access elements from 0 to 1 and exclude 2
# [1,2]
print(myListAccessing[::-1]) #access elements in reverse
# [30, 10, 3.132, ‘example’, 3, 2, 1]
print(myListAccessing[2::]) #access elements from index 2

# Other functions
#
# You have several other functions that can be used when working with lists.
# The len() function returns to us the length of the list
# The index() function finds the index value of value passed where it has been encountered
# the first time.
# The count() function finds the count of the value passed to it
# The sorted() functions do the same thing, that is to sort the values of the list.
# The sorted() has a return type whereas the sort() modifies the original list.
myListOther = [1, 2, 3, 10, 30, 10]
print(len(myListOther)) #find length of list
# 6
print(myListOther.index(10)) #find index of element that occurs first
# 3
print(myListOther.count(10)) #find count of the element
# 2
print(sorted(myListOther)) #print sorted list but not change original
# [1, 2, 3, 10, 10, 30]
myListOther.sort(reverse=True) #sort original list
print(myListOther)
# [30, 10, 10, 3, 2, 1]