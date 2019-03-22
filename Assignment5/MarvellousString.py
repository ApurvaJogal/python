
# Author: Apurva Anil Jogal
# Date : 22nd March 2019

#Write a program which contains one function that accepts string from user and return reverse of that string.
#Input : "Marvellous Pune"
#Output : "enuP suollevraM"

def reverseString(str1):

  str2 = "" 
  for i in str1: 
    str2 = i + str2
  return str2
	
	
	
#Write a program which contains one function that accepts string from user and return number of words from that string.
#Input : "Marvellous Infosystems by Piyush Khairnar"
#Output : 5

def numberofWords(str1):

	return len(str1.split())



#Write a program which contains one function that accepts string from user and print all permutations of that string.
#Input : XYZ
#Output : XYZ XZY YXZ YXZ ZXY ZYX
from itertools import permutations
def permutationsOfString(str1):
	
	for i in permutations(str1):
		print(i);
	

#Write a program which contains one function that accepts string and one position from user.Remove the character from that position.
#Input : "ABCDEFGHIJK"  Position : 5
#Output : "ABCDEGHIJK"

def deletePosition(str1, position):
	str2=str1[:position] + str1[position+1:]
	return(str2);
	



#5 Accept string from user and return average of ascii value of characters from that string.
#Input : "ABCDE"
#Output : 67      ((65+66+67+68+69)/5)


def avgAscii(str1):
	
	list1= list(str1)
	sum=0;
	for i in list1:
		sum=sum+ord(i);
		
	avg=(sum/len(list1));
	
	return avg
