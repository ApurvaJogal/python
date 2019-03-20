# module file for Assignment3_5.py

#	Author : Apurva Anil Jogal
#	Date : 20th March 2019

def ChkPrime(number):
	flag=True;
	for i in range(2,(number)):
		if((number%i)==0):
			flag=False
			break;
			
	return flag;
		
				
		
