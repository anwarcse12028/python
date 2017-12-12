# --------------------display in console---------------------
# print("Hello, Python!")

#   Ctrl + slash is used to line comment
# -----------------input from key board-----------------------
# name  = input('Enter Your Name  ')
# print('Your are ',name)

# ------------------multi line statement using line continuation character(\)--------------------
# mul_str  = 'item one'\
#     'item two'\
#     'item three'
# print('Multi line String:',mul_str)

# --------------------- python string -------
# str = 'Hello World'
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str+' test')

# --------------------- python list ------------------
# list = ['abcd', 786, 2.23, 'john', 70.2 ]
# list2 = [123, 'adfd']
# print(list)
# print(list2)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(list2 * 2)

#------------------------- python Tuples ---------------
# tuple = ('abcd', 786, 2.23, 'johm', 70.2 )
# tuple2 = (123, 'john')
# print(tuple)
# print(tuple2)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:])
# print(tuple2 * 2)
# print(tuple + tuple2)
# # tuple[2] = 111 #invalid syntax with tuple, i.e tuple does not support these, but list support

# --------------------- python dictionary (key, value pair) --------------------
dict = {}
dict['one'] = 'this is one' # 'one' is key and 'this is one' is value
dict[2] = 'this is two'     # similarly '2' is key and 'This is two' is value
tinydict = {'name':'john', 'code': 6734, 'dept': 'sales','anotherKey':'Another Value'}
print(dict['one'])
print(dict[2])
print(dict)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

