'''
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

Solution

if __name__ == '__main__':
    a = int(input()) #1 <= a <= 10e10
    b = int(input()) #1 <= b <= 10e10

    add_ab = (a + b)
    subtr_ab = (a - b)
    mul_ab = (a * b)
    
print(add_ab)
print(subtr_ab)
print(mul_ab)
