#Design python application which creates two threads as evenlist and oddlist. 
#Both the threads accept list of integers as parameter. 
#Evenlist thread add all even elements from input list and display the addition. 
#Oddlist thread add all odd elements from input list and display the addition.

# Author: Apurva Anil Jogal
# Date : 5th April 2019


from threading import *

def funEven(numberlist1):
	
	for i in numberlist1:
		if(i % 2 == 0):
			print("Even", i);
			
			

def funOdd(numberlist2):
	
	for i in numberlist2:
		if(i % 2 != 0):
			print("Odd", i);
			
			
			
def main():

	inputList= list();

	N=input("Enter Number of elements in the list: ");

	print("Enter elements in the list");

	for i in range(0,N):
		element=int(input("Element : "));
		inputList.append(int(element));
		
	evenlist = Thread(target= funEven,args = (inputList,));		
	oddlist = Thread(target= funOdd, args = (inputList,));
	
	
	# Will execute both in parallel
	evenlist.start()
	oddlist.start()
	
	# Joins threads back to the parent process, which is this program.
	evenlist.join()
	oddlist.join()
	
	print("Exit from main");
	
if __name__ == "__main__":
	main();
	

