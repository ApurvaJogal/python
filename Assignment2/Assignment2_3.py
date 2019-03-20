
#Write a program which accept one number from user and return its factorial.
#Input :5	Output : 120


#	Author : Apurva Anil Jogal
#	Date : 14th March 2019


def factorial(no):
	i=no;
	fact=1;
	
	while(i>0):
		fact=fact*i;
		i=i-1;
	
	return fact;
	
	
num=input("Enter a number\n");
ans=factorial(num);
print("Factorial is"),
print(ans);
