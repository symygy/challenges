from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'

matched_letters = []

class Hangman(object):
    def __init__(self, chosenWord):
        self.chosenWord = chosenWord
        self.wrong_letters_counter = 0
        self.wrong_letters = []

    def drawPlaceholders(self):
        self.matched_letters_counter = 0
        for i in self.chosenWord.lower():
            if i == ' ':
                print(' ', end=' ')
            elif i in matched_letters:
                self.matched_letters_counter += 1
                print(i.upper(), end=' ')
            else:
                print(PLACEHOLDER, end=' ')
        print('\n\n')

    def inputALetter(self):
        print("\n")
        letter = input("Choose a letter: ")
        return letter

    def checkLetter(self, letter):
        if letter in self.chosenWord.lower():
            matched_letters.append(letter)
            self.drawPlaceholders()
        else:
            self.wrong_letters_counter += 1
            print("No letter: " + letter + " in searched word.")
            self.wrong_letters.append(letter)
            print(self.wrong_letters)
            self.drawPlaceholders()


    def checkIfWin(self, chosenWord):
        if self.matched_letters_counter == len(chosenWord.replace(" ", "")):
            print(" CONGRATS. YOU WON !!!")
            return True

        elif len(self.wrong_letters) == 6:
            print("GAME OVER")
            print("Searched movie title: " + self.chosenWord)
            sys.exit()

        else:
            print(HANG_GRAPHICS[self.wrong_letters_counter])
            return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    #print(word)

    game = Hangman(word)
    game.drawPlaceholders()

    while game.checkIfWin(word) == False:
        letter = game.inputALetter()
        check = game.checkLetter(letter)


    # init / call program
