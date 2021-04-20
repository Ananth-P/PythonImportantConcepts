# class method vs static method


class Student:
	school = 'BCM' # class variables

	def __init__(self,m1,m2,m3):
		self.m1	= m1  #instance variables 
		self.m2	= m2
		self.m3	= m3

	def avg(self): # instance methods because we passing self
		return (self.m1+self.m2+self.m3)/3

	def get_m1(self): #accessor methods or getter
		return self.m1

	def set_m1(self,value): # mutator methods or setter
		self.m1 = value

	@classmethod
	def getSchool(cls):
		return cls.school

	@staticmethod
	def info():
		return "This is the static method class"




s1 = Student(34,47,32)
s2 = Student(89,32,12)


print(s1.avg())
print(s2.avg())
print(Student.getSchool()) # class method call
print(Student.info()) # static method call

# two methods:-
# accessor methods :- fetch the value
# mutator methods  :-set the value
# static methods :- the method which doesn't do with class variables and doesn't do with instance variables
# class methods : the method which need to deal with class variables


#Note
# if you are working with class variables ,we could use 'cls' keyword
# if you are working with instance , we could use 'self' keyword