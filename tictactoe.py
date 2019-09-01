# import necessary modules
import pygame
from pygame.locals import *

""""
-TODO
    *separate into different files
"""

# declare our global variables for the game
XO = "X"  # track whose turn it is; X goes first
grid = [[None, None, None],
        [None, None, None],
        [None, None, None]]

winner = None

window_size = pygame.display.set_mode((900, 900))
background = pygame.Surface(window_size.get_size())
background = background.convert()
background.fill((250, 250, 250))


# declare our support functions
def draw_big_grid():
    pygame.draw.line(background, (130, 0, 0), (300, 20), (300, 880), 4)
    pygame.draw.line(background, (130, 0, 0), (600, 20), (600, 880), 4)

    # horizontal lines...
    pygame.draw.line(background, (130, 0, 0), (20, 300), (880, 300), 4)
    pygame.draw.line(background, (130, 0, 0), (20, 600), (880, 600), 4)

def draw_small_grid():

   draw_small_grid_1_1()
   draw_small_grid_1_2()
   draw_small_grid_1_3()

   draw_small_grid_2_1()
   draw_small_grid_2_2()
   draw_small_grid_2_3()

   draw_small_grid_3_1()
   draw_small_grid_3_2()
   draw_small_grid_3_3()

def draw_small_grid_1_1():
    # horizontal lines for small grid 1,1
    pygame.draw.line(background, (0, 0, 0), (20, 100), (280, 100), 4)
    pygame.draw.line(background, (0, 0, 0), (20, 200), (280, 200), 4)
    # vertical lines for small grid 1,1
    pygame.draw.line(background, (0, 0, 0), (100, 20), (100, 280), 4)
    pygame.draw.line(background, (0, 0, 0), (200, 20), (200, 280), 4)

def draw_small_grid_2_1():
    # horizontal lines for small grid 2,1
    pygame.draw.line(background, (0, 0, 0), (320, 100), (580, 100), 4)
    pygame.draw.line(background, (0, 0, 0), (320, 200), (580, 200), 4)
    # vertical lines for small grid 2, 1
    pygame.draw.line(background, (0, 0, 0), (400, 20), (400, 280), 4)
    pygame.draw.line(background, (0, 0, 0), (500, 20), (500, 280), 4)

def draw_small_grid_3_1():
    # horizontal lines for small grid 3,1
    pygame.draw.line(background, (0, 0, 0), (620, 100), (880, 100), 4)
    pygame.draw.line(background, (0, 0, 0), (620, 200), (880, 200), 4)
    # vertical lines for small grid 3,1
    pygame.draw.line(background, (0, 0, 0), (700, 20), (700, 280), 4)
    pygame.draw.line(background, (0, 0, 0), (800, 20), (800, 280), 4)

def draw_small_grid_1_2():
    # horizontal lines for small grid 1,2
    pygame.draw.line(background, (0, 0, 0), (20, 400), (280, 400), 4)
    pygame.draw.line(background, (0, 0, 0), (20, 500), (280, 500), 4)
    # vertical liens for small grid 1,2
    pygame.draw.line(background, (0, 0, 0), (100, 320), (100, 580), 4)
    pygame.draw.line(background, (0, 0, 0), (200, 320), (200, 580), 4)

def draw_small_grid_1_3():
    # horizontal lines for small grid 1,3
    pygame.draw.line(background, (0, 0, 0), (20, 700), (280, 700), 4)
    pygame.draw.line(background, (0, 0, 0), (20, 800), (280, 800), 4)
    # vertical lines for small grid 1,3
    pygame.draw.line(background, (0, 0, 0), (100, 620), (100, 880), 4)
    pygame.draw.line(background, (0, 0, 0), (200, 620), (200, 880), 4)

def draw_small_grid_2_2():
    # horizontal lines for small grid 2,2
    pygame.draw.line(background, (0, 0, 0), (320, 400), (580, 400), 4)
    pygame.draw.line(background, (0, 0, 0), (320, 500), (580, 500), 4)
    # veritcal lines for small grid 2,2
    pygame.draw.line(background, (0, 0, 0), (400, 320), (400, 580), 4)
    pygame.draw.line(background, (0, 0, 0), (500, 320), (500, 580), 4)

def draw_small_grid_3_2():
    # horizontal lines for small grid 3,2
    pygame.draw.line(background, (0, 0, 0), (620, 400), (880, 400), 4)
    pygame.draw.line(background, (0, 0, 0), (620, 500), (880, 500), 4)
    # vertical lines for small grid 3,2
    pygame.draw.line(background, (0, 0, 0), (700, 320), (700, 580), 4)
    pygame.draw.line(background, (0, 0, 0), (800, 320), (800, 580), 4)

