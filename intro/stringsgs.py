# # # You can assign the value of python to different variable all in one same line, to make your code more compact: 



# # a = b = c = 300



# # print("this is assignemtn", a, b, c)
# # print(type(a), type(b), type(c))

# # print(id(a), id(b), id(c))

# # a, b, c = 300, 300, 300

# # print(a, b, c)
# # print(type(a), type(b), type(c))


# # Python is a Dynamic typing language  : Where variable change in its lifetime. You can change the variable data type:


# Thing = "helo"

# print(type(Thing))
# print(id(Thing))

# # Thing = 1212

# # print(type(Thing))
# # print(id(Thing))


# # You can delete a variable using the del keyword :

# # del Thing

# # del a, b, c


# # print(Thing)
# # print(id(Thing))
# # print(a, b, c)

# Thins1 = 0
# del Thins1

# print(Thins1)
# print(id(0))

# # # Variables besides their data types can be further classified into two other main types : global and local variables. 
# # a  = 10 

# # def add(a):
	
# # 	global b = 1
# # 	c = a + b
# # 	print(c)
	
    
# # add(a)
# # print(b)
	


# # def multiply(a):
# # 		c = a*b
# # 		print(c)

# # # a  = 10 



# # def add(a):
	
# #     global br
# #     br = 1
# #     c = a + br
# #     print(c)
	



# # #     def multiply(a):
# # #          c = a*b
# # #          print(c)

# # # add(5)
# # # print(br)








""
''

# #String Escapes

# # print('this musn\'t happen')

# # print(("this musn't happen"))
           
# print(('this musn\'t happen'))


# print(a="this is a text")
# # print(a)
# a = "thi sis text"
# print(a)




# # Multi-line strings can be handled in three ways, each line separated by a \  the use of triple quotes.  Add parentheses to make the long line

# text = "This is is a string\
# this is also a strng \
# tis is also a string"

# print(text)


# text2 = """This is is a string\      
# this is also a strng 
#       tis is also a string"""

# print(__doc__.isalnum)


# print(text2)

#This program adds two numbers





# #string parenthesis

# text3 = ("%f hello," "or %d, " " or %s,"
#         %( 435345345.7,3, "hola"))

# print(text3)
# g  ='\\'
# print('The numbeer is %d', g)
# print(f'The number is {g}')


# a = f"this is a text.  {g}\ This should be on a new line"

# g = '\x07'

# a = f"this is a text. {g} This should be on a new line \7 this is on the third line"
# print('\n, This is an event')

# a = r"this musn't happen"

# print(a)

# a = 'hello' + 'there'
# a = a + 'this'



# b = 'l'
# print(a)

# # a[2] = 9

# print(a[1])

# print(a)



# x = -1

# 0
# print(len(a))
# for  count in a :
    
#     x+=1
   
#     print(f'{x}', id(count))
#     # print(x)

# print(id(b))

# # length of a string = n
# # final position : n-1

# d = 76777
# # print('This is d[0]',d[0])

# for count in d:
#     print(count)




#new line : \n



#ascii bell : \x07



#string concatenation

# A = 'This is cherry'
# B = 'Awesome'
# D = ' '* 100
# C = A + D+ B

# print(C)


# print(f'{A[0:8]} {B} {A[8:]}')




# A = '1'
# B = '2'
# D = 4
# C = A+B
# print(C)

# print('My age is '+C)
# print('My age is '+1+D)


A = 'Temperance'
# # 0 - n
# # n-1
# print(A)

# b = 0
# c = 5

# print(A[0:8])
# print(A[b:c+1])
A = 'Temperance'
# print(A[18:18])

# print(A[-8])
# A = r'Tempera \'\'nce'
# print(A[-2])
# print(A[-5])
# print(A[-5:-2])
# B = '>>>'
# print(len(A))
# # print(A+B)


