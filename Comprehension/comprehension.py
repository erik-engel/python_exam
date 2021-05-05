#List comprehension
alphabet = [chr(i) for i in range(65, 91)]
print (alphabet)
#output : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Advanced list comprehension with tuples
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
soled_out = [('Black', 'm'), ('White', 's')]
res = [(x, y) for x in colors for y in sizes if not (x,y) in soled_out]
print (res)
#output : [('Black', 's'), ('Black', 'l'), ('Black', 'xl'), ('White', 'm'),
#('White', 'l'), ('White', 'xl')]

#Set comprehension
print({ x * x for x in range(-9, 10) })
#output : {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}

#dict comprehension
print({ x: x * x for x in range(5) })
#output : {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}

#tuple comprehension (using list comprehension and then tuple it)
print(tuple([(x , y) for x in colors for y in sizes]))
#output : (('Black', 's'), ('Black', 'm'), ('Black', 'l'), ('Black', 'xl'),
#('White', 's'), ('White', 'm'), ('White', 'l'), ('White', 'xl'))
