#import statistics
#import random
import sys
#import stdio
import math

# Movies Given
input_file = open(sys.argv[1])
movieList = input_file.readlines()
input_file.close()

# Class Ratings for all movies
input_file = open(sys.argv[2])
classRatings = input_file.readlines()
input_file.close()

# My Ratings for all movies
input_file = open(sys.argv[3])
myRatings = input_file.readlines()
input_file.close()

# Makes an array with the new rating sets
myNewRatings = []
for i_index in range(len(myRatings)):
    for j_index in range(len(myRatings[i_index])):
        if myRatings[i_index][j_index] == '5':
            myNewRatings.append(5)
        if myRatings[i_index][j_index] == '4':
            myNewRatings.append(3)
        if myRatings[i_index][j_index] == '3':
            myNewRatings.append(1)
        if myRatings[i_index][j_index] == '2':
            myNewRatings.append(-3)
        if myRatings[i_index][j_index] == '1':
            myNewRatings.append(-5)
        if myRatings[i_index][j_index] == '0':
            myNewRatings.append(0)

i = 0
peopleNewRatings = []
for every_student in range(1,len(classRatings),2):
    peopleNewRatings.append([])
    for every_rating in range(0,len(classRatings[every_student]),2):
        if classRatings[every_student][every_rating] == '5':
            peopleNewRatings[i].append(5)
        if classRatings[every_student][every_rating] == '4':
            peopleNewRatings[i].append(3)
        if classRatings[every_student][every_rating] == '3':
            peopleNewRatings[i].append(1)
        if classRatings[every_student][every_rating] == '2':
            peopleNewRatings[i].append(-3)
        if classRatings[every_student][every_rating] == '1':
            peopleNewRatings[i].append(-5)
        if classRatings[every_student][every_rating] == '0':
            peopleNewRatings[i].append(0)
    i += 1



# Make a 2D array for the amount of people in class and there ratings compared to your using the scale.
# In that array save comparisons of each ratings.
temp = 0
peoplesRatings = []
for each_student in range(len(peopleNewRatings)):
    peoplesRatings.append([])
    for each_rating in range(len(peopleNewRatings[each_student])):
        temp = peopleNewRatings[each_student][each_rating] * myNewRatings[each_rating]
        peoplesRatings[each_student].append(temp)
    temp = 0

# Make another array which stores the sum of them in an array
temp1 = 0
sum = []
for i_student in range(len(peoplesRatings)):
    for j_rating in range(len(peoplesRatings[i_student])):
        temp1 += peoplesRatings[i_student][j_rating]
    sum.append(temp1)
    temp1 = 0

# Finds the largest value of the sum array
def findMax():
    maxValue = 0
    maxIndex = 0
    for e_student in range(len(sum)):
        if sum[e_student] > maxValue:
            maxValue = sum[e_student]
            maxIndex = e_student
    return maxIndex


# Compare your movies with their maxValue index.
# Go to your 0 ratings index, and then use the same index to check the other persons ratings.
# If its 5 then reccomend, and if not don't.
    # If there are no movies to recommend then move to the next max value (line 109)
print('Hello, ', myRatings[0].rstrip() + '!' + '\n')

print('''From your ratings of our 100 movies,
our CPSC 231 class believes that you
might also like:''')

def reccomendations():
    counter = 0
    maxIndex = findMax()
    for ratings_index in range(len(peopleNewRatings[maxIndex])):
        # Doesn't print a dozen of movie reccomendations. (Optimal 6 reccomendations)
        if myNewRatings[ratings_index] == 0 and peopleNewRatings[maxIndex][ratings_index] == 5 and counter <= 6:
            print('\t' + movieList[ratings_index].rstrip())
            counter += 1
    if counter == 0:
        sum[maxIndex] = 0
        maxIndex = findMax()
        reccomendations()
    # If it's my personal rating counter will be zero so it will find the second largest, if the second largest has no movies to reccomend it will move to the third largest value, so on and so fourth


# Runs the reccomendation process
reccomendations()


