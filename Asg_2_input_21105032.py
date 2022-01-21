#Question 1
print("\n Answer 1 \n")
input_str = "Python is a case sensitive language"
# Printing the length of the string
print("(a)\tThe length of the given string is : %s" % len(input_str))
#Creating reversed string
reversed_str = input_str[ : : -1 ]
print("(b)\tThe string in reverse would be : %s" % reversed_str)
#Creating a new string
new_str = input_str[10:26]
print("(c)\tThe new string becomes : %s" % new_str)
#Creating a duplicate input string for replaced value
dup_input_str = input_str.replace("a case sensitive", "object oriented")
print("(d)\tThe replaced substring will be : %s" % dup_input_str)
substr = "a"
# Finding the index value of the given substring
indx = input_str.find(substr)
#Printing the index value
if indx == -1:
    print("(e)\tThe given substring was not found in the inputted string")
else:
    print("(e)\tThe first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))
#Removing white spaces
no_white_spaces_str=input_str.replace(" ","")
print("(f)\tThe inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)



#Question 2
print("\n Answer 2 \n")
name='AVI GARG'
SID='21105032'
Dept_name='Electronics and Communication Engineering'
cgpa='9.4'
#using formatting of the strings
print('Hey, %s Here!'%name)
print('My SID is %s'%SID)
print('I am from %s department and my CGPA is %s'%(Dept_name,cgpa))


#Question 3
print( "\n Answer 3 \n")
a=56
b=10
print('a&b=',(a&b))
print('a|b=',(a|b))
print('a^b=',(a^b))
print('a<<2=',a<<2,'and','b<<2=',b<<2)
print('a>>2=',a>>2,'and','b>>4=',b>>4)



#Question 4
print(" \n Answer 4 \n")
number_1 = int(input("Enter the  first number : "))
number_2 = int(input("Enter the second number : "))
number_3 = int(input("Enter the third number : "))
if number_1 >= number_2:
    if number_1 >= number_3:
        print("The greatest number is %s\n" % number_1)
    else:
        print("The greatest number is %s\n" % number_3)
else:
    if number_2 >= number_3:
        print("The greatest number is %s\n" % number_2)
    else:
        print("The greatest number is %s\n" % number_3)





#Question 5
print(" \n Answer 5 \n")
if "name" in input("Enter the string : "):
    print("Yes\n")
else:
    print("No\n")




#Question 6
print("\n Answer 6 \n")
#Sorting the inputted values in a list
while True:
    sides = sorted(input("Enter the dimensions to check whether triangle possible or not : ").split())
    if len(sides) == 3:
        break
    else:
        print("\nA triangle has only 3 sides!\nPlease enter only 3 values")
if int(sides[2]) > (int(sides[0]) + int(sides[1])):
    print("No\n")
else:
    print("Yes\n")



