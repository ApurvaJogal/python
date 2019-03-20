
#Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 54 (13 + 5 + 7 +2 + 5)

#	Author : Apurva Anil Jogal
#	Date : 20th March 2019


from MarvellousNum import *


def ListPrime(brr):
	
	addition=0;
	for i in brr:
		bret=ChkPrime(i);
		if(bret==True):
			addition+=i
	return addition;
			
				
	

arr= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,int(N)):
	element=input("Element : ");
	arr.append(int(element));
	
ret=ListPrime(arr);
print(ret);

