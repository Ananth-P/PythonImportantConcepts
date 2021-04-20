'''
In simple words
Filter :- takes all obj in list ,then return a new list with only that element return true after passing the function
Ex : [1,2,3,4] when apply this function def f(x): return x % 2 == 0 , output will be [2,4]

Map:-takes all obj in list ,then return a list with output of the function for each element
Ex : [1,2,3,4] when apply this function def f(x): return x % 2 == 0 , output will be [False,True,False,True]
'''




def f(x): return x % 2 == 0
def m(y): return y * 2

list = [1,2,3,4]

flist = filter(f, list)
print(list)
print(flist)

mlist = map(m, list)
print(list)
print(mlist)

# They both work a little bit differently but you've got the right idea.

# Map takes all objects in a list and allows you to apply a function to it Filter takes all objects in a list and runs that through a function to create a new list with all objects that return True in that function

# We see that to both the filter and map we pass a list and assign their output to a new list.

# Output of this script is

[1, 2, 3, 4]
[2, 4]
[1, 2, 3, 4]
[2, 4, 6, 8]
# Question arises is that function call of both filter and map looks same so how will they behave if we interchange the contents of functions passed to them.

def f(x): return x * 2
def m(y): return y % 2 == 0

list = [1,2,3,4]

flist = filter(f, list)
print(list)
print(flist)

mlist = map(m, list)
print(list)
print(mlist)
# This results in

[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[False, True, False, True]
# This shows filter evaluates the function and if true it returns back the passed element. Here the function

def f(x): return x * 2
evaluates to

def f(x): return x * 2 != 0

#In contrast map evaluates the function expression and returns back the result as items. So filter always expects its function to do comparison type of task to filter out the elements while map expects its functions to evaluate a statement to get some result.

#References :-
#https://stackoverflow.com/questions/47578353/python-difference-between-filter-and-map