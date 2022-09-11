#!/usr/bin/python
"""This is a terminal game for the ITK LAN GameJam"""
import keyboard

from time import sleep
import keyboard
import os
import sys


screen_height = 30
screen_width = 80


message = "Welcome to the ITK LAN!"

current_room = "kistan"
def new_smash_world():
    world = [
        [
            " " for _ in range(screen_height)
        ] for _ in range(screen_width)
    ]
    for x in range(30):
        world[x+25][10] += "‾"
    for x in range(50):
        world[x+15][14] += "‾"
    for x in range(10):
        world[x+13][6] += "‾"
        world[x+28][6] += "‾"
        world[x+43][6] += "‾"
        world[x+58][6] += "‾"
        world[x+62][18] += "‾"
        world[x+7][18] += "‾"
    return world
world = {
    "kistan": [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "|", "|", "|", "|"],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", "A", "O", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", "S", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", "M", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", "A", " "],
        [" ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", "S", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", "H", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "A", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "_", " ", " ", " "],
        [" ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", "|", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "|", "|", "|", "|"],
        [" ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", " ", " ", "_", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", "|", "|", "_", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "#", "#", " ", " ", " ", "_", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "A", "O", " ", " ", " ", "|", "|", "|", "|", "|", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " ", " ", "_", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", "|", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "\\"," ", "<", " ", "/", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "\\"," ", "/", " ", "_", "_", " ", " ", " ", " ", " ", "|", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "\\"," ", " ", " ", "/", "_", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", " ", "(", " ", "_", " ", " ", " ", " ", " ", " ", "#", "M", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", "_", "_", "_", "_", " ", " ", " ", " ", " ", " ", "#", "A", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", " ", ")", " ", "_", " ", " ", " ", " ", " ", " ", "#", "G", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "\\","/", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", "I", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "_", " ", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", "C", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "_", "_", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", "_", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "/", "\\","|", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", "|", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "\\"," ", " ", " ", " ", "_", "_", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "|", "_", "|", "|", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "_", "_", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", " ", " ", " ", "_", " ", " ", " ", " ", " ", "|", "#", "#", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "\\"," ", "/", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "(", " ", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "_", "_", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", ",", "|", "`", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", "|", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", ",", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", " ", "_", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", "\\"," ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "|", " ", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ],
    "smash": new_smash_world(),
    "mtg": [[]],
}
npcs = [
    ["Silvia", 46, 5, 4, "Mooncakes will be ready soon :)", "Kanelbullarna är 5 Kronor."],
    ["Dante", 11, 22, 4, "ME ME ME!", "Sudo make me a sandwich!", "The position of X senator will soon be open..."],
    ["Froosty", 22, 14, 4, "We're gonna do league 5vs5 hopefully in like 35ish.", "Where is the root?"],
]
x = 21
y = 5
old_x = 0
old_y = 0
world["kistan"][x][y] += "A"
world["kistan"][x][y+1] += "@"

# smash vars
jumping = 0
falling = 0
knockback = 0
hit = 0
facing_left = False
ejumping = 0
efalling = 0
eknockback = 0
ehit = False
efacing_left = False
eescape = 0
ex = 0
ey = 0

# magic vars
mtg_focus = [4, 0]
mtg_health = 9
mtg_mana = 0
mtg_hand = []
mtg_lands = []
mtg_board = []
emtg_board = []
emtg_lands = []
emtg_health = 6
emtg_mana = 0

def display():
    """Display the current frame"""
    horizontal = "|"
    for _ in range(screen_width):
        horizontal += "_"
    horizontal += "|\n"

    output = "|"
    for _ in range(screen_width):
        output += "‾"
    output += "|\n"

    # draw message
    output += "| "
    output += message
    for _ in range(len(message), screen_width-1):
        output += " "
    output += "|\n"
    output += horizontal

    # draw world view
    i, j = 0, 0
    for i in range(screen_height):
        output += "|"
        for j in range(screen_width):
            output += world[current_room][j][screen_height-i-1][-1]
            j += 1
        output += "|\n"
        i += 1
    output += horizontal
    os.system('cls' if os.name == 'nt' else 'clear')
    print(output)

def no_collision(x, y):
    return world[current_room][x][y][-1] == " " or len(world[current_room][x][y]) > 1 and world[current_room][x][y][-2] == " " and world[current_room][x][y][-1] == "@"

def enter_kistan():
    global x, y, old_x, old_y, jumping, falling, current_room, message
    current_room = "kistan"
    x, y = old_x, old_y
    message = "Welcome to the ITK LAN"

def enter_smash():
    global x, y, ex, ey, old_x, old_y, jumping, falling, ejumping, efalling, current_room
    world["smash"] = new_smash_world()
    current_room = "smash"
    old_x, old_y = x,     x, y = 13, 10
    ex, ey = 67, 10
    jumping, falling, ejumping, efalling = 0, 0, 0, 0
    world["smash"][x][y] += "A"
    world["smash"][x][y+1] += "@"
    world["smash"][ex][ey] += "A"
    world["smash"][ex][ey+1] += "e"

def smash_end(win):
    ko = [
        "              .-'''-.        ___   ",
        "             '   _    \   .'/   \  ",
        "     .     /   /` '.   \ / /     \ ",
        "   .'|    .   |     \  ' | |     | ",
        " .'  |    |   '      |  '| |     | ",
        "<    |    \    \     / / |/`.   .' ",
        " |   | ____`.   ` ..' /   `.|   |  ",
        " |   | \ .'   '-...-'`     ||___|  ",
        " |   |/  .                 |/___/  ",
        " |    /\  \                .'.--.  ",
        " |   |  \  \              | |    | ",
        " '    \  \  \             \_\    / ",
        "'------'  '---'            `''--'  ",
        "                                   ",
        "             You win!              " if win else
        "            You loose!             ",
        "           Play again?             ",
        "              [Y/N]                ",
    ]

    world["smash"] = [[" " for _ in range(screen_height)] for _ in range(screen_width)]
    display()
    for i in range(len(ko)):
        for j in range(len(ko[i])):
            world["smash"][20+j][6+len(ko)-i] += ko[i][j]
        sleep(0.1)
        display()
    while True:
        if keyboard.is_pressed("y"):
            enter_smash()
            return
        if keyboard.is_pressed("n"):
            enter_kistan()
            return

def smash_ai_move():
    global ex, ey, ejumping, efalling, eescape, current_room, efacing_left, ehit, knockback, eknockback
    want_left = False
    want_fall = False
    want_jump = False
    want_punch = False
    if eescape > 0:
        eescape -= 1
        want_left = x > ex
        want_jump = y <= ey
    else:
        want_left = x < ex
        want_jump = y > ey
        want_fall = y < ey
        want_punch = (y == ey or y+1 == ey) and max(x, ex) - min(x, ex) < 2
    efacing_left = want_left
    if eknockback == 0:
        if (
            ey < screen_height-1 and ejumping == 0 and not no_collision(ex, ey-1)
            and (
                want_jump
                or want_left and ex in [25, 15, 13, 28, 43, 58, 62, 7]
                or not want_left and ex in [54, 64, 22, 37, 52, 67, 71, 16]
                )
            ):
            ejumping = 5
        if ey > 0 and not no_collision(ex, ey-1) and want_fall:
            efalling = 1
        if ex < screen_width-1 and no_collision(ex+1, ey) and not want_left:
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex += 1
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"
            efacing_left = False
        if ex > 0 and no_collision(ex-1, ey) and want_left:
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex -= 1
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"
            efacing_left = True
    else:
        if eknockback == 1 and ex < screen_width-1:
            eknockback = 0
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex += 1
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"
        elif eknockback > 1 and ex < screen_width-2:
            eknockback -= 2
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex += 2
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"
        if eknockback == -1 and ex > 0:
            eknockback = 0
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex -= 1
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"
        elif eknockback < -1 and ex > 1:
            eknockback += 2
            world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
            world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
            ex -= 1
            world["smash"][ex][ey] += "A"
            world["smash"][ex][ey+1] += "e"

    # execute falling
    if ejumping == 0 and (efalling > 0 or (ey > 0 and no_collision(ex, ey-1))):
        efalling -= 1
        world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
        world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
        ey -= 1
        world["smash"][ex][ey] += "A"
        world["smash"][ex][ey+1] += "e"
    # execute jump
    if ejumping >= 2 or ejumping == 1:
        if ejumping == 2:
            ejumping = 1.5
        else:
            ejumping -= 1
        world["smash"][ex][ey] = world["smash"][ex][ey][:-1]
        world["smash"][ex][ey+1] = world["smash"][ex][ey+1][:-1]
        ey += 1
        world["smash"][ex][ey] += "A"
        world["smash"][ex][ey+1] += "e"
    elif ejumping == 1.5:
        ejumping = 1

    # punching
    if want_punch and ehit == 0:
        ehit = 3
        if efacing_left and ex > 1:
            if world["smash"][ex-1][ey+1][-1] in ["A", "@"]:
                knockback = -9
                eescape = 4
            elif world["smash"][ex-2][ey+1][-1] in ["A", "@"]:
                knockback = -19
            world["smash"][ex-1][ey+1] += "_"
        elif not efacing_left and ex < screen_width-2:
            if world["smash"][ex+1][ey+1][-1] in ["A", "@"]:
                knockback = 9
                eescape = 4
            elif world["smash"][ex+2][ey+1][-1] in ["A", "@"]:
                knockback = 19
            world["smash"][ex+1][ey+1] += "_"
    elif ehit > 0:
        ehit -= 1

def format_cards(cards):
    output = ["", "", "", "", "", ""]
    for card in cards:
        if not card[3]:
            output[0] += " .------."
            output[1] += f" | |()|{card[0]}|" if card[4] else f" | |/\|{card[0]}|"
            output[2] += " | |()| |" if card[4] else " | |\/| |"
            output[3] += " | ~~~~ |"
            output[4] += f" | ~ {card[1]}/{card[2]}|"
            output[5] += " `------'"
        else:
            output[0] += "          "
            output[1] += ".--------."
            output[2] += f"| {card[0]}  ~   |"
            output[3] += "| () ~   |" if card[4] else "| /\ ~   |"
            output[4] += "| () ~ ~ |" if card[4] else "| \/ ~ ~ |"
            output[5] += "`--------'"
    return output

def render_mtg():
    world = [
        [
            " " for _ in range(screen_height)
        ] for _ in range(screen_width)
    ]
    images = [
        [65, 26, [f"HP: {emtg_health}"]],
        [65, 25, [f"Mana: {emtg_mana}"]],
        [20, 23, format_cards(emtg_lands)],
        [33, 17, format_cards(emtg_board)],
        [33, 10, format_cards(mtg_board)],
        [12, 4, format_cards(mtg_lands)],
        [25, 0, format_cards(mtg_hand)],
        [65, 1, [f"HP: {mtg_health}"]],
        [65, 0, [f"Mana: {mtg_mana}"]],
    ]
    for image in images:
        for i in range(len(image[2])):
            for j in range(len(image[2][i])):
                world[image[0]+j][image[1]+len(image[2])-i] += image[2][i][j]
    return world

def enter_mtg():
    global x, y, old_x, old_y, current_room
    global emtg_board, emtg_lands, emtg_health, mtg_mana, mtg_health, mtg_hand, mtg_board, mtg_lands, emtg_mana
    old_x, old_y = x, y
    if emtg_health == 0:
        emtg_health = 9
    mtg_health = 9
    mtg_mana = 0
    mtg_hand = [
        [1, " ", " ", False, True, "Mind Bomb", "Mind Bomb deals 3 damage to each player."],
        [1, " ", " ", False, False, "Mind Bomb", "Mind Bomb deals 3 damage to each player."],
        [4, 3, 3, False, False, "Micromancer", "Wait, are these cards missing some text?"],
    ]
    mtg_lands = [
        ["*", " ", " ", False, False, "Plains", "Tap for one white mana"],
        ["*", " ", " ", False, False, "Plains", "Tap for one white mana"],
        ["*", " ", " ", False, False, "Plains", "Tap for one white mana"],
        ["*", " ", " ", False, False, "Plains", "Tap for one white mana"],
        ["O", " ", " ", False, False, "Island", "Tap for one blue mana"],
        ["O", " ", " ", False, False, "Island", "Tap for one blue mana"],
    ]
    mtg_board = [
        [3, 2, 2, False, False, "Phyrexian Rager", "When this card enters the battlefield, draw a card."],
    ]
    emtg_board = [
        [3, 2, 2, True, False, "Phyrexian Rager", "When this card enters the battlefield, draw a card."],
    ]
    emtg_lands = [
        ["B", " ", " ", False, False, "Swamp", "Tap for one black mana"],
        ["B", " ", " ", False, False, "Swamp", "Tap for one black mana"],
        ["B", " ", " ", True, False, "Swamp", "Tap for one black mana"],
        ["B", " ", " ", True, False, "Swamp", "Tap for one black mana"],
    ]
    world["mtg"] = render_mtg()
    current_room = "mtg"

def mtg_end():
    ko = [
        " _____  _____ ",
        "|  __ \|  __ \\",
        "| |  \/| |  \/",
        "| | __ | | __ ",
        "| |_\ \| |_\ \\",
        "\____/ \____/ ",
        "              ",
        "   You win!   ",
        " Play again?  ",
        "    [Y/N]     ",
    ]

    world["mtg"] = [[" " for _ in range(screen_height)] for _ in range(screen_width)]
    display()
    for i in range(len(ko)):
        for j in range(len(ko[i])):
            world["mtg"][30+j][10+len(ko)-i] += ko[i][j]
        sleep(0.1)
        display()
    while True:
        if keyboard.is_pressed("y"):
            enter_mtg()
            return
        if keyboard.is_pressed("n"):
            enter_kistan()
            return


def main_loop():
    global x, y, old_x, old_y, jumping, falling, current_room, facing_left, hit, eknockback, knockback, message
    global current_room, emtg_board, emtg_lands, emtg_health, mtg_mana, mtg_health, mtg_hand, mtg_board, mtg_lands, emtg_mana, mtg_focus
    while True:
        try:
            if keyboard.is_pressed("q"):
                sys.exit()

            if current_room == "kistan":
                if y < screen_height-1 and world["kistan"][x][y+1] == "_@" and y > 20 and keyboard.is_pressed("up"):
                    enter_smash()
                    continue

                if y < screen_height-1 and world["kistan"][x][y+1] == "#@" and x > 40 and keyboard.is_pressed("up"):
                    enter_mtg()
                    continue

                # movement
                if keyboard.is_pressed("up") and y < screen_height-2 and no_collision(x, y+1):
                    world["kistan"][x][y] = world["kistan"][x][y][:-1]
                    world["kistan"][x][y+1] = world["kistan"][x][y+1][:-1]
                    y += 1
                    world["kistan"][x][y] += "A"
                    world["kistan"][x][y+1] += "@"
                if keyboard.is_pressed("down") and y > 0 and no_collision(x, y-1):
                    world["kistan"][x][y] = world["kistan"][x][y][:-1]
                    world["kistan"][x][y+1] = world["kistan"][x][y+1][:-1]
                    y -= 1
                    world["kistan"][x][y] += "A"
                    world["kistan"][x][y+1] += "@"
                if keyboard.is_pressed("right") and x < screen_width-1 and no_collision(x+1, y):
                    world["kistan"][x][y] = world["kistan"][x][y][:-1]
                    world["kistan"][x][y+1] = world["kistan"][x][y+1][:-1]
                    x += 1
                    world["kistan"][x][y] += "A"
                    world["kistan"][x][y+1] += "@"
                if keyboard.is_pressed("left") and x > 0 and no_collision(x-1, y):
                    world["kistan"][x][y] = world["kistan"][x][y][:-1]
                    world["kistan"][x][y+1] = world["kistan"][x][y+1][:-1]
                    x -= 1
                    world["kistan"][x][y] += "A"
                    world["kistan"][x][y+1] += "@"
                for npc in npcs:
                    if max(x, npc[1]) - min(x, npc[1]) < 3 and max(y, npc[2]) - min(y, npc[2]) < 3:
                        if npc[0] not in message:
                            message = f"{npc[0]}: {npc[npc[3]]}"
                            npc[3] = max((npc[3] + 1) % len(npc), 4)

            if current_room == "mtg":
                if emtg_health <= 0:
                    mtg_end()
                    continue
                key = keyboard.read_event().name
                mtg_grid = [emtg_lands, emtg_board, mtg_board, mtg_lands, mtg_hand]
                # focusing
                if key == "up":
                    mtg_focus[0] -= 1
                if key == "down":
                    mtg_focus[0] += 1
                if key == "right":
                    mtg_focus[1] += 1
                if key == "left":
                    mtg_focus[1] -= 1
                if mtg_focus[0] < 0:
                    mtg_focus [0] = 0
                if mtg_focus[0] > 4:
                    mtg_focus [0] = 4
                while len(mtg_grid[mtg_focus[0]]) == 0:
                    mtg_focus[0] += 1
                if mtg_focus[1] < 0:
                    mtg_focus [1] = 0
                if mtg_focus[1] >= len(mtg_grid[mtg_focus[0]]):
                    mtg_focus [1] = len(mtg_grid[mtg_focus[0]])-1
                for list in mtg_grid:
                    for card in list:
                        card[4] = False
                card = mtg_grid[mtg_focus[0]][mtg_focus[1]]
                card[4] = True
                message = f"{mtg_grid[mtg_focus[0]][mtg_focus[1]][5]}: {mtg_grid[mtg_focus[0]][mtg_focus[1]][6]}"
                # interacting with cards
                if key == "space":
                    if mtg_focus[0] == 4 and mtg_mana >= card[0]:
                        mtg_mana -= card[0]
                        if card[0] == 4:
                            mtg_board.append(card)
                        elif card[0] == 1:
                            mtg_health -=3
                            emtg_health -= 3
                        mtg_hand.pop(mtg_focus[1])
                    if mtg_focus[0] == 3 and not card[3]:
                        card[3] = True
                        mtg_mana += 1
                    if mtg_focus[0] == 2 and not card[3]:
                        card[3] = True
                        emtg_health -= card[1]
                    
                world["mtg"] = render_mtg()
                sleep(0.3)

            if current_room == "smash":
                # remove hit animation
                if hit == 3:
                    if facing_left:
                        world["smash"][x-1][y+1] = world["smash"][x-1][y+1][:-1]
                    else:
                        world["smash"][x+1][y+1] = world["smash"][x+1][y+1][:-1]
                if ehit == 3:
                    if efacing_left:
                        world["smash"][ex-1][ey+1] = world["smash"][ex-1][ey+1][:-1]
                    else:
                        world["smash"][ex+1][ey+1] = world["smash"][ex+1][ey+1][:-1]
                        
                smash_ai_move()
                if y == 0:
                    smash_end(False)
                    continue
                if ey == 0:
                    smash_end(True)
                    continue
                if knockback == 0:
                    if keyboard.is_pressed("up") and y < screen_height-1 and jumping == 0 and not no_collision(x, y-1):
                        jumping = 5
                    if keyboard.is_pressed("down") and y > 0 and not no_collision(x, y-1):
                        falling = 1
                    if keyboard.is_pressed("right"):
                        facing_left = False
                        if x < screen_width-1 and no_collision(x+1, y):
                            world["smash"][x][y] = world["smash"][x][y][:-1]
                            world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                            x += 1
                            world["smash"][x][y] += "A"
                            world["smash"][x][y+1] += "@"
                    if keyboard.is_pressed("left"):
                        facing_left = True
                        if x > 0 and no_collision(x-1, y):
                            world["smash"][x][y] = world["smash"][x][y][:-1]
                            world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                            x -= 1
                            world["smash"][x][y] += "A"
                            world["smash"][x][y+1] += "@"
                else:
                    if knockback == 1 and x < screen_width-1:
                        knockback = 0
                        world["smash"][x][y] = world["smash"][x][y][:-1]
                        world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                        x += 1
                        world["smash"][x][y] += "A"
                        world["smash"][x][y+1] += "@"
                    elif knockback > 1 and x < screen_width-2:
                        knockback -= 2
                        world["smash"][x][y] = world["smash"][x][y][:-1]
                        world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                        x += 2
                        world["smash"][x][y] += "A"
                        world["smash"][x][y+1] += "@"
                    if knockback == -1 and x > 0:
                        knockback = 0
                        world["smash"][x][y] = world["smash"][x][y][:-1]
                        world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                        x -= 1
                        world["smash"][x][y] += "A"
                        world["smash"][x][y+1] += "@"
                    elif knockback < -1 and x > 1:
                        knockback += 2
                        world["smash"][x][y] = world["smash"][x][y][:-1]
                        world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                        x -= 1
                        world["smash"][x][y] += "A"
                        world["smash"][x][y+1] += "@"
                        
                # execute falling
                if jumping == 0 and (falling > 0 or (y > 0 and no_collision(x, y-1))):
                    falling -= 1
                    world["smash"][x][y] = world["smash"][x][y][:-1]
                    world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                    y -= 1
                    world["smash"][x][y] += "A"
                    world["smash"][x][y+1] += "@"
                # execute jump
                if jumping >= 2 or jumping == 1:
                    if jumping == 2:
                        jumping = 1.5
                    else:
                        jumping -= 1
                    world["smash"][x][y] = world["smash"][x][y][:-1]
                    world["smash"][x][y+1] = world["smash"][x][y+1][:-1]
                    y += 1
                    world["smash"][x][y] += "A"
                    world["smash"][x][y+1] += "@"
                elif jumping == 1.5:
                    jumping = 1

                # punching
                if keyboard.is_pressed("space") and hit == 0:
                    hit = 3
                    if facing_left and x > 1:
                        if world["smash"][x-1][y+1][-1] in ["A", "e"]:
                            eknockback = -9
                        elif world["smash"][x-2][y+1][-1] in ["A", "e"]:
                            eknockback = -19
                        world["smash"][x-1][y+1] += "_"
                    elif not facing_left and x < screen_width-2:
                        if world["smash"][x+1][y+1][-1] in ["A", "e"]:
                            eknockback = 9
                        elif world["smash"][x+2][y+1][-1] in ["A", "e"]:
                            eknockback = 19
                        world["smash"][x+1][y+1] += "_"
                elif hit > 0:
                    hit -= 1
                    

            display()
            if current_room == "smash":
                sleep(0.05)
            elif current_room == "kistan":
                sleep(0.1)

        except (KeyboardInterrupt, SystemExit):
            os.system('stty sane')
            print('stopping.')
            sys.exit()

main_loop()
