#print even numbers using lambda 

# As obeying the lambda functionality , with that only we couldnt done , so i used filter built-in functions to accomplish this task

even_values = list(filter(lambda k : k%2==0,range(0,20)))

#Explanation:-
# filter method 