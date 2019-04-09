#Accept file name and one string from user and return the frequency of that string from file.
#Input : Demo.txt
#Marvellous
#Search "Marvellous" in Demo.txt

# Author: Apurva Anil Jogal
# Date : 9th April 2019

#Note : Please consider Assignment9/Demo_for_5.txt  as first file and ABC.txt for this question.

import sys;
import os;

def main():

	wordCount = 0;
	
	try:
		
		filename = input("Enter the file name:\n");		
		stringname = input("Enter the string/word:\n");
		
		fd = open(filename, 'r');
		
		for line in fd:
			count = line.count(stringname);
			wordCount += count; 
		
		print("frequency is :",wordCount)
  	
			    	
		fd.close();
	
	except Exception as eobj:
		print(eobj);
		print("File does not exists.");	
		
		
if __name__ == "__main__":
	main();

