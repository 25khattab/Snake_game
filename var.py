import pygame
import random
import time
img = pygame.image.load('images/SnakeHead.png')
Background = pygame.image.load("images/grass.jpg")
snakeIcon = pygame.image.load('images/snake.png')
apple = pygame.image.load('images/apple.png')
introBackground = pygame.image.load("images/startBackground.jpg")
white = (255, 255, 255)
black = (0, 0, 0)
bright_red = (255, 0, 0)
red = (155, 0, 0)
brown = (33, 20, 18)
purple = (150, 50, 150)
bright_purple = (255, 50, 255)
green = (20, 150, 20)
bright_green = (20, 255, 20)
blue = (30, 0, 150)
bright_blue = (0, 0, 255)
# 1366 768
display_width = 800
display_height = 600
FPS = 30
score = 0
block_size = 10 + 10
apple_thickness = 20
direction = "right"
speed = 10
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
rect_width = display_width / 4.0
rect_height = display_height / 12.0

rect_x_corner = (display_width / 2) - rect_width / 2  # x-ccoordinate of head of the head of the rectangle
rect1_y_corner = (display_height * 1 / 5.0) - (rect_height / 2)  # y-ccoordinate of head of the head of rectangle 1
rect2_y_corner = (display_height * 2 / 5.0) - (rect_height / 2)  # y-ccoordinate of head of the head of rectangle 2
rect3_y_corner = (display_height * 3 / 5.0) - (rect_height / 2)  # y-ccoordinate of head of the head of rectangle 3
rect4_y_corner = (display_height * 4 / 5.0) - (rect_height / 2)  # y-ccoordinate of head of the head of rectangle 4
rect5_y_corner = (display_height*5/5.0)-(rect_height/2)  # y-ccoordinate of head of the head of rectangle 5

rect1_y_displace = -(display_height / 2) + rect1_y_corner + (rect_height / 2)
rect2_y_displace = -(display_height / 2) + rect2_y_corner + (rect_height / 2)
rect3_y_displace = -(display_height / 2) + rect3_y_corner + (rect_height / 2)
rect4_y_displace = -(display_height / 2) + rect4_y_corner + (rect_height / 2)

inactive_color1 = purple
inactive_color2 = green
inactive_color3 = red
inactive_color4 = blue

active_color1 = bright_purple
active_color2 = bright_green
active_color3 = bright_red
active_color4 = bright_blue

rect1_x_displace = - (display_width / 2) + rect_x_corner + (rect_width / 2)
rect2_x_displace = - (display_width / 2) + rect_x_corner + (rect_width / 2)
rect3_x_displace = - (display_width / 2) + rect_x_corner + (rect_width / 2)
rect4_x_displace = - (display_width / 2) + rect_x_corner + (rect_width / 2)
####################################################################################################################################################################################
text_style1_name = "Alger"
text_style2_name = "Rage"
text_style_name = text_style1_name
text_style1 = "Fonts/ALGER.TTF"
text_style2 = "Fonts/RAGE.TTF"
text_style = text_style1
####################################################################################################################################################################################
text_size1_name = "Medium"
text_size2_name = "Small"
text_size_name = text_size1_name
small_text = int((round(display_width/35.0)+round(display_height/35.0))/2)
medium_text = int(round((round(display_width/26.6)+round(display_height/20.0))/2))
big_text = int((round(display_width/23.0)+round(display_height/21.0))/2.0)
text_size = medium_text
####################################################################################################################################################################################
music_state2 = "Enable"
music_state1 = "Disable"
music_state = music_state1
music_bool = True
####################################################################################################################################################################################
score_state2 = "Enable"
score_state1 = "Disable"
score_state = score_state1
score_bool = True