import sys
import random
import stdio
import math
import stdarray

input_file = open(sys.argv[1])
Movies = input_file.readlines()
input_file.close()

input_file = open(sys.argv[2])
classRatings = input_file.readlines()
input_file.close()

length_ClassRatings = len(classRatings)
length_Movies = len(Movies)
people_In_Class = len(classRatings) / 2

i=0
# Creates a 2D array to organise ratings by their movies.
sortedRating = []
for movie_index in range(0,length_Movies*2,2):
    # Adds a the 2nd Dimension
    sortedRating.append([])
    for every_student in range(1,length_ClassRatings,2):
        for every_rating in range(0,len(classRatings[every_student]),2):
            sortedRating[i].append(classRatings[every_student][movie_index])
            break
    i += 1

sortedRatingNum = []
for every_movie in range(length_Movies):
    sortedRatingNum.append([])
    for i_rating in range(len(sortedRating[every_movie])):
        if sortedRating[every_movie][i_rating] == '5':
            sortedRatingNum[every_movie].append(5)
        if sortedRating[every_movie][i_rating] == '4':
            sortedRatingNum[every_movie].append(4)
        if sortedRating[every_movie][i_rating] == '3':
            sortedRatingNum[every_movie].append(3)
        if sortedRating[every_movie][i_rating] == '2':
            sortedRatingNum[every_movie].append(2)
        if sortedRating[every_movie][i_rating] == '1':
            sortedRatingNum[every_movie].append(1)
        if sortedRating[every_movie][i_rating] == '0':
            sortedRatingNum[every_movie].append(0)

watched_Movies = []
count = 0
for i in range(length_Movies):
    for j in range(len(sortedRating[i])):
        if sortedRating[i][j] != '0':
            count += 1
    watched_Movies.append(count)
    count = 0

""" Calculate the average number of movies students watched """
def calculate_Average():
    # Count every movie which is rated 1 or above
    rated_Movie = 0
    # Run a loop and check any number bigger than zero.
    # Run through each line
    for i in range(1,len(classRatings),2):
        # Run through the contents of each line
        for j in range(0,len(classRatings[i]),2):
            # Check any value that is not an alphabhet and '0'
            if classRatings[i][j] == '1' or classRatings[i][j] == '2' or classRatings[i][j] == '3' or classRatings[i][j] == '4' or classRatings[i][j] == '5':
                rated_Movie += 1
    # Calculate Average
    average = float(rated_Movie) / float(people_In_Class)
    # Return Average
    return average

def most_Popular_Movies():
    count = 0
    Movies_watched = []
    maxValue = 0
    maxIndex = 0
    for every_movie in range(length_Movies):
        for every_rating in range(len(sortedRating[every_movie])):
            if sortedRating[every_movie][every_rating] != '0':
                count += 1
        Movies_watched.append(count)
        count = 0
    for i in range(5):
        for each_movie in range(len(Movies_watched)):
            if Movies_watched[each_movie] > maxValue:
                maxValue = Movies_watched[each_movie]
                maxIndex = each_movie
        print(Movies[maxIndex].rstrip())
        maxValue = 0
        Movies_watched[maxIndex] = -1

def least_Popular_Movies():
    count = 0
    Movies_watched = []
    maxValue = 0
    maxIndex = 0
    for every_movie in range(length_Movies):
        for every_rating in range(len(sortedRating[every_movie])):
            if sortedRating[every_movie][every_rating] == '0':
                count += 1
        Movies_watched.append(count)
        count = 0
    for i in range(5):
        for each_movie in range(len(Movies_watched)):
            if Movies_watched[each_movie] > maxValue:
                maxValue = Movies_watched[each_movie]
                maxIndex = each_movie
        print(Movies[maxIndex].rstrip())
        maxValue = 0
        Movies_watched[maxIndex] = -1

def highest_Rated_Movies():
    average_Ratings = []
    average = 0
    total = 0
    count = 0
    for each_movie in range(length_Movies):
        for each_rating in range(len(sortedRating[each_movie])):
            if sortedRatingNum[each_movie][each_rating] != 0:
                total += sortedRatingNum[each_movie][each_rating]
                count += 1
        average = total / count
        average_Ratings.append(average)
        total = 0
        count = 0
    maxValue = 0
    maxIndex = 0
    for i in range(5):
        for every_movie in range(len(average_Ratings)):
            if average_Ratings[every_movie] > maxValue:
                if watched_Movies[every_movie] > 10:
                    maxValue = average_Ratings[every_movie]
                    maxIndex = every_movie
                else:
                    average_Ratings[every_movie] = -1
        print(Movies[maxIndex].rstrip())
        maxValue = 0
        average_Ratings[maxIndex] = -1

def least_Rated_Movies():
    average_Ratings = []
    average = 0
    total = 0
    count = 0
    for each_movie in range(length_Movies):
        for each_rating in range(len(sortedRating[each_movie])):
            if sortedRatingNum[each_movie][each_rating] != 0:
                total += sortedRatingNum[each_movie][each_rating]
                count += 1
        average = total / count
        average_Ratings.append(average)
        total = 0
        count = 0
    minValue = 100
    minIndex = 0
    for i in range(5):
        for every_movie in range(len(average_Ratings)):
            if average_Ratings[every_movie] < minValue:
                if watched_Movies[every_movie] > 10:
                    minValue = average_Ratings[every_movie]
                    minIndex = every_movie
                else:
                    average_Ratings[every_movie] = 100
        print(Movies[minIndex].rstrip())
        minValue = 100
        average_Ratings[minIndex] = 100

def most_Contentious_Movies():
    average_Ratings = []
    average = 0
    total = 0
    count = 0
    for each_movie in range(length_Movies):
        for each_rating in range(len(sortedRating[each_movie])):
            if sortedRatingNum[each_movie][each_rating] != 0:
                total += sortedRatingNum[each_movie][each_rating]
                count += 1
        average = total / count
        average_Ratings.append(average)
        total = 0
        count = 0
    mean = 0
    sum = 0
    variance = []
    temp = 0
    varianceT = 0
    counter = 0
    for every_movie in range(length_Movies):
        for every_rating in range(len(sortedRating[every_movie])):
            if sortedRatingNum[every_movie][every_rating] != 0:
                temp += (sortedRatingNum[every_movie][every_rating] - average_Ratings[every_movie])**2
                counter += 1
        varianceT = (1/(counter)) * temp
        variance.append(varianceT)
        varianceT = 0
        counter = 0
        temp = 0
    maxValue = 0
    maxIndex = 0
    for i in range(5):
        for i_movie in range(len(variance)):
            if variance[i_movie] > maxValue:
                if watched_Movies[i_movie] > 10:
                    maxValue = variance[i_movie]
                    maxIndex = i_movie
                else:
                    variance[i_movie] = -1
        print(Movies[maxIndex].rstrip())
        maxValue = 0
        variance[maxIndex] = -1



# All Functions executed
print('The Average Student in CPSC 231 has seen', "%.2f" % calculate_Average(), 'of the', length_Movies, 'movies.\n')
print('The Most Popular Movies Were:')
most_Popular_Movies()
print('')
print('The Least Popular Movies Were:')
least_Popular_Movies()
print('')
print('The Highest Rated Movies Were:')
highest_Rated_Movies()
print('')
print('The Least Rated Movies Were:')
least_Rated_Movies()
print('')
print('The Most Contentious Movies Were:')
most_Contentious_Movies()
print('')

