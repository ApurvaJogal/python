from MarvellousString import *

print("1.Reverse of string : ");
str1=input("Enter the string\n ");
str2= reverseString(str1);
print(str2);


print("2.Find number of words in the string : ");
str3=input("Enter the string\n");
wordCount = numberofWords(str3);
print("word count is :",wordCount);

print("3.Find permutation of the given string :");
str4=input("Enter the string: \n");
permutationsOfString(str4);


print("4.Delete character from position:");
str5=input("Enter the string \n");
pos= input("Enter position at which character is to remove : ");
str6=deletePosition(str5,pos);
print("New String is : ",str6);

print("5.Average pf ASCII values of characters in the string : ");
str7=input("Enter the string \n");
avg=avgAscii(str7);
print("Average is :", avg);

