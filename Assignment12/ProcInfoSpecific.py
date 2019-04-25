#Design automation script which accept process name and display information of that process if it is running.
#Usage : ProcInfo.py Notepad

#use python3 instead of python


# Author : Apurva Anil Jogal
# Date : 23rd April 2019

import psutil;
from sys import *;
def ProcessDisplay(ProcessName):
	flag = False;
	listprocess= [];
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username']);
			
			if(ProcessName.lower() in pinfo['name'].lower()):
				listprocess.append(pinfo);
				flag=True;
			
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.Zombieprocess):
			pass;
			
	if flag:
		print("Process Information:");
		print(pinfo);
	
	else:
		print("Process Not Found");
			
	return flag;
	
def main():
	print("Process Monitoring");
	
	listprocess = ProcessDisplay(argv[1]);
	
	

if __name__== "__main__":
	main();

