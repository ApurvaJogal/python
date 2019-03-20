#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#Input : 8	Output : False
#Input : 25	Output : True

#	Author	:	Apurva Anil Jogal
#	Date	:	13th March 2019

def divbyfive(number):
	
	flag=False;
	
	if(number%5==0):
		flag=True;
	else:
		flag=False;
	
	return flag;
	
	
num=input("Enter a number\n");

check=divbyfive(num);

if(check == True):
	print("True");
else:
	print("False");
