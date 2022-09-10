'''
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
'''

Solution

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    int_div = (a // b)
    float_div = (a / b)
    
print(int_div)
print(float_div)
