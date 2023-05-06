# Two player game

import random
import time


class Game:
    def __init__(self, player):
        self.player = player
        self.number = 0
        self.dice = [1,2,3,4,5,6]

    def roll(self):
        print(self.player, " is rolling")
        dice_roll = random.choice(self.dice)
        time.sleep(2)
        print("You rolled ", dice_roll)
        return dice_roll
class Person:
    def __init__(self, name, player_number):
        self.name = name
        self.points = 0
        self.player_number = player_number
        self.game = Game(self.name)

    def play(self):
        self.points += self.game.roll()

    def check_winner(self):
        if self.points >= 10:
            return True
        return False


p1 = Person("Swatika", 1)
p2 = Person("Venkat", 2)
toggle = True
while True:
    if toggle:
        p = p1
    else:
        p = p2
    toggle = not(toggle)
    n = input("Want to continue ?\n If you want to quit, you can type 'exit'\n")
    if n != "exit":
        p.play()
        if p.check_winner():
            print("Player : ", p.name, " wins")
            break
    else:
        print("Quitting game\n")
        break
