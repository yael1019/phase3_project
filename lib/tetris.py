import random
import pygame
from highscore import HighScore


pygame.font.init()

# Screen and block sizes
s_width = 800
s_height = 700
# screen_width = 800
# screen_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
# top_left_x = (screen_width - play_width) // 2
# top_left_y = screen_height - play_height

# # Shapes
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# List of shapes 
shapes = [S, Z, I, O, J, L, T]

# Color of shape in order to align with the index in the list of shapes
# shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)] 
shape_colors = [(0, 230, 172), (255, 80, 80), (0, 255, 255), (255, 255, 102), (255, 133, 51), (0, 153, 255), (204, 0, 204)] 

# class Piece(object):
#     rows = 20
#     columns = 10

#     def __init__(self, x, y, shape):
#         self.x = x
#         self.y = y
#         self.shape = shape
#         # we do not need to pass in color as an argument
#         # we want the same color at index of the shape that is passed in 
#         self.color = shape_colors[shapes.index(shape)]
#         # when we want to rotate the shape we will add one to it because each shape list has all the rotations 
#         # index 0 is the first rotation, index 1 is the next rotation
#         self.rotation = 0

# def create_grid(locked_pos = {}):
#     # create one list for every row in our grid
#     # creates a blank grid
#     grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

#     # locked_pos is the blocks in our grid that are not moving they already fell down and are static
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             # rows are represented by i, columns are represented by j
#             # j is x and i is y value
#             if (j, i) in locked_pos:
#                 value = locked_pos[(j, i)]
#                 grid[i][j] = value

#     return grid

# def convert_shape_format(shape):
#     positions = []
#     # grab each index in the shape list (grabbing the diff rotations)
#     format = shape.shape[shape.rotation % len(shape.shape)]

#     for i, line in enumerate(format):
#         row = list(line)
#         # row will be a list of . and 0, ex: ..0..
#         for j, column in enumerate(row):
#             if column == '0':
#                 positions.append((shape.x + j, shape.y + i))

#     for i, pos in enumerate(positions):
#         positions[i] = (pos[0] - 2, pos[1] - 4)
        
#     return positions
 
# def valid_space(shape, grid):
#     # returns if the current position we are in is a valid space so we don't go off the screen
#     accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
#     accepted_pos = [j for sub in accepted_pos for j in sub]
#     # this is allowing us to flatten out our list 
#     # [[(0, 1)], [(2, 3)]] --> [(0, 1), (2, 3)]
#     # removes the nested lists

#     # call our convert_shape_format fn
#     formatted = convert_shape_format(shape)

#     for pos in formatted:
#         if pos not in accepted_pos:
#             if pos[1] > -1:
#                 return False
#     return True
 
# def check_lost(positions):
#     # check if any of the positions are above the screen and then we lost the game
#     for pos in positions:
#         # split up the tuple
#         x, y = pos
#         if y < 1:
#              return True
#     # if the position is greater than 1 return false because we have not lost yet
#     return False
 
# def get_shape():
#     global shapes, shape_colors
#     # picks one of the shapes in our shapes list
#     # so we get a random shape to fall down the screen

#     # call the class piece and pass in x, y coordinates and a shape
#     return Piece(5, 0, random.choice(shapes))
 
# def draw_text_middle(text, size, color, surface):
#     # display the score when we lose
#     font = pygame.font.SysFont('comicsane', size, bold=True)
#     label = font.render(text, 1, color)

#     surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y + play_height /  2 - (label.get_height() / 2)))
   
# def draw_grid(surface, row, col):
#     # draw the lines for the grid
#     sx = top_left_x
#     sy = top_left_y

#     for i in range(row):
#         # this will draw 20 vertical lines
#         pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * 30), (sx + play_width, sy + i * 30))
#         for j in range(col):
#             # this will draw 10 horizontal lines
#             pygame.draw.line(surface, (128, 128, 128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))

 
# def clear_rows(grid, locked):
#     # incrementer
#     inc = 0
#     # loop through the grid backwards
#     for i in range(len(grid) - 1, -1, -1):
#         row = grid[i]
#         # if (0,0,0) does not exist the row needs to be cleared
#         # if there is no black square the row is full and should be deleted
#         if (0, 0, 0) not in row:
#             inc += 1
#             ind = i
#             for j in range(len(row)):
#                 try:
#                     del locked[(j, i)]
#                 except:
#                      continue
    
