# print("Hello World")
'''
if 5 > 2:
    print("5 is greater than 2")
'''



# x = str(5)
# y = "James"
# print(x)
# print(y)
# print(type(x))

# numStudent = 657
# daysAttn = 78
# numStudent = 567 // 45
# print(numStudent)

'''
My electricity bills for the last three months have been $23, $32 and $64.
What is the average monthly electricity bill over the three month period? 
Write an expression to calculate the mean,
and use print() to view the result.
'''
# firstMonth = 23
# secondMonth = 32
# thirdMonth = 64
# avgAmount = ((firstMonth + secondMonth + thirdMonth) / 3)
# print(avgAmount)

'''
In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. 
One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. 
Tiles come in packages of 6.
How many tiles are needed?
You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
'''
# numTiles = (9 * 7) + (5 * 7)
# print(numTiles)

# packOfTiles = (17 * 6)
# numOfTilesLeft = packOfTiles - numTiles
# print(numOfTilesLeft)

'''
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
'''
# sf_population = 864816
# sf_area = 231.89
# rio_population = 6453682
# rio_area = 486.5

# san_francisco_pop_density = sf_population / sf_area
# rio_de_janeiro_pop_density = rio_population / rio_area
# print(san_francisco_pop_density)
# print(rio_de_janeiro_pop_density)

# if (san_francisco_pop_density > rio_de_janeiro_pop_density):
#     print(True)
# else:
#     print(False)

'''
>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"
'''
# Simon's skateboard is in the garage

# myString = 'Simon\'s skateboard is in the garage'
# print(myString)


# string1 = 'Hello'
# string2 = 'James'
# string3 = 'Jam'

# print(string1 + ' ' + string2)

# print(string2 * 5)
# print(len(string2))

# print(string2[0:4])

# print(len(string2) / len(string3))


# TODO: Fix this string!
# ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
# print(ford_quote)

'''
Quiz: Write a Server Log Message
In this programming quiz, you’re going to use what you’ve learned about strings
to write a logging message for a server.

You’ll be provided with example data for a user, the time of their visit and the site they accessed. 
You should use the variables provided and the techniques you’ve learned to print a
log message like this one (with the username, url, and timestamp 
replaced with values from the appropriate variables):

Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
'''


username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

# print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')


'''
Quiz: len()
Use string concatenation and the len() function to find the length of a certain movie star's actual full name. 
Store that length in the name_length variable. Don't forget that there are spaces in between the different parts 
of a name!
'''
'''
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = #todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit
'''
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
white_space = 2

driving_license_character_limit = 28

nameLength = len(given_name + middle_names + family_name) + white_space
print(nameLength)
print(nameLength <= driving_license_character_limit)