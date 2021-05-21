# A ='1934567'
# print(A[0::2])

# s = "123"
# print(s.replace("12", "ab"))

# Traversing to the 0th element of the 2nd element of the Tuple
# Tuple's 2nd element is list & List's 0th element is 4
# A=((1),[2,3],[4])
# print(A[2][0])

# x = 'A,B,C,D'
# print(x.split(','))
#
# txt = "apple#banana#cherry#orange"
#
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
#
# print(x)

# Dictionary Methods
# release_year_dict = { "The Bodyguard":"1992", "Saturday Night Fever":"1977"}
# print(release_year_dict.keys())


# for i in range(5):
#     for j in range(4-i,0, -1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print('*', end= " ")
#print()

#
# for i in range(5):
#     for j in range(i):
#         print(' ', end=" ")
#     for j in range(5-i,0,-1):
#         print('*', end=" ")
#     print()

#Zip() Function in Python which merges 2 or more iterables into elemnts of tuples & returns an iterable object

# items = ['bananas', 'matteresses', 'dog kennels', 'machine', 'cheeses']
# weights = [15, 34, 42, 120, 5]

# print(zip(items, weights))
# print(list(zip(items, weights)))
# for courier in zip(items, weights):
#     print(courier[0], courier[1])

# for item, weight in zip(items, weights):
#     print(item, weight)

# manifest = [('bananas',15), ('matteresses', 34), ('dog kennels',42), ('machine',120) , ('cheeses',5)]
# items, weights = zip(*manifest)
# print(items)
# print(weights)

# iterating through a list with list indices

# items = ['bananas', 'matteresses', 'dog kennels', 'machine', 'cheeses']
#
# for i, item in zip(range(len(items)), items):
#     print(i, item)

# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = []
# write your for loop here


# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!
#
#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/
#
# <3, Juno
# """
#
#
# print(snake_string * how_many_snakes)

# items2 =[]
# items = ['bananas', 'matteresses', 'dog kennels', 'machine', 'cheeses']
# for item in items:
#     items2.append(item.strip(',')[0])
#
# print(items2)

# Generator
# def my_range(x):
#     i = 0
#     while i < x:
#         yield i
#         i += 1
# print(my_range(4))
# for num in  my_range(4):
#     print(num)


# sort() method in lists:-

# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)

# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort(reverse= True)
# print(cars)

# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort(key=) # key = is actually a function which defines the sorting order
# print(cars)

# print('\\t')

try:
    value = int(input(''))
except: Type error
     print('This is not the intended type')



