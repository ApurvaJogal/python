#Design python application which creates three threads as small, capital, digits. 
#All the threads accepts string as parameter. 
#Small thread display number of small characters
#capital thread display number of capital characters 
#and digits thread display number of digits. 
#Display id and name of each thread.


# Author: Apurva Anil Jogal
# Date : 4th April 2019

from threading import *

def calcSmall (string1):
	countSmall=0;
	
	for i in string1:
		if i.isupper():
		    countSmall += 1;	
	print("small =",countSmall);	    
		    
def calcCapital (string2):
	countCapital=0;
	
	for i in string2:
		if i.islower():
		    countCapital += 1;
	print("capital =",countCapital);
	
def calcDigit (string3):
	countDigit=0;
	
	for i in string3:
		if i.isdigit():
		    countDigit +=1;
	print("digit =",countDigit);
	
	
def main():
	
	stringInput= input("Enter the string\n");
	
	small = Thread(target=calcSmall, args=(stringInput,));
	capital = Thread(target=calcCapital, args=(stringInput,));
	digits = Thread(target=calcDigit, args=(stringInput,));
 
 
 	# Will execute three threads in parallel
 	small.start();
 	capital.start();
 	digits.start();
 	
 	# Joins threads back to the parent process, which is this program.
 	small.join();
 	capital.join();
 	digits.join();
 	
 	
	print("Exit from main");
	
if __name__ == "__main__":
	main();

