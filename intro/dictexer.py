


# dict1 = {}

# dict1 = dict()

# dict1 = {1: 'apple', 2: 'mango'}


# dict1 = {1: 'apple', 'key1': 'mango'}

# dict1 = {{1:1}: 'apple', 'key1': 'mango'}

# list1 = [(1,3,8), (2,3, 7)]

# dict1 = {}

# for i in list1:

#         key,*value = i
#         print(key,value)
#         dict1[key] = value
       

# print(type(dict1))
# print(dict1)




# person = {

#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 35,
#     'fav_colours': 'blue',
#     'active': True
# }

# print( (person))


# vowels = {'a', 'e', 'i', 'o', 'u'}
# # value = {'vowel1', 'vowel2', 'vowel3', 'vowel4', 'vowel5'}
# value = [1]
# dict_keys = dict.fromkeys(vowels, value)

# print(dict_keys)



# marks = {}.fromkeys(['math', 'science', 'english'], [0,8])

# print(marks)



# vowels = {'a', 'e', 'i', 'o', 'u'}
# # value = {'vowel1', 'vowel2', 'vowel3', 'vowel4', 'vowel5'}
# value = [1]
# dict_keys = dict.fromkeys(vowels, value)

# print(dict_keys)

# value.append(2)

# print(dict_keys)




person = {

    'first_name': 'John',
    'last_name': 'Doe',
    'age': 35,
    'fav_colours': 'blue',
    'active': True
}

# print( (person))


# print(person['first_name'])
# print(person['active'])
# # print(person[0])


# print(person.get('age'))

# print(person.get(0, 'This is flagged'))


# print(person.items())

# print(person.keys)

# print(person.keys())

# print(person.values)

# print(person.values())


# person = {

#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 35,
#     'fav_colours': 'blue',
#     'active': True
# }

# person['active'] = None
# # person['salary'] = 35000
# # del person['active']
# # print(person)
# # print(person.pop('age'))
# # print(person.pop('first_name', 'last_name'))
# # print(person.pop('guava'))
# # print(person.popitem())
# # person.clear()

# # del person



# salary = person.setdefault('salary', '350000')

# print(person)
# print(salary)


d = {1: 'one', 2:'two'}
d1 = {2: "two", 3:"three"}

d.update(d1)

print(d)
print(d1)