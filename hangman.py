import random
from hangman_art import logo,stages
word_list = ["aardvark", "baboon", "camel"]

print(logo)
chosen_word = random.choice(word_list)
blanked_list = []

blanked_list = ['_']*len(chosen_word)

print(blanked_list)
end_of_game = False


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = len(stages)

while not end_of_game and lives != 0:

    guess = input('Enter a Letter').lower()

    for i,letter in enumerate(chosen_word):
        if letter == guess:
            blanked_list[i] = letter
        else:

            # print('Wrong')
            pass

    if guess not in blanked_list:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print('You lose!!!')

    print(blanked_list)

    if ''.join(blanked_list) == chosen_word:
        end_of_game = True
        print('You passed!!!')