# A = 'Temperance'
# B = 0 
# C = 9
# print(A[0:4])
# print(A[0:-4])
# print(A[-9:-1])
# print(A[0:])
# print(A[-9:])
# print(A[:-9])
# # print(A['t':'c'])
# print(A[B:C])

# # print(A[1: 2.5])

# A[-8] = 9
# del(A[9])

# A = 'temperance ' 
# # print(A + 'abc')
# # print(A)

# print('c' in A)
# print(A[9] in A)
# print(' ' in A)


# B = enumerate(A)
# B = list(enumerate(A))
# print(B)
# print(list(B))
# print(B)

# A = 'temperance'
# print(type(A))
# print(str(A))


# A = 233453
# print(type(A))
# print(id(A))
# A = str(233453)
# A = str(A)
# print(id(A))
# print(str(A))
# print(type(A))

# A = ('temperance').upper()
# print(A)
# print(A)

# A = ('Banana').count('an')
# print(A)
# print(A)


# A = '       Bana                na      '
# print(len(A))


# A = A.lstrip()
# print(len(A))
# print(A)

# A = A.rstrip()
# print(len(A))
# print(A)

# A = '           '

# A = 'Banana'
# print(len(A))
# print(A.isalpha())
# print(A.isdigit())
# print(A.isspace())
# print(A.startswith('b'))
# print(A.endswith('a'))
# print(A.find('B'))

# print(id(A))
# A = A.replace('B', 'C')
# print(id(A))


A = 'this is curry'
# A = 12123123123
# A.split('')

# B = A.join({'a':'b'})

# C = A.capitalize()
# C = A.upper()
# C = A.title()

# A = A.isalnum()


# B = 15000
# B = B.isnumeric()

# print(B)

A = str(hex(345345345))
print(A)
B = A.isdecimal()

print(B)
# B = ascii(A)
# print(ord('T'))

# 84 69
# 116 101

c = 'Ben'
c =45456456.78

# C = 'Welcome back %s',c
print("Total score for %f " % c)
# print('Welcome back %d', 4 )

c = 'Asare'
d = 'liviu'
e = 'Ben'


data = {'name': 'asare', 'date': '12/09/2024'}
# print('{c} has an apple, {e} has a banana, {d} has a strawberry'.format(c = 'Ben', d='Appiah', e='Asare'))

# print('{data[name]} has an apple'.format(data = data))
print('{name} has an apple on {date}'.format(**data))







# print('{:5d}'.format(12))


# print('{:2d}'.format(1234))

# print('{:8.3f}'.format(12.3467))


# print('{:05d}'.format(12))

# print('{:08.3f}'.format(12.34))


# print('{:+f} {:+f}'.format(12.34, -12.67))

# print('{:-f} {:-f}'.format(12.34, -12.67))

# print('{: f} {: f}'.format(12.34, -12.67))


# print('{:5d}'.format(12))

# print('{:^10.3f}'.format(12.2346))

# print('{:<05d}'.format(12))

# print('{:=8.3f}'.format(-12.3467))

# print('{:5}'.format("cat"))

# print('{:>5}'.format("cat"))

# print('{:^5}'.format("cat"))

# print('{:*^5}'.format("cat"))

# print('{:*>5}'.format("cat"))


# print('{:.3}'.format("caterpillar"))
# print('{:5.3}'.format("caterpillar"))
# print('{:^5.3}'.format("caterpillar"))


# txt = "the temp is {:=8} degree celcius"

# print(txt.format(-5))

# print('{:,}'.format(19999999))

# print('{:b}'.format(19999999))

# # print('{:c}'.format('1'))

# print('{:e}'.format(1))

# print('{:E}'.format(1))

# print('{:f}'.format(1))

# print('{:F}'.format(1))


# print('{:g}'.format(1.8899099999999))


# print('{:G}'.format(1.8899099999999))

# print('{:o}'.format(1))


# print('{:x}'.format(1))

# print('{:n}'.format(1))

# print('{:"(None)}'.format(1))
# # print('{:x}'.format(12))
# # print('{:X}'.format(12))
# # print('{:n}'.format(12))
# # print('{:%}'.format(12))


