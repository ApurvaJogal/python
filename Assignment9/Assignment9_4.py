#Write a program which accept two file names from user and compare contents of both the files. 
#If both the files contains same contents then display success otherwise display failure.
#Accept names of both the files from command line.

#Input : Demo.txt Hello.txt
#Compare contents of Demo.txt and Hello.txt

# Author: Apurva Anil Jogal
# Date : 9th April 2019

#Note : Please consider Assignment9/Demo.txt and ABC.txt for this question.

import sys;
import os;
def main():
	
	flag = True;
	try:
		
		file1 = sys.argv[1];
		file2 = sys.argv[2];
		
	
		fd1 = open(file1, 'r');
		fd2 = open(file2, 'r');
	
		for line1 in fd1:
			for line2 in fd2:
			    if line1 != line2:
		        	flag = False;
		        	
		if(flag == True):
			print("Success");
		else:
			print("Failure");
				    	
		fd1.close();
		fd2.close();
		
		
	
	except Exception:
		print(eobj);
		print("File1 or File2 does not exists.");	
		
		
if __name__ == "__main__":
	main();

