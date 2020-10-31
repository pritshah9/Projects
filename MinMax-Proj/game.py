import pygame as pg
import math
import minmax
import sys
import threading




XO = "X"

board = [[None, None, None], [None, None, None], [None, None, None]]

result = None

winWidth = 630;
winHeight = 630;
gridWidth = winWidth/3;
gridHeight = winHeight/3;
white = (255, 255, 255)
SPACING = 20
pg.init()
run = True
game_over = False



def game_result(grid):
    for i in range(3):
        if grid[i][0] is not None and grid[i][0] == grid[i][1] == grid[i][2]:
            return grid[i][0]
        if grid[0][i] is not None and grid[0][i] == grid[1][i] == grid[2][i]:
            return grid[0][i]

    if grid[0][2] is not None and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    if grid[0][0] is not None and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    if is_full(board):
        return "draw"

    return None


def restart():
    win.fill((0, 0, 0))
    ttt_lines(win)
    global XO
    global board
    board = [[None, None, None], [None, None, None], [None, None, None]]
    XO = "X"


def draw_XO(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                pg.draw.line(win, white, (int(j*gridHeight + SPACING), int((i+1)*gridWidth - SPACING)),
                             (int((j+1)*gridHeight - SPACING), int(i*gridWidth + SPACING)), 1)
                pg.draw.line(win, white, (int(j*gridHeight + SPACING), int(i*gridWidth + SPACING)),
                             (int((j+1)*gridHeight - SPACING), int((i+1)*gridWidth - SPACING)), 1)
            elif grid[i][j] == "O":
                pg.draw.circle(win, white, (int(j*gridHeight + (gridHeight/2)), int(i*gridWidth + (gridWidth/2))),
                               gridWidth/2 - SPACING, 1)


def is_full(grid):
    for rows in range(3):
        for cols in range(3):
            if grid[rows][cols] is None:
                return False
    return True


def is_available(grid, x, y):
    return grid[x][y] is None


def ttt_lines(window):
    pg.draw.line(window, white, (0, gridHeight), (winWidth, gridHeight))
    pg.draw.line(window, white, (0, gridHeight*2), (winWidth, gridHeight*2))
    pg.draw.line(window, white, (gridWidth, 0), (gridWidth, winHeight))
    pg.draw.line(window, white, (gridWidth*2, 0), (gridWidth*2, winHeight))


win = pg.display.set_mode((winWidth, winHeight))
pg.display.set_caption("Tic-Tac-Toe")
ttt_lines(win)



while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            posX = event.pos[0]
            posY = event.pos[1]
            clicked_row = int(event.pos[1]/gridWidth)
            clicked_col = int(event.pos[0]/gridHeight)
            if is_available(board, clicked_row, clicked_col):
                board[clicked_row][clicked_col] = XO
                draw_XO(board)
                if game_result(board) is not None:
                    game_over = True
                    result = game_result(board)
                if XO == "X":
                    XO = "O"
                else:
                    XO = "X"

                if XO == "O":
                    minValue, moveX, moveY = minmax.min(board, -2, 2)
                    if is_available(board, moveX, moveY):
                        board[moveX][moveY] = XO
                        draw_XO(board)
                        if game_result(board) is not None:
                            game_over = True
                            result = game_result(board)
                        XO = "X"

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                restart()
                game_over = False

    pg.display.update()