# name= 'june'

# print(f'hello {name}')


# message = (
#         f"hello {name}" 
#         "this is a multilined string"\
#         f"have a good day{name}")

# print(message)


# number = 10
# print(f"{number}+ 1 = {number+1}")


# def func():

#     return 4


# print(f"func() = {func()}")

# print(type(10))

# print(type(5.0))

# print(type(5 + 3j))

# c =  5.1 + 3.1j

# d =  3.1j

# print(c + d)# # # You can assign the value of python to different variable all in one same line, to make your code more compact: 



# # a = b = c = 300



# # print("this is assignemtn", a, b, c)
# # print(type(a), type(b), type(c))

# # print(id(a), id(b), id(c))

# # a, b, c = 300, 300, 300

# # print(a, b, c)
# # print(type(a), type(b), type(c))


# # Python is a Dynamic typing language  : Where variable change in its lifetime. You can change the variable data type:


# Thing = "helo"

# print(type(Thing))
# print(id(Thing))

# # Thing = 1212

# # print(type(Thing))
# # print(id(Thing))


# # You can delete a variable using the del keyword :

# # del Thing

# # del a, b, c


# # print(Thing)
# # print(id(Thing))
# # print(a, b, c)

# Thins1 = 0
# del Thins1

# print(Thins1)
# print(id(0))

# # # Variables besides their data types can be further classified into two other main types : global and local variables. 
# # a  = 10 

# # def add(a):
	
# # 	global b = 1
# # 	c = a + b
# # 	print(c)
	
    
# # add(a)
# # print(b)
	


# # def multiply(a):
# # 		c = a*b
# # 		print(c)

# # # a  = 10 



# # def add(a):
	
# #     global br
# #     br = 1
# #     c = a + br
# #     print(c)
	



# # #     def multiply(a):
# # #          c = a*b
# # #          print(c)

# # # add(5)
# # # print(br)








""
''

# #String Escapes

# # print('this musn\'t happen')

# # print(("this musn't happen"))
           
# print(('this musn\'t happen'))


# print(a="this is a text")
# # print(a)
# a = "thi sis text"
# print(a)




# # Multi-line strings can be handled in three ways, each line separated by a \  the use of triple quotes.  Add parentheses to make the long line

# text = "This is is a string\
# this is also a strng \
# tis is also a string"

# print(text)


# text2 = """This is is a string\      
# this is also a strng 
#       tis is also a string"""

# print(__doc__.isalnum)


# print(text2)

#This program adds two numbers





# #string parenthesis

# text3 = ("%f hello," "or %d, " " or %s,"
#         %( 435345345.7,3, "hola"))

# print(text3)
# g  ='\\'
# print('The numbeer is %d', g)
# print(f'The number is {g}')


# a = f"this is a text.  {g}\ This should be on a new line"

# g = '\x07'

# a = f"this is a text. {g} This should be on a new line \7 this is on the third line"
# print('\n, This is an event')

# a = r"this musn't happen"

# print(a)

# a = 'hello' + 'there'
# a = a + 'this'



# b = 'l'
# print(a)

# # a[2] = 9

# print(a[1])

# print(a)



# x = -1

# 0
# print(len(a))
# for  count in a :
    
#     x+=1
   
#     print(f'{x}', id(count))
#     # print(x)

# print(id(b))

# # length of a string = n
# # final position : n-1

# d = 76777
# # print('This is d[0]',d[0])

# for count in d:
#     print(count)




#new line : \n



#ascii bell : \x07



#string concatenation

# A = 'This is cherry'
# B = 'Awesome'
# D = ' '* 100
# C = A + D+ B

# print(C)


# print(f'{A[0:8]} {B} {A[8:]}')




# A = '1'
# B = '2'
# D = 4
# C = A+B
# print(C)

# print('My age is '+C)
# print('My age is '+1+D)


A = 'Temperance'
# # 0 - n
# # n-1
# print(A)

