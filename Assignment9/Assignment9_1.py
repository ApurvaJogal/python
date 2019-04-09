#Write a program which accepts file name from user and check whether that file exists in current directory or not.
#Input : Demo.txt
#Check whether Demo.txt exists or not.

# Author: Apurva Anil Jogal
# Date : 9th April 2019

#Note : Please consider Assignment9/Demo.txt for this question.

import os;

def main():
	
	try:
		filename = input("Enter file name with extension\n");
		fd = open(filename);
		print("File Exists");
		fd.close();
	
	except Exception as eobj:
		print(eobj);
		print("File does not exists.");
	
	
if __name__ == "__main__":
	main();
	

	
		


