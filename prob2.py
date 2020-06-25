import sys
import random
import stdio

input_file = open(sys.argv[1])
docMoviesLines = input_file.readlines()
input_file.close()

input_file = open(sys.argv[2])
docRatingsLines = input_file.readlines()
input_file.close()

movies = len(docMoviesLines)
numRatingsLine = len(docRatingsLines)

NAME = docRatingsLines[0]
print('Hi!', NAME)

ratings = docRatingsLines[1]
ratingsN = []
for i in range(len(ratings)):
    if ratings[i] != ',' and ratings[i] != ' ':
        ratingsN += ratings[i]

counter = 0
for i in range(len(ratingsN)):
    if ratingsN[i] == '0':
        counter += 1
else:
    print("It looks like you've seen", movies-counter, 'of the', movies, 'movies.')
    print('')

print('Your favorite movies were:')
for i in range(len(ratingsN)):
    if ratingsN[i] == '5':
        print(docMoviesLines[i].strip())
else:
    print('')

print('Your least favorite movies were:')
for i in range(len(ratingsN)):
    if ratingsN[i] == '1':
        print(docMoviesLines[i].strip())
else:
    print('')

