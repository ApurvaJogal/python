#Write a program which accept number from user and return number of digits in that number.
#Input : 5187934
#Output : 7

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019


def numdigits(no):
	temp=no;
	count=0;
	
	while(temp!=0):
		count=count+1;
		temp=temp/10;
	return count;
	
num=input("Enter Number\n");
digit=numdigits(num);

print("Number of digits:"),
print(digit);
