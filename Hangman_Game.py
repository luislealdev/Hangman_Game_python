import random
from Hangman_Words import word_list
from Hangman_Art import logo, stages

chosen_word = random.choice(word_list)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

print(logo)

display = []
for letter in chosen_word:
    display.append('_')

hasFinished = False

while not hasFinished:
    print('------------')
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives-=1
    elif guess in display:
        print("This letter is already in the word")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
    
    print(stages[lives])
    print(display)

    if '_' not in display:
        hasFinished = True
        print("You won!")
    elif lives==0:
        hasFinished = True
        print("You lost :(")
