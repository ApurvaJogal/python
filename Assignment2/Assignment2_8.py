#Write a program which accept one number and display below pattern.
#Input : 5
#Output :
#		1
#		1 2 
#		1 2 3 
#		1 2 3 4
#		1 2 3 4 5 

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019



def pattern(no):

		i=1;
		
		while(i<=no):
			j=1;
			while(j<=i):
				print(j),
				j=j+1;
			print("");
			i=i+1;


num=input("Enter number\n");
pattern(num);


