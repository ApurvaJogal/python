
#Write a program which accept one number and display below pattern.
#Input :5	
#Output :
#		* * * * *
#		* * * *
#		* * *
#		* * 
#		*

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019


def pattern(no):
	
		i=0;
		
		while(i<no):
			j=i;
			while(j<no):
				print("*"),
				j=j+1;
			print("");
			i=i+1;


num=input("Enter number\n");
pattern(num);