def draw_small_grid_3_3():
    # horizontal lines for small grid 3,3
    pygame.draw.line(background, (0, 0, 0), (620, 700), (880, 700), 4)
    pygame.draw.line(background, (0, 0, 0), (620, 800), (880, 800), 4)
    # vertical liens fro small grid 3,3
    pygame.draw.line(background, (0, 0, 0), (700, 620), (700, 880), 4)
    pygame.draw.line(background, (0, 0, 0), (800, 620), (800, 880), 4)

def draw_small_grid_2_3():
    # horizontal lines for small grid 2,3
    pygame.draw.line(background, (0, 0, 0), (320, 700), (580, 700), 4)
    pygame.draw.line(background, (0, 0, 0), (320, 800), (580, 800), 4)
    # vertical lines for small grid 2,3
    pygame.draw.line(background, (0, 0, 0), (400, 620), (400, 880), 4)
    pygame.draw.line(background, (0, 0, 0), (500, 620), (500, 880), 4)

def init_board():

    draw_big_grid()
    draw_small_grid()

    return background

def draw_status(board):
    # draw the status (i.e., player turn, etc) at the bottom of the board
    # ---------------------------------------------------------------
    # board : the initialized game board surface where the status will
    #         be drawn

    # gain access to global variables
    global XO, winner

    # determine the status message
    if (winner is None):
        message = XO + "'s turn"
    else:
        message = winner + " won!"

    # render the status message
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (255, 0, 0))#text color

    # copy the rendered message onto the board
    board.fill((250, 250, 250), (0, 880, 880, 25))
    board.blit(text, (10, 880))


def show_board(window_size, board):
    # redraw the game board on the display
    # ---------------------------------------------------------------
    # window_size   : the initialized pyGame display
    # board : the game board surface

    draw_status(board)
    window_size.blit(board, (0, 0))
    pygame.display.flip()


def board_position(mouseX, mouseY):
    # given a set of coordinates from the mouse, determine which board space
    # (row, column) the user clicked in.
    # ---------------------------------------------------------------
    # mouseX : the X coordinate the user clicked
    # mouseY : the Y coordinate the user clicked

    # determine the row the user clicked
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    else:
        row = 2

    # determine the column the user clicked
    if (mouseX < 100):
        col = 0
    elif (mouseX < 200):
        col = 1
    else:
        col = 2

    # return the tuple containg the row & column
    return (row, col)


def draw_move(board, boardRow, boardCol, Piece):
    # draw an X or O (Piece) on the board in boardRow, boardCol
    # ---------------------------------------------------------------
    # board     : the game board surface
    # boardRow,
    # boardCol  : the Row & Col in which to draw the piece (0 based)
    # Piece     : X or O

    # determine the center of the square
    centerX = ((boardCol) * 100) + 50
    centerY = ((boardRow) * 100) + 50

    # draw the appropriate piece
    if (Piece == 'O'):
        pygame.draw.circle(board, (0, 0, 0), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line(board, (0, 0, 0), (centerX - 22, centerY - 22),
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line(board, (0, 0, 0), (centerX + 22, centerY - 22),
                         (centerX - 22, centerY + 22), 2)

    # mark the space as used
    grid[boardRow][boardCol] = Piece


def click_board(board):
    # determine where the user clicked and if the space is not already
    # occupied, draw the appropriate piece there (X or O)
    # ---------------------------------------------------------------
    # board : the game board surface

    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = board_position(mouseX, mouseY)

    # make sure no one's used this space
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
        # this space is in use
        return

    # draw an X or O
    draw_move(board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"


def check_for_win(board):
    # determine if anyone has won the game
    # ---------------------------------------------------------------
    # board : the game board surface

    global grid, winner

    # check for winning rows
    for row in range(0, 3):
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and 
                (grid[row][0] is not None)):
            # this row won
            winner = grid[row][0]
            pygame.draw.line(board, (250, 0, 0), (0, (row + 1) * 100 - 50),
                             (300, (row + 1) * 100 - 50), 4)
            break

    # check for winning columns
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
                (grid[0][col] is not None):
            # this column won
            winner = grid[0][col]
            pygame.draw.line(board, (250, 0, 0), ((col + 1) * 100 - 50, 0),
                             ((col + 1) * 100 - 50, 300), 4)
            break

    # check for diagonal winners
    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
            (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]
        pygame.draw.line(board, (250, 0, 0), (50, 50), (250, 250), 4)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
            (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
        pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), 4)


# --------------------------------------------------------------------
# initialize pygame and our window
pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')

# create the game board
board = init_board()

# main event loop
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            click_board(board)

        # check for a winner
        check_for_win(board)

        # update the display
        show_board(window_size, board)