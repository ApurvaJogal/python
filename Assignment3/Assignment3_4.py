#Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

#	Author : Apurva Anil Jogal
#	Date : 20th March 2019



def count(brr,search):
	count=0;
	for i in brr:
		if(i==search):
			count+=1;
	return count;
	
	
arr= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,int(N)):
	element=input("Element : ");
	arr.append(int(element));
	
search=input("Element to search : ");

ret=count(arr,search);
print(ret);



