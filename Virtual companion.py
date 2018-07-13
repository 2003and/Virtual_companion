from random import randint
import pygame as pg
from time import sleep
import subprocess
from bcolors import BColors

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
bcolors = BColors()
conf = open('config', 'r')
pg.init()
SIZE = int(conf.readline())
rawf = 'Faces_RAW' + conf.readline() + '.png'
screen = pg.display.set_mode([SIZE, SIZE])
pg.display.set_caption('Virtual companion')


def math():
    ipt1 = int(input('What will the first number be?'))
    ipt2 = int(input('What will the second number be?'))
    op = input('What operation should I do?')
    if op == '+':
        oup = ipt1 + ipt2
    elif op == '-':
        oup = ipt1 - ipt2
    elif op == '*':
        oup = ipt1 * ipt2
    elif op == '/':
        oup = ipt1 / ipt2
    elif op == 'div':
        oup = ipt1 // ipt2
    elif op == 'mod':
        oup = ipt1 % ipt2
    elif op == '**':
        oup = ipt1 ** ipt2
    elif op == '%':
        oup = ipt1 // 100 * ipt2
    else:
        oup = 'none, you gave me an unknown operation'
    print('The answer is', oup)


def gen_pswd():
    pswd = bcolors.OKGREEN + ''
    len_o_pswd = randint(5, 15)
    for i in range(len_o_pswd):
        pswd += characters[randint(0, len(characters) - 1)]
    return pswd + bcolors.OKBLUE


def open_terminal():
    subprocess.call('/usr/bin/gnome-terminal')


def open_tlauncher():
    subprocess.call(executable='/usr/bin/java', args=["-jar", "/home/andrew/.tlauncher/TLauncher.jar"])


class Companion:
    def __init__(self):
        self.raw = pg.image.load(rawf)
        self.faces = []
        for i in range(3):
            f = pg.Surface([20, 20])
            f.blit(self.raw, [-i * 20, 0])
            f = pg.transform.scale(f, [SIZE, SIZE])
            self.faces.append(f)
        self.name = 'Companion'
        icon = self.faces[0]
        pg.display.set_icon(icon)

    def draw_face(self, which='idle'):
        if which == 'idle':
            screen.blit(self.faces[0], [0, 0])
        if which == 'happy':
            screen.blit(self.faces[1], [0, 0])
        elif which == 'sad':
            screen.blit(self.faces[2], [0, 0])
        pg.display.flip()

    def change_name(self, new_name):
        self.name = new_name

    def say(self, string, sec):
        print(self.name + ':', string)
        sleep(sec)


companion = Companion()
companion.draw_face()
print(bcolors.OKBLUE)
companion.say("Hi! I'm your new companion!", 1)
companion.say("You can type me 'quit' to quit", 1)
companion.say("Otherwise it's impossible", 1)
companion.say("""Also, it's HIGHLY recommended to check the 
"always on top" on the companion's face's window""", 1)
while True:
    companion.draw_face()
    cmd = input(companion.name + ': So?\n')
    if cmd == 'Knock knock':
        companion.say("Who's there?", 1)
        companion.say(input() + ' who?', 1)
        input()
        companion.draw_face('happy')
        companion.say('Ha ha! Got me on that one!', 0)
        sleep(3)
    elif cmd == 'quit':
        companion.say('See you later' + bcolors.ENDC, 0)
        exit()
    elif cmd == 'do some math':
        companion.draw_face('happy')
        companion.say('ok!', 1)
        companion.draw_face('idle')
        math()
    elif cmd == 'open terminal':
        companion.draw_face('happy')
        companion.say('Sure!', 1)
        companion.draw_face('idle')
        open_terminal()
    elif cmd == 'open TLauncher':
        companion.draw_face('happy')
        companion.say('Sure!', 1)
        companion.draw_face('idle')
        open_tlauncher()
    elif cmd == 'generate a password':
        companion.draw_face('happy')
        companion.say('Sure!', 1)
        companion.draw_face('idle')
        companion.say('How about ' + gen_pswd() + ' ?', 3)
    elif cmd == 'change name':
        companion.change_name(input(companion.name + ":Ok! What's my new name?"))
    else:
        companion.draw_face('sad')
        companion.say("Sorry! I don't know such command!", 2)
        companion.draw_face('happy')
        companion.say('Maybe, you could try to suggest it?', 2)
