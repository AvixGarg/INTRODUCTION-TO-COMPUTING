#Answer 1
print("Ans 1")
#Defining tower of Hanoi function
def tower_of_hanoi(n , A, B, C):
    step_number=1
    if n==1:
        print (f"Move disk 1 from{A}to{C}")
        return
    tower_of_hanoi(n-1, A, B, C)
    print (f"Move disk {n} from {A} {C}")
    tower_of_hanoi(n-1, B, C, A)
#taking the  number of disk input from the user
no_of_disk=int(input("Enter number of disks in tower of Hanoi:"))
print('''The Disks are numbered starting from top of the tower. 
      Steps to move all disks from Source Tower to Destination Tower is given below''')
#Using the function of tower of hanoi
tower_of_hanoi(no_of_disk,"A","C","B")



#Answer 2
print("Ans 2")

#input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\n Alternate Method \n")
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()


#Answer 3
print("Ans 3")

int1, int2 = map(int,input("Enter 2 numbers: ").split())

quo = int1 // int2
rem = int1 % int2

print(f"The quotient is {quo} and reminder is {rem}")

#part a
print("a. The quotient and reminder is a callable value.")
print(callable(quo))
print(callable(rem))

#part b
if quo == 0:
    print("b. The quotient is zero")
if rem == 0:
    print("b. The reminder is zero")
if quo != 0 and rem != 0:
    print("b. All the values are non zero")

#part c
clist = (quo , rem) + (4, 5, 6)

result = []
for i in range(len(clist)):
    if clist[i] < 5:
        result.append(clist[i])
print(f"c. Filtered out numbers: {result}")

#part d
setresult = set(result)
print("d. Set:",setresult)

#part e
setfrozen = frozenset(setresult)
print("e. Immutable set:",setfrozen)

#part f
print("f. Hash value of the max value from the above set:", hash(max(setfrozen)))



#Answer 4

print("Ans 4")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Avi Garg", 21105032)
print("Object created")

#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting object
del student1



#Answer 5
print("Ans 5")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

#part a, updating salary
employee_1.salary = 70000
print(f"a. The updated salary of the employee {employee_1.name} is {employee_1.salary}")

#part b, deleting a record
print("b. ", end='')
del employee_3



#Answer 6
print("Ans 6")

# definig principle of game
def samesense(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1="George"
player2="Barbie"
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by George:"))
word_player2=str(input(f"Enter Word by Barbie:"))
#using samesense function
result=samesense(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of Barbie and George is REAL")
elif result==False:
    print(f"\nFriendship of Barbie and George is FAKE")
    
