import pygame
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe") # window title

WHITE = (255, 255, 255) # tuple for rgb white
PURPLE = (74, 0, 143) # rgb purple
TEAL = (27, 224, 208) # rgb teal
RED = (240, 58, 95)
ORANGE = (255, 98, 0)
DARK_ORANGE = (191, 74, 0)
GREY = (62, 58, 56)
LINE_WIDTH = 15
FPS = 60 # define how many frames per second we want game to update at

board = [[None]*3, [None]*3, [None]*3]

def draw_window():
    WIN.fill(ORANGE) # tuple with RGB values to set background of entire screen/window
    
    pygame.draw.line(WIN, DARK_ORANGE, (0, 200), (600, 200), LINE_WIDTH) # draw line: screen, color, start position, end position, width
    pygame.draw.line(WIN, DARK_ORANGE, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(WIN, DARK_ORANGE, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(WIN, DARK_ORANGE, (400, 0), (400, 600), LINE_WIDTH)

    pygame.display.update() # need to do this manually to show changes/things that we draw

def mark_square(row, col, player):
    board[row][col] = player

def check_square(row, col):
    return board[row][col]

def board_full():
    for row in range(3):
        for col in range(3):
            if check_square(row, col) == None:
                return False
    return True

def draw_marks():
    for row in range(3):
        for col in range(3):
            if check_square(row, col) == 2:
                pygame.draw.circle(WIN, WHITE, (int(col * 200 + 100), int(row * 200 + 100)), 60, 15) # Draw circle: screen, color, position (center), radius, thickness
            elif check_square(row, col) == 1:
                pygame.draw.line(WIN, GREY, (int(col * 200 + 50), int(row * 200 + 50)), (int(col * 200 + 150), int(row * 200 + 150)), 20)
                pygame.draw.line(WIN, GREY, (int(col * 200 + 150), int(row * 200 + 50)), (int(col * 200 + 50), int(row * 200 + 150)), 20)

def check_win(player):
    # Check diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return [(0, 0), (2, 2)]
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return [(2, 0), (0, 2)]

    # Check horizontal wins
    win = True
    for row in range(3):
        for col in range(3):
            if board[row][col] != player:
                win = False
                break
        if (win):
            return [(row, 0), (row, 2)]
        win = True
    
    # Check vertical wins
    win = True
    for row in range(3):
        for col in range(3):
            if board[col][row] != player:
                win = False
        if (win):
            return [(0, row), (2, row)]
        win = True
    
    return []

def draw_win(row1, col1, row2, col2, player):
    if col1 < col2:
        if row1 < row2: # diagonal up --> down
            c1 = (int(col1 * 200 + 25), int(row1 * 200 + 25))
            c2 = (int(col2 * 200 + 175), int(row2 * 200 + 175))
        elif row2 < row1: # diagonal down --> up
            c1 = (int(col1 * 200 + 25), int(row1 * 200 + 175))
            c2 = (int(col2 * 200 + 175), int(row2 * 200 + 25))
        else: # horizontal
            c1 = (int(col1 * 200 + 15), int(row1 * 200 + 100))
            c2 = (int(col2 * 200 + 185), int(row2 * 200 + 100))
    else: # vertical
        c1 = (int(col1 * 200 + 100), int(row1 * 200 + 15))
        c2 = (int(col2 * 200 + 100), int(row2 * 200 + 185))

    if player == 1:
        pygame.draw.line(WIN, GREY, c1, c2, LINE_WIDTH)
    else:
        pygame.draw.line(WIN, WHITE, c1, c2, LINE_WIDTH)

def main():
    clock = pygame.time.Clock() # define clock object
    player = 1
    run = True

    draw_window()

    while run:
        clock.tick(FPS) # "tick" the clock FPS (60) times per second = ensures that frame rate is 60fps

        for event in pygame.event.get(): # list of all different events
            if event.type == pygame.QUIT: # user quits; when pygame window opens and press "x" to close window
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: # mouse clicked
                x = event.pos[0] // 200 # x coordinate
                y = event.pos[1] // 200 # y coordinate

                if check_square(y, x) == None:
                    if player == 1:
                        mark_square(y, x, 1)
                    else:
                        mark_square(y, x, 2)
                    draw_marks()

                    result = check_win(player)
                    if result != []:
                        print("Player " + str(player) + " wins!" )
                        draw_win(result[0][0], result[0][1], result[1][0], result[1][1], player)
                        run = False
                    elif board_full():
                        print("Draw!")
                        run = False
                    
                    if player == 1:
                        player = 2
                    else:
                        player = 1
        
        pygame.display.update()

    time.sleep(1.5)
    pygame.quit() # quit game

if __name__ == "__main__":
    main() # Make sure that only run main function if run specifically call this file directly (rather than if it is imported from somwhere else)
        