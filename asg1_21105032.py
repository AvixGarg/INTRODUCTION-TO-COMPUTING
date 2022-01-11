#Assignment 1
#Answer 1
print("Answer 1")
#Taking input of three numbers from user
num1=float(input("Enter the first number ="))
num2=float(input("Enter the second number ="))
num3=float(input("Enter the third number ="))
sum=num1+num2+num3
#Defining average of three numbers
Average =sum/3
print("Average value  of the numbers is ",Average)



#Answer 2
print("Answer 2")
#To calculate the income tax
income=float(input("Enter your gross total income ="))
standard_deduction=10000
flat_tax_rate=0.20
dependent_deduction=3000
dependents=int(input("Enter the number of dependents ="))
taxable_income=income-standard_deduction-(dependent_deduction*dependents)
print("Your taxable income is =",taxable_income)
tax=taxable_income*flat_tax_rate
if tax<0:
    print("You don't have to pay any income tax.")
else:
    print("Your final Income tax is =", tax)



#Answer 3
print("Answer 3")
#Taking Input from user
SID =int(input("Enter your SID = "))
Name = input("Enter your Name =")
Gender =input("Enter Gender use (\'M'\'F'\'U') = ")
Course_Name =input("Enter course Name =")
CGPA =float(input("Enter your CGPA = "))
Student = [SID,Name,Gender,Course_Name,CGPA]
#student here is defined as list
print("Your values are given as =")
print(Student)



#Answer 4
print("Answer 4")
#Taking input from students of their marks
std1=int(input("Marks of student 1 = "))
std2=int(input("Marks of student 2 = "))
std3=int(input("Marks of student 3 = "))
std4=int(input("Marks of student 4 = "))
std5=int(input("Marks of student 5 = "))
Marks =[std1,std3,std3,std4,std5]
#Making the list of marks obtained by students
print("Marks of students before sorting =",end="")
print(Marks)
Marks.sort()
print("Marks obtained by students after sorting =",end="")
print(Marks)


print("Answer 5")
Color = ['Red','Green','White','Black','Pink','Yellow']
#Making list of Different colors
print("Colors are = ",Color)
#Answer 5(a)
Color.pop(3)
#Removing 4th element from the list of colors
print("Colors after removing 4th element =", Color)
Color=['Red','Green','White','Black','Pink','Yellow']
Color[3:5]=["Purple"]
#Replacing Black and Pink color with Purple in a single line
print("Final colors are =",end="")
print(Color)
