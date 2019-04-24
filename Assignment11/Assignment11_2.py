# Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. 
# Log.txt file should be created into current directory.
# Usage : DirectoryDusplicate.py "Demo"

#Author : Apurva Anil Jogal
#Date : 23rd April 2019

from sys import *;
import os;
import hashlib;
import datetime;

def hashfile(path, blocksize=1024):
	fd= open(path,'rb');
	hasher = hashlib.md5();
	buf=fd.read(blocksize);
	
	while len(buf) > 0:
		hasher.update(buf);
		buf=fd.read(blocksize);
	fd.close();
	
	return hasher.hexdigest()
	
def FindDuplicate(path):
	flag = os.path.isabs(path);
	if(flag == False):
		path = os.path.abspath(path)
	exists = os.path.isdir(path);
	
	dups={};
	
	if exists:
		for dirName, subDir, fileList in os.walk(path):
			print("Current folder is: "+dirName);
			for filen in fileList:
				path = os.path.join(dirName,filen);
				file_hash = hashfile(path);
				if file_hash in dups:
					dups[file_hash].append(path);
				else:
					dups[file_hash] = [path];
				
		return dups;
	else:
		print("MError:Invalid Path");
		
def PrintDuplicate(dict1):
	results = list(filter(lambda x : len(x)>1,dict1.values()))
	time1 = datetime.datetime.now();
	
	fd = open("DetectLog %s.txt" %time1,"w+a");
	if( len(results)> 0):
		fd.write("Dupliate found\n");
		fd.write("Following files are Identical:\n");
		
		icnt=0;
		for result in results:
			for subresult in result:
				icnt+=1;
				if icnt>=2:
					fd.write("\t\t%s\n" %subresult);
	else:
		fd.write("MError: No duplicate files found\n");


def main():

	print("Apllication Name: "+argv[0]);
	if(len(argv) != 2):
		print("Error: Invalid number of arguments");
		exit();
	
	if((argv[1]=="-h") or (argv[1]=="-H")):
		print("This script is used to traverse specific directory and diplsay sizes of files");
		exit();
		
	if((argv[1]=="-u") or (argv[1]=="-U")):
		print("Usage: Application_Name Absolute_path_of_directory Extension");
		exit();
		
	try:
		arr = {};
		arr= FindDuplicate(argv[1]);
		PrintDuplicate(arr);
		
	except Exception as eobj:
		print("Error: Invalid input", eobj);
		
		
if __name__ == "__main__":
	main()		
	
