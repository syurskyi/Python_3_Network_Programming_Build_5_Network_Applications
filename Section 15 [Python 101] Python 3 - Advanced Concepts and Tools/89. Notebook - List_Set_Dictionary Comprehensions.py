#List / Set / Dictionary comprehensions
#Instead of...
list1 = []
for i in range(10):
    j = i ** 2
    list1.append(j)

#...we can use a list comprehension
list2 = [x ** 2 for x in range(10)]

list3 = [x ** 2 for x in range(10) if x > 5] #with a conditional statament

set1 = {x ** 2 for x in range(10)}     #set comprehension

dict1 = {x: x * 2 for x in range(10)} #dictionary comprehension