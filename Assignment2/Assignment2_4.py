
#Write a program which accept one number form user and return addition of its factors.
#Input :12 Output : 16(1+2+3+4+6)

#	Author : Apurva Anil Jogal
#	Date : 14th March 2019



def addfactors(no):
	i =1;
	sum=0;
	
	while(i<=no/2):
		if(no%i==0):
			sum=sum+i;
		i=i+1;
	return sum;


num=input("Enter Number\n");
ans=addfactors(num);

print(ans);
