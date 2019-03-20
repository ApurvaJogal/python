
#
#Write a program which accept number from user and print that number of "*" on screen.
#Input : 5
#Output : * * * * *
#

#	Author	:	Apurva Anil Jogal
#	Date	:	13th March 2019


def pattern(number):
	i=0;
	
	while(i<number):
		print("*"),
		i=i+1;
		
		
num=input("Enter a number \n");

pattern(num);