#     # after a row is deleted we need to shift every row down
#     # we also need to add another row on top to make sure our grid stays the same size
#     if inc > 0:
#         for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
#             x, y = key
#             if y < ind:
#                 new_key = (x, y + inc)
#                 locked[new_key] = locked.pop(key)

#     return inc

 
# def draw_next_shape(shape, surface):
#     # shows the next shape before it dropped

#     # font for our label
#     font = pygame.font.SysFont('cambriacambriamath', 30)
#     # the label = the text we want to display and the color
#     label = font.render('Next shape:', 1, (255, 255, 255))

#     # the position on the screen
#     sx = top_left_x + play_width + 50
#     sy = top_left_y + play_height/2 - 100

#     format = shape.shape[shape.rotation % len(shape.shape)]

#     for i, line in enumerate(format):
#         row = list(line)
#         for j, column in enumerate(row):
#             if column == '0':
#                 pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

#     surface.blit(label, (sx + 10, sy - 30))


# # def update_score(nscore):
# #     with open('scores.txt', 'r') as f:
# #         lines = f.readlines()
# #         score = lines[0].strip()

# #     with open('scores.txt', 'w') as f:
# #         # if the original score is greater than the original score otherwise we write the new score
# #         if int(score) > nscore:
# #             f.write(str(score))
# #         else:
# #             f.write(str(nscore))

# # def max_score():
# #     with open('scores.txt', 'r') as f:
# #         lines = f.readlines()
# #         score = lines[0].strip()
# #     return score
 
# def draw_window(surface, score = 0, last_score = 0):
#     # surface is what we are drawing on
#     # the surface is going to be black
#     surface.fill((0, 0, 0))

#     # setting up font and getting ready to draw on the screen
#     # pygame.font.init()
#     # this is the font and size of the font
#     #* to change font look up fonts on pygame website
#     font = pygame.font.SysFont('cambriacambriamath', 70, bold=True)
#     # Our title
#     label = font.render('Tetris', 1, (255, 255, 255))

#     # draw the label on the screen
#     surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))

#     # font for our label for the current score
#     font = pygame.font.SysFont('cambriacambriamath', 30)
#     # the label = the text we want to display and the color
#     label = font.render('Score: ' + str(score), 1, (255, 255, 255))

#     # the position on the screen
#     sx = top_left_x + play_width + 50
#     sy = top_left_y + play_height/2 - 100

#     # the location of the score on the screen
#     surface.blit(label, (sx + 20, sy + 160))

#     # Our label for the last score
#     # the label = the text we want to display and the color
#     # label = font.render('High Score: ' + str(last_score), 1, (255, 255, 255))

#     # the position on the screen
#     # sx = top_left_x - 200
#     # sy = top_left_y + 200

#     # the location of the score on the screen
#     # surface.blit(label, (sx + 20, sy + 160))

#     for i in range(len(grid)): 
#         for j in range(len(grid[i])):
#             pygame.draw.rect(surface, grid[i][j], (top_left_x + j*30, top_left_y + i*30, 30, 30), 0)
    
#     # call our draw_grid fn
#     draw_grid(surface, 20, 10)
#     # draw the border
#     pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

#     # update the screen
#     # pygame.display.update()
 
# def main():
#     global grid
#     # last_score = max_score()

#     # this is what we are passing into create_grid fn
#     locked_positions = {}
#     grid = create_grid(locked_positions)

#     change_piece = False
#     run = True
#     current_piece = get_shape()
#     next_piece = get_shape()
#     clock = pygame.time.Clock()
#     fall_time = 0
#     # to make the piece fall faster with time
#     level_time = 0
#     score = 0

#     # while loop keeps the screen open until we exit it
#     while run:
#         # how long it will take before each shape starts falling
#         fall_speed = 0.27

#         grid = create_grid(locked_positions)
#         fall_time += clock.get_rawtime()
#         level_time += clock.get_rawtime()
#         clock.tick()

#         if level_time/1000 > 5:
#             level_time = 0
#             if fall_speed > 0.12:
#                 fall_speed -= 0.0

#         if fall_time / 1000 > fall_speed:
#             fall_time = 0
#             current_piece.y += 1
#             if not (valid_space(current_piece, grid)) and current_piece.y > 0:
#                 current_piece.y -= 1
#                 change_piece = True 

#         for event in pygame.event.get():
#             # if we quit the game, reasign run to false so we exit the loop and the window is closed
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.display.quit()
#                 quit()

