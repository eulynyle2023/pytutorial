
# # Empty tuple
# my_tuple = () 
# print(my_tuple)

# # Tuple having integers
# my_tuple = (1, 2, 3)
# print(my_tuple)

# # tuple with mixed datatypes
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# # nested tuple

# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)


# # tuple packing.
# my_tuple = 3, 4.6, "dog"
# print(my_tuple)


# # tuple unpacking is also possible

# a, b, c = my_tuple

# print(a)      # 3
# print(b)      # 4.6
# print(c)      # dog
# # print(e)



# A tuple with one element


# my_tuple = ("hello",)
# print(type(my_tuple)) 



# my_tuple = "hello"
# print(type(my_tuple))  

# numbers = (3)
# print(type(numbers))


numbers = r'(3,6, ,)'
print(type(numbers))



# # Modifying a tuple

rgb = ('red', 'green', 'blue')

# rgb[0] = 'yellow'

# print(rgb)


# my_tuple = (4, 2, 3, [6, 5])
# my_tuple[1] = 9


# # But, if the element is itself a mutable data type like a list, its nested items can be changed.

my_tuple = (4, 2, 3, [6, 5])
# my_tuple[3][0:] = [9,9]
# print(my_tuple)


# # Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')


print(my_tuple)


# # Concatenation

# print((1, 2, 3) + (4, 5, 6))

# print(("Repeat",) * 3)


# # Accessing a tuple

my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   
print(my_tuple[5])   




# # nested tuple
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# # # nested index
# print(n_tuple[0][3])       
# print(n_tuple[1][1])       

# # # IndexError: list index out of range
# print(my_tuple[6])



# # Index must be an integer
# # TypeError: list indices must be integers, not float
# my_tuple[2.0]




# # Negative indexing for accessing tuple elements
# my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
# print(my_tuple[-1])
# print(my_tuple[-6])


# # 3.	Slicing

# my_tuple = ('p','r','o','g','r','a','m','i','z')


# print(my_tuple[1:4])

# print(my_tuple[:-7])


# print(my_tuple[7:])


# print(my_tuple[:])




# # Deleting a tuple

# # Deleting tuples
# my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# # del my_tuple[3]

# # # # Can delete an entire tuple
# del my_tuple

# # # NameError: name 'my_tuple' is not defined
# print(my_tuple)

# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# del n_tuple[0][0]

# print(n_tuple)

# # Couting a tuple

# my_tuple = ('a', 'p', 'p', 'l', 'e',)

# print(my_tuple.count('p')) 


# print(len(my_tuple))




# # print(id(n_tuple))
# # print(id(n_tuple[0]))

# # print(id(n_tuple[1]))
# # print(id(n_tuple[2]))

# # print(id(n_tuple[2][1]))
# # print(id(n_tuple[1][1]))


# # # Index

# # my_tuple = ("mouse", 'l',[8, 4, 6], (1, 4, 3))
# # print(my_tuple.index('l'))


# # # Tuple membership

# # # Membership test in tuple
# # my_tuple = ('a', 'p', 'p', 'l', 'e',)

# # # # In operation
# # print('a' in my_tuple)
# # print('b' in my_tuple)

# # # # Not in operation
# # print('g' not in 'there')

# # # Iterating through a tuple

# # # Using a for loop to iterate through a tuple
# for i in ('John', 'Kate'):
#     print("Hello", i)



# print({

# 'name': 'utwaduauwqe86878',
# 'age': 57,
# 'nationality': 'english'

# })


# dict_name = {

# 'name': 'utwaduauwqe86878',
# 'age': 57,
# 'nationality': 'english'

# }

# print(dict_name)
# print(id(dict_name))
# print(id({

# 'name': 'utwaduauwqe86878',
# 'age': 57,
# 'nationality': 'english'

# }))


# dict_empty = {}
# print(dict_empty)

# my_tuple = ((int(6),1), (0.9,6), (6, 8), ('l', 9), ('e',0))
# new = dict(my_tuple)
# print(new)


# print(new[6])


dict1 = {
    'name' : 'sdfdsf',
    'age': 67
}


print(dict1)
dict1['name'] = 45

print(dict1)