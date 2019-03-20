
#Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
#All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019


#we can import modules in 3 ways shown below (use any one)

#1
import Assignment2_1Module

#2
#import Assignment2_1Module as MyModule

#3
#from Assignment2_1Module import*



#accepting 2 inputs from user

num1=input("Enter first number\n");
num2=input("Enter second number\n");


# to access methods using #1 
add= Assignment2_1Module.Add(num1,num2);
sub= Assignment2_1Module.Sub(num1,num2);
mult= Assignment2_1Module.Mult(num1,num2);
div= Assignment2_1Module.Div(num1,num2);


# to access methods using #2
#add= MyModule.Add(num1,num2);
#sub= MyModule.Sub(num1,num2);
#mult= MyModule.Mult(num1,num2);
#div= MyModule.Div(num1,num2);

# to access methods using #3

#add= Add(num1,num2);
#sub= Sub(num1,num2);
#mult=Mult(num1,num2);
#div= Div(num1,num2);

print("Addition is"),
print(add);
print("Subtraction is"),
print(sub);
print("Multiplication is "),
print(mult);
print("Division is "),
print(div);
