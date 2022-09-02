'''
Quiz: Assign and Modify Variables
Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) 
have instructions for creating and modifying variables. 
After each comment write a line of code that implements the instruction.

Note that this code uses scientific notation to define large numbers. 
4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

 # The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

# add the rainfall variable to the reservoir_volume variable

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
# decrease reservoir_volume by 5% to account for evaporation

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

# print the new value of the reservoir_volume variable
'''


# decrease the rainfall variable by 10% to account for runoff
rainfall = 5 * 10 ** 6 
runOff = rainfall - (0.1 * rainfall)
print(runOff)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume = 4.445 * 10 ** 8 
SumOfBothVolumes = reservoir_volume + rainfall
print(SumOfBothVolumes)
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
stormwater = reservoir_volume + (0.05 * reservoir_volume)
print(stormwater)
# decrease reservoir_volume by 5% to account for evaporation
everporation = reservoir_volume - (0.05 * reservoir_volume)
print(everporation)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - (2.5 * 10 ** 5)

# print the new value of the reservoir_volume variable
print(reservoir_volume)
# create a file for it. Name it "assign_modify_quiz"
# push the file to github when you're done.