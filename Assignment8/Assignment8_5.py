#Design python application which contains two threads named as thread1 and thread2.
#Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
#After execution of thread1 gets completed then schedule thread2.

# Author: Apurva Anil Jogal
# Date : 4th April 2019

from threading import *

def funCaller(function, lock):
	function(lock);

def forwardFifty(lock):

	lock.acquire()
	for i in range(1,51):
		print("forwardFifty",i);
	lock.release();

def reverseFifty(lock):

	lock.acquire()
	for i in reversed(range(1,51)):
		print("reverseFifty",i);
	lock.release();


def main():
	
	#creating a lock
	
	lock = Lock();
	
	thread1 = Thread(target=funCaller, args=(forwardFifty,lock,));
	thread2 = Thread(target=funCaller, args=(reverseFifty,lock,));
	
	# Will execute both in parallel
	thread1.start();
	thread2.start();
	
	# Joins threads back to the parent process, which is this program.
	thread1.join();
	thread2.join();
	
	print("Exit from main");
	
if __name__ == "__main__":
	main();