# b = 0
# c = 5

# print(A[0:8])
# print(A[b:c+1])
A = 'Temperance'
# print(A[18:18])

# print(A[-8])
# A = r'Tempera \'\'nce'
# print(A[-2])
# print(A[-5])
# print(A[-5:-2])
# B = '>>>'
# print(len(A))
# # print(A+B)


# A = 'Temperance'
# B = 0 
# C = 9
# print(A[0:4])
# print(A[0:-4])
# print(A[-9:-1])
# print(A[0:])
# print(A[-9:])
# print(A[:-9])
# # print(A['t':'c'])
# print(A[B:C])

# # print(A[1: 2.5])

# A[-8] = 9

# print(A)







# print('{:5d}'.format(12))


# print('{:2d}'.format(1234))

# print('{:8.3f}'.format(12.3467))


# print('{:05d}'.format(12))

# print('{:08.3f}'.format(12.34))


# print('{:+f} {:+f}'.format(12.34, -12.67))

# print('{:-f} {:-f}'.format(12.34, -12.67))

# print('{: f} {: f}'.format(12.34, -12.67))


# print('{:5d}'.format(12))

# print('{:^10.3f}'.format(12.2346))

# print('{:<05d}'.format(12))

# print('{:=8.3f}'.format(-12.3467))

# print('{:5}'.format("cat"))

# print('{:>5}'.format("cat"))

# print('{:^5}'.format("cat"))

# print('{:*^5}'.format("cat"))

# print('{:*>5}'.format("cat"))


# print('{:.3}'.format("caterpillar"))
# print('{:5.3}'.format("caterpillar"))
# print('{:^5.3}'.format("caterpillar"))


# txt = "the temp is {:=8} degree celcius"

# print(txt.format(-5))

# print('{:,}'.format(19999999))

# print('{:b}'.format(19999999))

# # print('{:c}'.format('1'))

# print('{:e}'.format(1))

# print('{:E}'.format(1))

# print('{:f}'.format(1))

# print('{:F}'.format(1))


# print('{:g}'.format(1.8899099999999))


# print('{:G}'.format(1.8899099999999))

# print('{:o}'.format(1))


# print('{:x}'.format(1))

# print('{:n}'.format(1))

# print('{:"(None)}'.format(1))
# # print('{:x}'.format(12))
# # print('{:X}'.format(12))
# # print('{:n}'.format(12))
# # print('{:%}'.format(12))


# name= 'june'

# print(f'hello {name}')


# message = (
#         f"hello {name}" 
#         "this is a multilined string"\
#         f"have a good day{name}")

# print(message)


# number = 10
# print(f"{number}+ 1 = {number+1}")


# def func():

#     return 4


# print(f"func() = {func()}")

# print(type(10))

# print(type(5.0))

# print(type(5 + 3j))

# c =  5.1 + 3.1j

# d =  3.1j

# print(c + d)

# print(isinstance(c, complex))

# print(isinstance(5j, complex))

# x = 15
# y = 4


# print('x + y =',x+y)

# print('x - y =',x-y)

# print('x * y =',x*y)


# print('x / y =',x/y)

# print('x // y =',x//y)


# print('x ** y =',x**y)

# print('x mod y =',x%y)



# print(( ( ( ( 13 + 5 ) * 2 ) - 4 ) / 2) - 13)


# x = 'appletini'
# y = 'Appletini'

# print('x > y is',x>y)
# print('x < y is',x<y)
# print('x == y is',x==y)
# print('x != y is',x!=y)
# print('x >= y is',x>=y)
# print('x <= y is',x<=y)


# X = "apple"
# Y = "banana"


# print('x > y is',x>y)
# print('x < y is',x<y)
# print('x == y is',x==y)
# print('x != y is',x!=y)
# print('x >= y is',x>=y)
# print('x <= y is',x<=y)


# A = 10
# B = 20
# print(A >= 10 or A < B)
# print(A > 10 or A < B)
# print(A> 10 or A > B)

