#Write a program which accept one number for user and check whether number is prime or not.
#Input :5	Output : It is Prime Number

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019

def prime(no):
	i=2;
	flag = 0;
	
	
	while(i<=no/2):
		if(no%i==0):
			flag=1;
			break;
		i=i+1;
	
	return flag;
	

num=input("Enter number\n");
check=prime(num);

if(check==0):
	print("It is Prime Number ");
else:
	print("It is not Prime Number");	

