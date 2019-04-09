#Write a program which accept file name from user and open that file and display the contents of that file on screen.
#Input : Demo.txt
#Display contents of Demo.txt on console.

# Author: Apurva Anil Jogal
# Date : 9th April 2019


#Note : Please consider Assignment9/Demo.txt for this question.

import os;

def main():
	
	try:
		filename = input("Enter file name with extension\n");
		fd = open(filename,'r');
		print(fd.read());
		fd.seek(0);
		fd.close();
	
	except Exception as eobj:
		print(eobj);
		print("File does not exists.");
		
if __name__ == "__main__":
	main();

