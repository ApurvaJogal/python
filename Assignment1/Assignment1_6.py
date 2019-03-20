#Write a program which accept number from user and check whether that number is positive or negative or zero.
#Input : 11	Output : Positive Number
#Input : -8	Output : Negative Number
#Input : 0 	Output : Zero

#	Author	:	Apurva Anil Jogal
#	Date	:	13th March 2019

def posnegzero(number):
	
	if(number>0):
		print("Positive Number");
	elif(number<0):
		print("Negative Number");
	else:
		print("Zero");
	
	
num=input("Enter a number\n");

posnegzero(num);
