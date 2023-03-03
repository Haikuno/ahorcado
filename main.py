import random
import math
from states import states
from words import words

class Game():
    def __init__(self) -> None:
        self.state = 0
        self.word = random.choice(words)
        self.visible_word = "_ " * (len(self.word)-1) + "_"
        self.guessed_letters = []

    def is_valid_letter(self, c) -> bool():
        try:
            if c.upper() in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" and not c.upper() in self.guessed_letters:
                self.guessed_letters.append(c.upper())
                return True
        except:
            ...

        return False

    def ask_for_letter(self) -> str:
        c = input("Letra a probar : ")

        try:
            if len(c) > 1:
                if c.upper() == self.word:
                    self.visible_word = self.word
                    return self.word
                else:
                    return c
        except:
            ...

        while not self.is_valid_letter(c):
            c = input("Letra invalida, intenta de nuevo : ")

        return c.upper()

    def try_letter(self, letter) -> None:
        if letter in self.word:
            indices = []
            visible_word_list = list(self.visible_word)
            for idx, value in enumerate(self.word):
                if value == letter:
                    indices.append(idx)
            for i in indices:
                visible_word_list[i*2] = letter
                self.visible_word = ''.join(visible_word_list)

        else:
            self.state += 1

    def show_guessed_letters(self) -> None:
        str_guessed_letters = ""
        for letter in self.guessed_letters:
            str_guessed_letters += letter + " "
        print("Letras ya probadas : " + str_guessed_letters)

    def show_state(self) -> None:
        print(states[self.state])
        print(self.visible_word)

    def win(self) -> None:
        input("Ganaste")

    def lose(self) -> None:
        input("Perdiste, la palabra era " + self.word)

def main():
    game = Game()
    while True:

        if game.visible_word == game.word:
            game.show_state()
            game.win()
            exit()
        if game.state == len(states) - 1:
            game.show_state()
            game.lose()
            exit()

        game.show_state()
        game.show_guessed_letters()
        letter = game.ask_for_letter()
        if letter != game.word:
            game.try_letter(letter)

if __name__ == "__main__":
    main()

