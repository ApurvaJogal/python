#Design python application which creates two thread named as even and odd.
#Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

# Author: Apurva Anil Jogal
# Date : 5th April 20

from threading import *;

def funEven():
	
	for i in range(10):
	
		if(i%2==0):	
			print("funEven",i)
	
def funOdd():
	for i in range(10):
		if(i%2 != 0):
			print("funOdd",i)
			



def main():
		
	even = Thread(target= funEven);		
	odd = Thread(target= funOdd);
	
	
	# Will execute both in parallel
	even.start()
	odd.start()
	
	# Joins threads back to the parent process, which is this program.
	even.join()
	odd.join()
	
	print("Exit from main");
	
if __name__ == "__main__":
	main();


