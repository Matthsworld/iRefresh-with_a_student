'''
Exercise;
1. Create a variable named carname and assign the value Volvo to it.

2. Create a variable named x and assign the value 50 to it.

3. Display the sum of 5 + 10, using two variables: x and y:
                  
 = 

y = 10
print(x 
 y)

4. Create a variable called z, assign x + y to it, and display the result:

x = 5
y = 10
 = x + y
print(
)

5. Remove the illegal characters in the variable name:
                  2my-first_name = "John"

6. Insert the correct syntax to assign the same value to all three variables in one code line
x 
 y 
 z 
 "Orange"

7.  Insert the correct keyword to make the variable x belong to the global scope:
def myfunc():
  
 x
  x = "fantastic"
'''


#SOLUTIONS
#1. Create a variable named carname and assign the value Volvo to it.
carName = 'Volvo'

#2. Create a variable named x and assign the value 50 to it.
x = 50

#3. Display the sum of 5 + 10, using two variables: x and y:
x = 5
y = 10
print(x + y)

#4. Create a variable called z, assign x + y to it, and display the result:
x = 5
y = 10
z = x + y
print(z)

#5. Remove the illegal characters in the variable name:
my_first_name = "John"

#6. Insert the correct syntax to assign the same value to all three variables in one code line
x = y = z = "Orange"

#7.  Insert the correct keyword to make the variable x belong to the global scope:
def myfunc():
  
 global x
 x = "fantastic"