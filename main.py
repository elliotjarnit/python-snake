import keyboard
import time
import threading
import random

class Game:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 2, 3, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.gameOver = False
        self.direction = 'left'
        self.lastloc = []


# def on_press(key):
#     if game.direction != 'right':
#         if key == Key.left:
#             game.direction = 'left'
#     if game.direction != 'left':
#         if key == Key.right:
#             game.direction = 'right'
#     if game.direction != 'up':
#         if key == Key.down:
#             game.direction = 'down'
#     if game.direction != 'down':
#         if key == Key.up:
#             game.direction = 'up'


def add_snake_size():
    count = 0
    for row in range(len(game.board)):
        for column in range(len(game.board[row])):
            try:
                if game.board[row][column] > 0:
                    count += 1
            except TypeError:
                pass

    game.board[game.lastloc[0]][game.lastloc[1]] = count + 1


def place_apples(times = 1):
    for i in range(times):
        done = False
        while not done:
            rows = len(game.board)
            columns = 0
            for column in game.board:
                columns += 1

            pickrow = random.randint(0, rows - 1)
            pickcolumn = random.randint(0, columns - 1)

            if game.board[pickrow][pickcolumn] != 'a':
                if game.board[pickrow][pickcolumn] < 1:
                    game.board[pickrow][pickcolumn] = 'a'
                    done = True


def print_board():
    print("\n" * 50)
    for row in game.board:
        for tile in row:
            if tile == 'a':
                print("🟥    ", end="")
            elif tile > 0:
                print("🟪    ", end="")
            elif tile == 0:
                print("⬜️    ", end="")
        print("\n")


def main_loop():
    while not game.gameOver:
        print_board()

        # Remove Apples
        tempapples = []
        for row in range(len(game.board)):
            for column in range(len(game.board[row])):
                if game.board[row][column] == 'a':
                    tempapples.append([row, column])
                    game.board[row][column] = '0'

        # Move Snake
        newpos = None
        onpos = 1
        cycles = 0
        temp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        while cycles < 2:
            cycles += 1
            for row in range(len(game.board)):
                for tile in range(len(game.board[row])):
                    if onpos == 1:
                        if game.board[row][tile] == onpos:
                            newpos = [row, tile]
                            try:
                                if game.direction == 'left':
                                    if tile - 1 < 0:
                                        game.gameOver = True
                                    try:
                                        if game.board[row][tile - 1] > 0:
                                            game.gameOver = True
                                    except TypeError:
                                        pass
                                    temp[row][tile - 1] = onpos
                                elif game.direction == 'right':
                                    try:
                                        if game.board[row][tile + 1] > 0:
                                            game.gameOver = True
                                    except TypeError:
                                        pass
                                    temp[row][tile + 1] = onpos
                                elif game.direction == 'up':
                                    if row - 1 < 0:
                                        game.gameOver = True
                                    try:
                                        if game.board[row - 1][tile] > 0:
                                            game.gameOver = True
                                    except TypeError:
                                        pass
                                    temp[row - 1][tile] = onpos
                                elif game.direction == 'down':
                                    try:
                                        if game.board[row + 1][tile] > 0:
                                            game.gameOver = True
                                    except TypeError:
                                        pass
                                    temp[row + 1][tile] = onpos
                            except IndexError:
                                game.gameOver = True
                            onpos += 1
                            cycles -= 1

                    else:
                        if game.board[row][tile] == onpos:
                            temp[newpos[0]][newpos[1]] = onpos
                            newpos = [row, tile]
                            onpos += 1
                            cycles -= 1
                            game.lastloc = [row, tile]
        game.board = temp
        time.sleep(0.4)

        # Add Apples
        for apple in tempapples:
            if type(game.board[apple[0]][apple[1]]) == str:
                pass
            elif game.board[apple[0]][apple[1]] > 0:
                add_snake_size()
                place_apples()
            else:
                game.board[apple[0]][apple[1]] = 'a'

    # Game Over
    print("\n" * 50)
    print("GAME OVER")
    count = 0
    for row in range(len(game.board)):
        for column in range(len(game.board[row])):
            try:
                if game.board[row][column] > 0:
                    count += 1
            except TypeError:
                pass
    print("SCORE: " + str(count) + "\n")

def press_left():
    if game.direction != 'right':
        game.direction = 'left'

def press_right():
    if game.direction != 'left':
        game.direction = 'right'

def press_down():
    if game.direction != 'up':
        game.direction = 'down'

def press_up():
    if game.direction != 'down':
        game.direction = 'up'

game = Game()

keyboard.on_press_key("left", lambda _:press_left())
keyboard.on_press_key("right", lambda _:press_right())
keyboard.on_press_key("up", lambda _:press_up())
keyboard.on_press_key("down", lambda _:press_down())

place_apples(2)
print_board()
loop = threading.Thread(name="mainloop", target=main_loop)
loop.start()

