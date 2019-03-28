#Write a program which contains one class named as Arithmetic.
#Arithmetic class contains two instance variables as Value1 ,Value2.
#Inside init method initialise all instance variables to 0.
#There are five instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
#Accept() 			method will accept value of Value1 and Value2 from user.
#Addition() 		method will perform addition of Value1 ,Value2 and return result.
#Subtraction() 		method will perform subtraction of Value1 ,Value2 and return result.
#Multiplication() 	method will perform multiplication of Value1 ,Value2 and return result.
#Division() 		method will perform division of Value1 ,Value2 and return result.
#After designing the above class call all instance methods by creating multiple objects.

# Author: Apurva Anil Jogal
# Date : 28th March 2019

class Arithmetic:

	def __init__(self):
		self.Value1 = 0;
		self.Value2 = 0;

	def Accept(self):
		self.Value1 = input("Enter first value: \n");
		self.Value2 = input("Enter second value: \n");
	
	def Addition(self):
		return (self.Value1 + self.Value2);
	
	def Subtraction(self):
		return (self.Value1 - self.Value2);
	
	def Multiplication(self):
		return (self.Value1 * self.Value2);
	
	def Division(self):
		return (float(self.Value1 / self.Value2));
		
		
		

Obj1 = Arithmetic();
Obj2 = Arithmetic();
Obj3 = Arithmetic();
		
Obj1.Accept();
add1 = Obj1.Addition();
sub1 = Obj1.Subtraction();
mul1 = Obj1.Multiplication();
div1 = Obj1.Division();

print("Addition :"),
print(add1);
print("Subtraction"),
print( sub1)
print("Multiplication"),
print(mul1)
print("Division"), 
print(div1);


Obj2.Accept();
add2 = Obj2.Addition();
sub2 = Obj2.Subtraction();
mul2 = Obj2.Multiplication();
div2 = Obj2.Division();

print("Addition :"),
print(add2);
print("Subtraction"),
print( sub2)
print("Multiplication"),
print(mul2)
print("Division"), 
print(div2);


Obj3.Accept();
add3 = Obj3.Addition();
sub3 = Obj3.Subtraction();
mul3 = Obj3.Multiplication();
div3 = Obj3.Division();

print("Addition :"),
print(add3);
print("Subtraction"),
print( sub3)
print("Multiplication"),
print(mul3)
print("Division"), 
print(div3);