# # A = 10
# # B = 20
# # print(A > 10 or A < B)
# # print(A >= 10 or A < B)


# print(not(A >= 10 or A < B))

# a = 10
# b = 4

# print(bin(~a), bin(a))

# # Print bitwise AND operation  
# print(a & b)
# # Print bitwise OR operation
# print(a | b)
# # Print bitwise NOT operation 
# print(~a)


# # print bitwise XOR operation 
# print(a ^ b)
# # print bitwise right shift operation 
# print(a >> 2)
# # print bitwise left shift operation 
# print(a << 2)



# import decimal
# from decimal import Decimal

# x = Decimal('0.1')
# y = Decimal('0.1')
# z = Decimal('0.1')

# print(x+y+z)

# ctx = decimal.getcontext()
# print(ctx.prec)
# print(ctx.rounding)

# a = [1,2,3,'c','m']

# b = ['another','c','m']
# # print(id(a))


# a[4] = b
# # print(a, len(a))

# # print(a[4][-2])


# n = ['t', 'e', 'a', 'm']

# print(a.index('c', 2))


# num = [1,2,3,4,5]

# num[1:4] = [5,8,7]

# print(num[4]*2)


# num.append([9, 'c'])

# print(num)

# num.insert(3, [7,8,9])

# print(num + [0,8,7])


# del num[5]

# num.remove(5)
# print(num)

# num.pop(3)

# d = num[1:3]

# print(d)


# print(isinstance(c, complex))

# print(isinstance(5j, complex))

# x = 15
# y = 4


# print('x + y =',x+y)

# print('x - y =',x-y)

# print('x * y =',x*y)


# print('x / y =',x/y)

# print('x // y =',x//y)


# print('x ** y =',x**y)

# print('x mod y =',x%y)



# print(( ( ( ( 13 + 5 ) * 2 ) - 4 ) / 2) - 13)


# x = 'appletini'
# y = 'Appletini'

# print('x > y is',x>y)
# print('x < y is',x<y)
# print('x == y is',x==y)
# print('x != y is',x!=y)
# print('x >= y is',x>=y)
# print('x <= y is',x<=y)


# X = "apple"
# Y = "banana"


# print('x > y is',x>y)
# print('x < y is',x<y)
# print('x == y is',x==y)
# print('x != y is',x!=y)
# print('x >= y is',x>=y)
# print('x <= y is',x<=y)


# A = 10
# B = 20
# print(A >= 10 or A < B)
# print(A > 10 or A < B)
# print(A> 10 or A > B)

# # A = 10
# # B = 20
# # print(A > 10 or A < B)
# # print(A >= 10 or A < B)


# print(not(A >= 10 or A < B))

# a = 10
# b = 4

# print(bin(~a), bin(a))

# # Print bitwise AND operation  
# print(a & b)
# # Print bitwise OR operation
# print(a | b)
# # Print bitwise NOT operation 
# print(~a)


# # print bitwise XOR operation 
# print(a ^ b)
# # print bitwise right shift operation 
# print(a >> 2)
# # print bitwise left shift operation 
# print(a << 2)



# import decimal
# from decimal import Decimal

# x = Decimal('0.1')
# y = Decimal('0.1')
# z = Decimal('0.1')

# print(x+y+z)

# ctx = decimal.getcontext()
# print(ctx.prec)
# print(ctx.rounding)

# a = [1,2,3,'c','m']

# b = ['another','c','m']
# # print(id(a))


# a[4] = b
# # print(a, len(a))

# # print(a[4][-2])


# n = ['t', 'e', 'a', 'm']

# print(a.index('c', 2))


# num = [1,2,3,4,5]

# num[1:4] = [5,8,7]

# print(num[4]*2)


# num.append([9, 'c'])

# print(num)

# num.insert(3, [7,8,9])

# print(num + [0,8,7])


# del num[5]

# num.remove(5)
# print(num)

# num.pop(3)

# d = num[1:3]

# print(d)
