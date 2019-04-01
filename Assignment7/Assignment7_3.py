
#Write a program which contains one class named as Numbers.
#Arithmetic class contains one instance variables as Value.
#Inside init method initialise that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
#
#ChkPrime() method 		will returns true if number is prime otherwise return false.
#ChkPerfect() method	will returns true if number is perfect otherwise return false.
#Factors() method 		will display all factors of instance variable.
#SumFactors() method 	will return addition of all factors. Use this method in any another method as a helper method if required.

#After designing the above class call all instance methods by creating multiple objects.

# Author: Apurva Anil Jogal
# Date : 28th March 2019


class Numbers:
	
	def __init__(self, Value):
		self.Value = Value;
		
	def ChkPrime(self):
		i=2;
		flag = 0;
	
		while(i<=(self.Value/2)):
			if((self.Value)%i==0):
				flag=1;
				break;
			i=i+1;
	
		return flag;
		
	
	
	def ChkPerfect(self):
		
		self.summation=0;
	
		for i in range(1 , (self.Value)):
			if(self.Value % i == 0):
				self.summation += i; 
		return self.summation;
		
		if(self.summation == self.Value):
			return True;
			
			
	def Factors(self):
		
		for i in range(1 , (self.Value/2)):
			if(self.Value % i == 0):
				print(i),
				
			
	def SumFactors(self):
	
		self.summation=0;
	
		for i in range(1 , (self.Value)):
			if(self.Value % i == 0):
				self.summation += i; 
		return self.summation;
			
		
	
	
		
		
def main():
	
	Obj1 =  Numbers(6);
	Obj2 =  Numbers(2);
	
	
	checkPrime = Obj1.ChkPrime();
	sumFactor= Obj1.SumFactors();
	checkPerfect = Obj1.ChkPerfect();
	Obj1.Factors();
	
	
	
	if(checkPrime == True):
		print("It is Prime Number ");
	else:
		print("It is not Prime Number");	

	if(checkPerfect==True):
		print("It is Perfect Number ");
	else:
		print("It is not Perfect Number");	
		
	print("Summation of Factors is:", sumFactor);

	
if __name__ == "__main__":
	main();


