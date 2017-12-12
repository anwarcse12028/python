import sys

# ----------------Arithmetic Operators : + - * / % **(Exponent) //(floor division) ---------------
a = 9.0
b = 2.0
# res = a//b
# rem = a%b
# print('res = ',res, ' rem = ',rem)
# print(a ** b)

# ------------------- Python Logical Operators (and, or, not ) -------------
# if(a>10 and b > 5):
#     print("True")
# else:
#     print('False')

# -----------------python Bitwise Operators ---------------------
# bin( number) fuction is used to display integer number as binary number
# f_bit = 60
# s_bit = 13
# print('f_bit & s_bit  = ',f_bit & s_bit,' = :',bin(f_bit & s_bit))
# print('f_bit | s_bit  = ',f_bit | s_bit,' = :',bin(f_bit | s_bit))
# print('f_bit ^ s_bit  = ',f_bit ^ s_bit,' = :',bin(f_bit ^ s_bit))
# print('~f_bit  = ',~f_bit,' = :',bin(~f_bit))
# print("result of LEFT Shift is ", f_bit<<2,' = :',bin(f_bit<<2)) # left shift is used to multiply
# print("result of Right Shift is ", f_bit>>2,' = :',bin(f_bit>>2)) # right shift is used to divide

# ---------------- python membership operators (in, not in ) --------------
# list = [1,2,3,4,5,6]
# if(a in list):
#     print("a is found")
# else:
#     print('Not found')

# ------------------- python identity operators (is , is not) -------------------
# a = 10
# b = 10
# if(a is b):
#     print("a  and  b have smae identity")
# else:
#     print("a and b do not have same identity")

# ----------------- python  nested if else -----------------------------------
# if(a>b):
#     print("a is greater than b")
# elif(b>a):
#     print('b is greater than a')
# else:
#     print("a and b are equal")

# ------------------------------ python while loop --------------------------------------
count = 0
# while(count<10):
#     print('The count is :', count)
#     count+=1
# print("Good bye")
# ---------------------- while else------------
# while(count<5):
#     print(count)
#     count+=1
# else:
#     print('count is not less than 5')

# ---------------------------------python for loop -----------------------------------

# ---------range() built in function is used to iterate over a sequence of numbers.
# print("using range() function :range(5) = ",range(5),' = ',list(range(5)))
# for var in list(range(5)):
#     print(var)
# fruits = ['banana', 'apple', 'manago']
# for fruit in fruits:
#     print('current fruit : ',fruit)
# print('Good bye!')
#
# print("accessing array by index")
# # -------Iterating by sequence Index
# for index in range(len(fruits)):
#     print('Current fruit: ', fruits[index])
#
# # ---- inner loop ----
# for i in range(1,11):
#     for j in range(1,11):
#         k = i*j
#         print(k, end=' ') # end = '' which appends a space instead of default newline
#     print()
# #-----loop control statement (break , continue, &  pass statement) ---------------
# for letter in 'python':
#     if letter == 'h':
#         #break
#         #continue
#         pass # used when you do not want any command or code to execute.
#         print("this is a pass statement")
#     print('current letter : ', letter)

# -------------------------- Python fibonacci number printing ---------------------------------
# def fibonacci(n): #generator function
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a # yield keeps track the last execution and the second next() call continues from previous value
#         a, b = b, a+b
#         counter += 1
# f = fibonacci(10) # f is iterator object
#
# while True:
#     try:
#         print(next(f), end=" ") # next method called untill it reaches the yield statement, which returns the yielded value
#     except StopIteration:
#         sys.exit()


# ----------------Python Mathematical Functions ---------------------------------------------
# all functions are: abs(x), ceil(x), cmp(x,y), exp(x), fabs(x), floor(x), log(x), log10(x), max(x1,x2,....),
#                    min(x1,x2,...), modf(x), round(x[,n]), sqrt(x)

print(" abs(-45) :", abs(-45))
print("abs(100.12)  :", abs(100.12))

import math

print('math.ceil(-45.17) is ', math.ceil(-45.17))
print('math.exp(-45.17) is:', math.exp(-45.17))
print('math.fabs(-45.17) is: ',
      math.fabs(-45.17))  # fabs works only on float and integer whreas abs() works with complex number also
