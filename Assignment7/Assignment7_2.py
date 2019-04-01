

#Write a program which contains one class named as BankAccount.
#BankAccount class contains two instance variables as Name & Amount.
#That class contains one class variable as ROI which is initialise to 10.5.
#Inside init method initialise all name and amount variables by accepting the values from user.
#There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
#
#Deposit() method 			will accept the amount from user and add that value in class instance variable Amount.
#Withdraw() method 			will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
#CalculateIntrest() method 	will calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
#Display() method        	will display value of all the instance variables as Name and Amount.

#After designing the above class call all instance methods by creating multiple objects.


# Author: Apurva Anil Jogal
# Date : 28th March 2019

class BankAccount:
	
	ROI = 10.5;
	
	def __init__(self, name, amount):
		self.Name= name;
		self.Amount= amount;	
		
	def Deposit(self):
		damount = input("Enter Deposite account :\n");
		self.Amount = self.Amount + damount;
		print("Account Balance:", self.Amount);
	
	
	def Withdraw(self):
		wamount = input("Enter withdrawal account :\n");
		self.Amount = self.Amount - wamount;
		print("Account Balance:", self.Amount);
	
	
	def CalculateIntrest(self): 
		self.interest = self.Amount * BankAccount.ROI * 12;
		print("Interest is:",self.interest);
		
	
	def	Display(self):
		print("Account holder:", self.Name);
		print("Account Balance:", self.Amount);
	
	
def main():
	Obj1 = BankAccount("Apurva", 10000);
	Obj2 = BankAccount("XYZ", 20000);
		
	Obj1.Display();	
	Obj1.Deposit();
	Obj1.Withdraw();
	Obj1.CalculateIntrest();
	Obj1.Display();	
	
	
	Obj2.Display();	
	Obj2.Deposit();
	Obj2.Withdraw();
	Obj2.CalculateIntrest();
	Obj2.Display();		

if __name__ == "__main__":
	main();
	
	

