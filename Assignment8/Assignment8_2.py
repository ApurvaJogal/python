#Design python application which creates two threads as evenfactor and oddfactor.
#Both the thread accept one parameter as integer.
#Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. 
#After execution of both the thread gets completed main thread should display message as "exit from main".

# Author: Apurva Anil Jogal
# Date : 5th April 2019

from threading import *;

def funEvenFactor(number):
	
	for i in range(1,number):
	
		if( number%i ==0 and i%2==0):	
			print("funEvenFactor",i)
	
def funOddFactor(number):
	for i in range(1,number):
		if(number%i ==0 and i%2 != 0):
			print("funOddFactor",i)
			

def main():

	no = input("Enter a number");
		
	evenfactor = Thread(target= funEvenFactor,args = (no,));		
	oddfactor = Thread(target= funOddFactor, args = (no,));
	
	
	# Will execute both in parallel
	evenfactor.start()
	oddfactor.start()
	
	# Joins threads back to the parent process, which is this program.
	evenfactor.join()
	oddfactor.join()
	
	print("Exit from main");
	
if __name__ == "__main__":
	main();


