#Write a program which contains filter(), map() and reduce() in it. 
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which are even. 
#Map function will calculate its square.
#Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204


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

fliterList = list(filter(lambda no :(no%2==0),inputList ))
print(fliterList);

#applying map()
mappedList = list(map(lambda no : no**2,fliterList));
print(mappedList);

#applying reduce()

reducedOutput = reduce(lambda no1, no2: no1+no2,mappedList);
print(reducedOutput);
