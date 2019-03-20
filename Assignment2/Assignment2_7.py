#Write a program which accept one number and display below pattern.
#Input :5
#Output :
#		1 1 1 1 1
#		2 2 2 2 2
#		3 3 3 3 3
#		4 4 4 4 4
#		5 5 5 5 5

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019

def pattern(no):
	
		i=1;
		
		while(i<=no):
			j=0;
			while(j<no):
				print(i),
				j=j+1;
			print("");
			i=i+1;


num=input("Enter number\n");
pattern(num);
