#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#Input : 11 5
#Output : 16

#	Author : Apurva Anil Jogal
#	Date : 13th March 2019

def  Add(no1,no2):
	ans= no1+no2;
	return ans;
	
number1=input("Enter first number: \n");
number2=input("Enetr second number: \n");

addition= Add(number1, number2);
print("Addition is : \t"addition);

