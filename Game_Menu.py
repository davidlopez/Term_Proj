from microbit import *
import random

Diamond = Image("00900:"
              "09090:"
              "90009:"
              "09090:"
              "00900")

SmallDiamond = Image("00000:"
                   "00900:"
                   "09090:"
                   "00900:"
                   "00000")

Skull = Image("09990:"
            "90909:"
            "99999:"
            "09990:"
            "09990")

Square = Image("99999:"
             "90009:"
             "90009:"
             "90009:"
             "99999")
                 
class Coinflip_Game:
    def __init__(self):
        self.diamond = Diamond
        self.smalldiamond = SmallDiamond
        self.skull = Skull
        self.square = Square
        self.choices = [self.skull, self.square]
        self.choice = None
        
    def flip(self):
        display.show(self.diamond)
        sleep(1000)
        display.show(self.smalldiamond)
        sleep(1000)
        display.show(self.diamond)
        sleep(1000)
        display.show(self.smalldiamond)
        sleep(1000)
        self.choice = random.choice(self.choices)

    def play_coinflip(self):
        for i in range(10000000):    
            if button_a.is_pressed():
                self.flip()
                display.show(self.choice)

flipcoin = Coinflip_Game()

player_x = 2
enemy_x = random.randint(0, 4)
enemy_y = 0

def DHM():
    sleep(1000)
    while True:
        global player_x
        global enemy_x
        global enemy_y
        display.clear()
        display.set_pixel(player_x, 4, 9)
        display.set_pixel(enemy_x, enemy_y, 9)
        if enemy_y == 4 and enemy_x == player_x:
                break
        if button_a.was_pressed() and player_x > 0:
            player_x -= 1
        if button_b.was_pressed() and player_x < 4:
            player_x += 1
        enemy_y += 1
        if enemy_y > 4:
            enemy_y = 0
            enemy_x = random.randint(0, 4)
        sleep(250) 
    display.scroll("GAME OVER")
        
Rock = Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000")
             
Paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")
              
Scissors = Image("90009:"
                 "09090:"
                 "00900:"
                 "99099:"
                 "99099")
                 
Lizzard = Image("90000:"
                "90000:"
                "90000:"
                "90000:"
                "99999")

Spock = Image("99999:"
              "90000:"
              "99999:"
              "00009:"
              "99999")

#RPSLS = [rock, paper, scissors, lizzard, spock]

class RPS:
    def __init__(self):
        self.rock = Rock
        self.paper = Paper
        self.scissors = Scissors
        self.lizzard = Lizzard
        self.spock = Spock
        self.choices = [self.rock, self.paper, self.scissors, self.lizzard, self.spock]
        self.choice = None
        
    def choose(self):
        self.choice = random.choice(self.choices)
        
    def play_RPS(self):
        for i in range(10000000):    
            if accelerometer.is_gesture("shake"):
                self.choose()
                display.show(self.choice)
Rocks = RPS()

while True:
    if button_b.is_pressed():
        if button_b.was_pressed():
            DHM()
        break
    if button_a.is_pressed():       
        flipcoin.play_coinflip()
        break
    if accelerometer.is_gesture("shake"):
        Rocks.play_RPS()
        break
        
