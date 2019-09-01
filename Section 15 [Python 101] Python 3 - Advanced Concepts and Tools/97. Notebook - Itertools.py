#Itertools - built-in Python module for working with iterable data sets
import itertools

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

#chain() - takes several sequences and chains them together
chain(list1, list2)

list(chain(list1, list2)) #result is [1, 2, 3, 'a', 'b', 'c', 101, 102, 103, 'X', 'Y']

#count() - returns an iterator that generates consecutive integers until you stop it, otherwise it will go on forever
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break   #result is printing the numbers between 10 and 50 inclusively, with a step of 2.5

#cycle() - returns an iterator that simply repeats the value given as argument infinitely; you have to find a way to break out of the infinite loop
a = range(11, 16)

for i in cycle(a):
	print(i) #use Ctrl+C to break out of the infinite loop

#filterfalse() - returns the elements for which the function you give as argument returns False
list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])) #in Python 2 the result is [5, 6, 7]; in Python 3 there is no ifilter() like in Python 2, just filter() and filterfalse()

#islice() - performs slicing; we can specify a starting point of the slice, an end point and a step
list(islice(range(10), 2, 9, 2)) #result is [2, 4, 6, 8]