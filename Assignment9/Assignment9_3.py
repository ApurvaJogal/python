#Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. 
#Accept file name through command line arguments.
#Input : ABC.txt
#Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

# Author: Apurva Anil Jogal
# Date : 9th April 2019

#Note : Please consider Assignment9/Demo.txt  as first file and ABC.txt as second file for this question.

import sys;
from shutil import *;
import os;

def main():
	
	try:
		source = sys.argv[1];
		destination = sys.argv[2];
		
		fds = open(source,"r");
		fdd = open(destination, "w+a+r");
		
		copy2(source, destination);
		
		fds.seek(0);
		fdd.seek(0);
		
		print("Source file:\n",fds.read());
		print("Destination file:\n",fdd.read());
		
		
		fds.close();
		fdd.close();
		
	except Exception as eobj:
		print(eobj);
		print("File does not exists.");
		
if __name__ == "__main__":
	main();

