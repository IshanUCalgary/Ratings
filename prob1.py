import sys
import random
import stdio

input_file = open(sys.argv[1])
docLines = input_file.readlines()
input_file.close()

output_file = open('ratings.txt', 'w')

numLines = len(docLines)

""" Introduction, questions """
NAME = input("What's is your name? ")
output_file.write(NAME)
output_file.write('\n')
print('')
print('''Hi,''', NAME+'!', '''
Please tell us your favourite movies using the following scale:
    0 = Never seen it.
    1 = It was terrible!
    2 = Didn’t like it.
    3 = It was OK.
    4 = Liked it.
    5 = It was awesome!
''')

for i in range(numLines):
    line_of_text = docLines[i]
    ratings = input(line_of_text.strip()+'? ')
    output_file.write(ratings+', ')
else:
    print('')
    print('''Thank you!,''', NAME, '''
Your ratings were saved to
ratings.txt
        ''')
