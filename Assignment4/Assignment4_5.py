#Write a program which contains filter(), map() and reduce() in it. 
#Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. 
#Filter should filter out all prime numbers. 
#Map function will multiply each number by 2. 
#Reduce will return Maximum number from that numbers.
#(You can also use normal functions instead of lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62

#	Author : Apurva Anil Jogal
#	Date   : 20th March 2019

# accepting list from user
inputList= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,N):
	element=input("Element : ");
	inputList.append(int(element));
	
	
	
def ChkPrime(number):
	flag=True;
	for i in range(2,(number)):
		if((number%i)==0):
			flag=False
			break;
			
	return flag;
	
#applying filer()

fliterList = list(filter(lambda no :(ChkPrime(no)),inputList ))
print(fliterList);

#applying map()
mappedList = list(map(lambda no : no*2,fliterList));
print(mappedList);

#applying reduce()

reducedOutput = reduce(max,mappedList);
print(reducedOutput);
