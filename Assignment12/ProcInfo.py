#Design automation script which display information of running processes as its name, PID, Username.
#Usage : ProcInfo.py

#use python3 instead of python to run this code

# Author : Apurva Anil Jogal
# Date : 23rd April 2019

import psutil;

def ProcessDisplay():
	listprocess= [];
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username']);
			listprocess.append(pinfo)
			
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.Zombieprocess):
			pass;
			
	return listprocess;
	
def main():
	print("Process Monitor");
	
	listprocess = ProcessDisplay();
	
	for element in listprocess:
		print(element);
		

if __name__== "__main__":
	main();

