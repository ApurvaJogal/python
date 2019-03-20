#Write a program which contains filter(), map() and reduce() in it. 
#Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. 
#Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
#Map function will increase each number by 10. 
#Reduce will return product of all that numbers.

#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000


#	Author : Apurva Anil Jogal
#	Date   : 20th March 2019

# accepting list from user
inputList= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,N):
	element=input("Element : ");
	inputList.append(int(element));
	
	
#applying filer()

fliterList = list(filter(lambda no :(no>=70 and no<=90),inputList ))
print(fliterList);

#applying map()
mappedList = list(map(lambda no : no+10,fliterList));
print(mappedList);

#applying reduce()

reducedOutput = reduce(lambda no1, no2: no1*no2,mappedList);
print(reducedOutput);
