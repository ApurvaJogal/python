# Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934
#Output : 37

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019


def adddigits(no):
	temp=no;
	sum=0;
	
	while(temp!=0):
		digit=temp%10;
		sum=sum+digit;
		temp=temp/10;
	return sum;
	
num=input("Enter Number\n");
digit=adddigits(num);

print("Sum of number of digits:"),
print(digit);
