
#Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130


#	Author : Apurva Anil Jogal
#	Date : 20th March 2019


arr= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,int(N)):
	element=input("Element : ");
	arr.append(int(element));
	
sum=0;
for i in arr:
	sum=sum+i;
	
print(sum);