#             # move the blocks according to the keys we hit on the keyboard
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     current_piece.x -= 1
#                     # check that if is a valid space and we are not moving off the screen
#                     if not valid_space(current_piece, grid):
#                         current_piece.x += 1
#                 elif event.key == pygame.K_RIGHT:
#                     current_piece.x += 1
#                     if not valid_space(current_piece, grid):
#                         current_piece.x -= 1
#                 elif event.key == pygame.K_UP:
#                     # rotate the shape
#                     current_piece.rotation += 1
#                     if not valid_space(current_piece, grid):
#                         current_piece.rotation -= 1
#                 if event.key == pygame.K_DOWN:
#                     current_piece.y += 1
#                     if not valid_space(current_piece, grid):
#                         current_piece.y -= 1
        
#         shape_pos = convert_shape_format(current_piece)

#         for i in range(len(shape_pos)):
#             x, y = shape_pos[i]
#             if y > -1:
#                 grid[y][x] = current_piece.color
        
#         if change_piece:
#             for pos in shape_pos:
#                 p = (pos[0], pos[1])
#                 locked_positions[p] = current_piece.color
#             current_piece = next_piece
#             next_piece = get_shape()
#             change_piece = False
#             score += clear_rows(grid, locked_positions) * 10

#             clear_rows(grid, locked_positions)

        
#         # call draw_window fn
#         draw_window(win, score)

#         # call draw_next_shape fn
#         draw_next_shape(next_piece, win)

#         # update the display
#         pygame.display.update()

#         if check_lost(locked_positions):
#             run: False
#             # update_score(score)
#     # show a message when we lose - text, size, color, surface
#     draw_text_middle('YOU LOST!', 80, (255, 255, 255), win)
#     pygame.display.update()
#     # delay will show this message for 1.5 seconds before we go back to menu screen
#     pygame.time.delay(2000)

#         # pygame.display.quit()
 
# def main_menu():
#     # main menu screen
#     run = True 
#     while run:
#         win.fill((0,0,0))
#         draw_text_middle('Press Any Key To Play', 60, (255, 255, 255), win)
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.KEYDOWN:
#                 main()
    
#     pygame.quit()

# win = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Tetris')
# main_menu()

 
class Piece():
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3
 
 
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid
 
 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions
 
 
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
 
    return True
 
 
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
 
def get_shape():
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('cambriacambriamath', size, bold=True)
    label = font.render(text, 1, color)
 
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))
 
 
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines
 
 
def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one
 
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc
 
 
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('cambriacambriamath', 40, bold=True, italic=True)
    label = font.render('Next Shape:', 1, (255,255,255))
 
    sx = top_left_x + play_width + 45
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    surface.blit(label, (sx + 10, sy- 30))
 
 
def draw_window(surface, score = 0):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('cambriacambriamath', 70, bold=True)
    label = font.render('TETRIS', 1, (255,255,255))
 
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont('cambriacambriamath', 40, bold=True, italic=True)
    label = font.render('Score: ' + str(score), 1, (255,255,255))
 
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    
    surface.blit(label, (sx + 20, sy + 160))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10)
    # pygame.draw.rect(surface, (0, 204, 255), (top_left_x, top_left_y, play_width, play_height), 5)
    pygame.draw.rect(surface, (255, 0, 102), (top_left_x, top_left_y, play_width, play_height), 5)
    # pygame.display.update()
 
 
def main(win,username,id):
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    # how long it will take before each shape starts falling
    fall_speed = 0.27
    # to make the piece fall faster with time
    level_time = 0
    score = 0
 
    while run:
        fall_speed = 0.27
 
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.0
 
        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
 
                    # if event.key == pygame.K_SPACE:
                    #     while valid_space(current_piece, grid):
                    #         current_piece.y += 1
                    #         current_piece.y -= 1
                    # print(convert_shape_format(current_piece))
 
        shape_pos = convert_shape_format(current_piece)
 
        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
 
        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
 
            # call four times to check for multiple clear rows
            score += clear_rows(grid, locked_positions) * 10
 
        draw_window(win, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()
 
        # Check if user lost
        if check_lost(locked_positions):
            none = HighScore(username,score, id)
            none.save()
            run = False
 
    draw_text_middle("You Lost", 40, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(2000)
 
 
def main_menu(username, id):
    win = pygame.display.set_mode((s_width, s_height))
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main(win,username,id)
    pygame.quit()
 
 

pygame.display.set_caption('Tetris')
 
#main_menu()  # start game

 