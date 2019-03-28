#Write a program which contains one class named as Demo.
#Demo class contains two instance variables as no1 ,no2.
#That class contains one class variable as Value.
#There are two instance methods of class as Fun and Gun which displays values of instance variables.
#Initialise instance variable in init method by accepting the values from user. 
#After creating the class create the two objects of Demo class as
#Obj1 = Demo(11,21)
#Obj2 = Demo(51,101)
#
#Now call the instance methods as
#Obj1.Fun()
#Obj2.Fun()
#Obj1.Gun()
#Obj2.Gun()


# Author: Apurva Anil Jogal
# Date : 28th March 2019

class Demo:
	
	#class variable
	Value=None;
	
	
	def __init__(self, x, y):
	
		self.no1 = input("Enter first number: \n"); 	#instance variable
		self.no2 = input("Enter second number: \n");	#instance variable
	
	
	def Fun(self):		#instance method
	
		print(self.no1,self.no2);
	
	
	def Gun(self):		#instance method
	
		print(self.no1,self.no2);
	


Obj1 = Demo(11,21);
Obj2 = Demo(51,101);

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()








