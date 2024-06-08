import random

words=['programming', 'tiger', 'lamp', 'television', 
       'laptop', 'water', 'mircoscope', 'doctor', 'youtube'
       ,'project']

random_word=random.choice(words)

print('Randon word', random_word)

print('WORD GUESSING GAME')

user_guess=''
chances=5

while chances >0:
    wrong_guess=0
    for character in random_word:
        if character in user_guess:
            print(f"Correct: {character}")
        else:
            wrong_guess+=1
            print('_')

    if wrong_guess == 0:
        print('Correct')
        print(f"Word: {random_word}")
        break
    
    guess = input('Make a guess: ')
    user_guess += guess

    if guess not in random_word:
        chances-=1
        print(f"Wrong. You have more {chances} chances")

        if chances==0:
            print('GAME OVER')




