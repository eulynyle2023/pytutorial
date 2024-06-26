# list1 = ['Liviu', 'Asare', 'Appiah']

# print(list1)

# print(type(list1))

# print(id(list1))


# empty_list = ['a', 1, 0.5]
# empty_list1 = ['a']
# print(empty_list)

# print(type(empty_list))

# print(id(empty_list))
# print(id(empty_list1))


# empty_list = ['a', 1, 0.6]
# print(id(empty_list))

# empty_list = ['a', 1, 0.5, empty_list, [7,9,8, empty_list]]
# print(empty_list)

# print(id(empty_list))


# print(empty_list[-1][3][2])



# empty_list = ['b', 'r', 'e', 'a', 'd']
# print(id(empty_list))
# # # print(empty_list[-3:0])

# # index1 = 5

# # print(empty_list[:index1])




# # print(empty_list.index('d', 'e'))

# empty_list[0] = [1,2,3]

# print(empty_list)

# print(id(empty_list[0]))
# print(id(empty_list[1]))

# print(id(empty_list[0][1]))



num = [1,7,9,3,4,5,6,7, 8, 3, 4]

# print(num * 10)


# print(num[5] * 10)

# num.append([6,7,8])
# num.extend(['tytytyt', 0.9])

# num.insert(2,[6,7,8,'4545', 'dfgdfg'])

# num[2:2] = [6,7,8, 'thgfhjg']
# num[2:5] = [9, 7 , '7']
# num2 = [8,9,'fghfgh']
# num = num + [7,8,] + num2

# del num[:]

# # num.remove(7)
# num = [1,7,9,3,4,5,6,7, 8, 3, 4]
# # num.pop(5)
# # num.pop(9)
# # num.clear()
# # print(len(num))

# print(num.count(3))


# vowels = ['5', 'E', 'u', 'i', 'a', 'o' ]

# print(vowels)
# print(id(vowels))

# vowels.sort(reverse=True)

# # print(vowels)
# # print(id(vowels))

# # 
# vowels = sorted(vowels)

# print(vowels)
# print(id(vowels))


# vowels = sorted(vowels, reverse=True)

# print(vowels)
# print(id(vowels))


# OS = ['Windows', 'macOs', 'Linux', 'Android', [2,3,4]]
# OS.reverse()

# print(OS)

# reserved_list = OS[-1:][0]
# reserved_list.reverse()
# print(reserved_list)


# for every_name in OS[::-1]:

    
#     if type(every_name) == list:

#         for nest in every_name:
#             print(nest)

#     else: 
#         print(every_name)


# colors = ['red', 'blue', 'green', 'orange']

# red, blue, *green, orange = colors

# print(red)
# print(blue)
# print(green)
# print(orange)



# colors2 = colors


# colors.append('ice')
# colors2.append('mango')
# print(colors)
# print(id(colors))

# print(colors2)
# print(id(colors2))


# colors2 = colors.copy()


# colors.append('ice')

# print(colors)
# print(id(colors))

# print(colors2)
# print(id(colors2))


# colors2 = colors[:]


# colors.append('ice')
# colors2.append('mango')

# print(colors)
# print(id(colors))

# print(colors2)
# print(id(colors2))

import copy

colors = ['red', 'blue', 'green', 'orange' , [3,4,56,7]]

# print(id(colors[4]))
# newcolor = copy.copy(colors)

# colors.append('new')
# print(colors)
# print(id(colors))

# print(newcolor)
# print(id(newcolor))
# print(id(newcolor[4]))





# newcolor = copy.deepcopy(colors)

# colors.append('new')
# print(colors)

# print(id(colors))

# print(newcolor)
# print(id(newcolor))

# print(id(colors[4]))
# print(id(newcolor[4]))

append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
copy.copy(
    copy.deepcopy()
)