#Design automation script which accept directory name and display checksum of all files.
#Usage : DirectoryChecksum.py "Demo"
#Demo is name of directory.

#Author : Apurva Anil Jogal
#Date : 23rd April 2019

from sys import *;
import os;
import hashlib;


def hashfile(path, blocksize=1024):
	afile= open(path,'rb');
	hasher = hashlib.md5();
	buf=afile.read(blocksize);
	
	while len(buf) > 0:
		hasher.update(buf);
		buf=afile.read(blocksize);
	afile.close();
	
	return hasher.hexdigest()
	
def DisplayChecksum(path):
	flag = os.path.isabs(path);
	if(flag == False):
		path = os.path.abspath(path)
	exists = os.path.isdir(path);
	
	if exists:
		for dirName, subDir, fileList in os.walk(path):
			print("Current folder is: "+dirName);
			for filen in fileList:
				path = os.path.join(dirName,filen);
				file_hash = hashfile(path);
				print(path);
				print(file_hash);
				print('');
	else:
		print("MError:Invalid Path");
		

def main():

	print("Apllication Name: "+argv[0]);
	if(len(argv) != 2):
		print("Error: Invalid number of arguments");
		exit();
	
	if((argv[1]=="-h") or (argv[1]=="-H")):
		print("This script is used to traverse specific directory and diplsay checksum");
		exit();
		
	if((argv[1]=="-u") or (argv[1]=="-U")):
		print("Usage: Application_Name Absolute_path_of_directory Extension");
		exit();
		
	try:
		arr = DisplayChecksum(argv[1]);
					
	except Exception as eobj:
		print("Error: Invalid input", eobj);
		
		
if __name__ == "__main__":
	main()		
	


