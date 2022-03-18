print('Welcome to CodeWithVed_Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What is your Favourite programming language?')
    if answer.lower() == 'C++':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2: Do you follow any Youtuber? ')
    if answer.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: What is the name of your favourite Youtube Channal for learning C++?')
    if answer.lower() == 'CodeWithVed':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('Thanks For Attempting ,Bye!')