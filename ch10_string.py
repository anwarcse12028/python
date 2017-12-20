var1 = 'Hello World!'
var2 = 'Python Programming'
print('var1 = ', var1 + '\n' + 'var2 = ', var2)

print('var1[0]: ', var1[0])
print('var2[1:5] :', var2[1:5])

print("updated sting :- ", var1[:6] + 'Python')

para_str = """ this is a long sting that is made up of several lines and non-printable characters such as 
               and they will show up that way when displayed. within the string, whether explicitly given like this withing 
               the brackets, just a within the variable assignment will also show up.
               z
            """
print('para_str = ', para_str)
print('length = ', len(para_str))
print('lower to upper:\n', para_str.upper())

s = "-"
seq = ("a", "b", "c")  # This is sequence of strings.
print('Using join() function: ', s.join(seq))

print("Max character: " + max(para_str))

print(para_str.split())
print(para_str.splitlines())

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("total legnth of list1 = ", len(list1))
list1.reverse()
print("reverse list1  = ", list1)

dict = {'Name': 'Dsi', 'Age': 7, 'Class': 'First'}
print("dict[Name]: ", dict['Name'])
print("dict[Age]: ", dict['Age'])

import calendar

cal = calendar.month(2017, 12)
print("Here is the calendar: ")
print(cal)


def printfuction(str):
    "This prints a passed string into this fuction"
    print(str)
    return


printfuction(para_str)


# Fibonacci numbers module

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


print('Fibonacci number: ', fib())
