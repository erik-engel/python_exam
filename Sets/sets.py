#sets contain unique values with no index
numbers_set_one = {5, 5, 10, 1, 0}
numbers_set_two = set({5,6, 7, 8, 9})
print (numbers_set_one)
print (numbers_set_two)
#output : {0, 1, 10, 5}
#output : {5, 6, 7, 8, 9}

#adding new element to the set
numbers_set_one.add(6)
print (numbers_set_one)
#output : {0, 1, 5, 6, 10}

#removing the specified element
numbers_set_one.remove(6)
print (numbers_set_one)
numbers_set_one.discard(6)
#output : {0, 1, 5, 10}

#union return a set containing the union of sets
numbers_set_one.union(numbers_set_two)
#or
numbers_set_one | numbers_set_two
#output : {0, 1, 5, 6, 7, 8, 9, 10}

#intersection returns a set, that is the intersection of two sets
numbers_set_one.intersection(numbers_set_two)
#or
numbers_set_one & numbers_set_two
#output : {5}

#difference returns a set containing the difference between two or more sets
numbers_set_one.difference(numbers_set_two)
#or
numbers_set_one - numbers_set_two
#output : {0, 1, 10}

#symmetric_difference returns a set with the symmetric differences of two sets
numbers_set_one.symmetric_difference(numbers_set_two)
#or
numbers_set_one ^ numbers_set_two
#output : {0, 1, 6, 7, 8, 9, 10}

#isdisjoint returns false if two sets have elements in common
numbers_set_one.isdisjoint(numbers_set_two)
#output : false

#copy returns a shallow copy of the set
numbers_set_three = numbers_set_one
#output : {0, 1, 10, 5}
numbers_set_one.discard(5)
print(numbers_set_one)
print(numbers_set_three)
#output : {0, 1, 10}
#output : {0, 1, 10}
numbers_set_three = numbers_set_one.copy()
numbers_set_three.add(5)
print(numbers_set_one)
print(numbers_set_three)
#output : {0, 1, 10}
#output : {0, 1, 10, 5}

#clear()	#Removes all the elements from the set
numbers_set_one.clear()
#output : set()


##difference_update()	#Removes the items in this set that are also included in another, specified set
##discard()	#Remove the specified item
##intersection()	#Returns a set, that is the intersection of two other sets
##intersection_update()	#Removes the items in this set that are not present in other, specified set(s)
##isdisjoint()	#Returns whether two sets have a intersection or not
##issubset()	#Returns whether another set contains this set or not
##issuperset()	#Returns whether this set contains another set or not
##pop()	#Removes an element from the set
##remove()	#Removes the specified element
##symmetric_difference()	#Returns a set with the symmetric differences of two sets
##symmetric_difference_update()	#inserts the symmetric differences from this set and another
##union()	#Return a set containing the union of sets
##update()	#Update the set with the union of this set and others
