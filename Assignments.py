'''
 ASSIGNMENT

Quiz: String Methods Coding Practice
Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling. 
Remember, \n is a special sequence of characters that causes a line break (a new line).

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\n
If you can trust yourself when all men doubt you,\n  
But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n 
Or being lied about, don’t deal in lies,\nOr being hated, 
don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
Use the code editor below to answer the following questions about verse and use 
Test Run to check your output in the quiz at the bottom of this page.

What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?
You will need to refer to Python's string methods documentation.

verse = "If you can keep your head when all about you\n
Are losing theirs and blaming it on you,\n
If you can trust yourself when all men doubt you,\n  
But make allowance for their doubting too;\n
If you can wait and not be tired by waiting,\n  
Or being lied about, don’t deal in lies,\n
Or being hated, don’t give way to hating,\n 
And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!



QUESTION 2 OF 2
Please match the correct response to each of the following questions.





10, 8, 64, 362, 62, 370, 3, 368, 186, 65





OBJECTIVE

CODE

What is the length of the string variable verse?

What is the index of the first occurrence of the word 'and' in verse?

What is the index of the last occurrence of the word 'you' in verse?

What is the count of occurrences of the word 'you' in the verse?
'''



verse ='''If you can keep your head when all about you
Are losing theirs and blaming it on you,
If you can trust yourself when all men doubt you,
But make allowance for their doubting too;
If you can wait and not be tired by waiting,
Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
And yet don’t look too good, nor talk too wise:'''

print(verse)

# What is the length of the string variable verse?
print(len(verse))

# What is the index of the first occurrence of the word 'and' in verse?
IndexOfFirstAnd = verse.index('and')
print(IndexOfFirstAnd)

# What is the index of the last occurrence of the word 'you' in verse?
indexOfLastYou = verse.rindex('you')
print(indexOfLastYou)

# What is the count of occurrences of the word 'you' in the verse?
print(verse.count('you'))


# QUESTION 2 OF 2
# Please match the correct response to each of the following questions.

print('The lenth of the string varibale verse is: 354')

print('The index of the first occurrence of the word "and" is: 63')

print('The index of the last of occurrence of the word "you" is: 182')

print('The count of occurrence of the word "you" is: 8')