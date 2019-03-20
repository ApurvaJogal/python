#Write a program which contains one function named as ChkNum() which accept one parameter as number.
#If number is even then it should display "even number" otherwise display "odd number".
#input	8 	Output	Even Number
#input	11	Output	Odd Number

#	Author : Apurva Anil Jogal
#	Date : 13th March 2019



def ChkNum(no):
	if(no%2 == 0):
		print("Even Number");
	else:
		print("Odd Number");
		

number=input("Enter a number");
ChkNum(number);

