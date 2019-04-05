#Design python application which contains two threads named as thread1 and thread2.
#Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
#After execution of thread1 gets completed then schedule thread2.

# Author: Apurva Anil Jogal
# Date : 4th April 2019

from threading import *

def forwardFifty():
	for i in range(1,50):
		print("forwardFifty",i);
		

def reverseFifty():
	for i in reversed(range(1,50)):
		print("reverseFifty",i);


def main():
	
	
	thread1 = Thread(target=forwardFifty);
	thread2 = Thread(target=reverseFifty);
	
	# Will execute both in parallel
	thread1.start();
	thread2.start();
	
	# Joins threads back to the parent process, which is this program.
	thread1.join();
	thread2.join();
	
	print("Exit from main");
	
if __name__ == "__main__":
	main();

