from var import *


def text_objects(text, color, text_style="freesansbold.ttf", text_size=medium_text):
    # change None to Font Style and change 25 to change font size
    font = pygame.font.Font(text_style, text_size)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace, text_style="freesansbold.ttf", text_size=30):
    textSurface, textRectangle = text_objects(msg, color)
    textRectangle.center = (
        display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurface, textRectangle)


def message_to_rect(msg, color, rect_x_center, rect_y_center, text_style=None, text_size=medium_text):
    textSurface, textRectangle = text_objects(
        msg, color, text_style, text_size)
    textRectangle.center = rect_x_center, rect_y_center
    gameDisplay.blit(textSurface, textRectangle)


def startBackground():
    for x in range(display_width // introBackground.get_width() + 1):
        for y in range(display_height // introBackground.get_height() + 1):
            gameDisplay.blit(introBackground, (x * 800, y * 600))


def background():
    for x in range(display_width // Background.get_width() + 1):
        for y in range(display_height // Background.get_height() + 1):
            gameDisplay.blit(Background, (x * 100, y * 100))


def music(song_name, repeat=0):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/"+song_name)
    pygame.mixer.music.play(repeat)


def Apple(random_x_coordinates, random_y_coordinates):
    gameDisplay.blit(apple, (random_x_coordinates, random_y_coordinates))


def snake(block_size, snakeBody):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeBody[-1][0], snakeBody[-1][1]))
    for XnY in snakeBody[:-1]:
        pygame.draw.rect(gameDisplay, black, [
                         XnY[0], XnY[1], block_size, block_size])


def gameLoop():
    if music_bool is True:
        music("Sleep Away.mp3", -1)
    direction = "right"
    global FPS, pause
    FPS = 22
    score = 0
    snakeBody = []
    snakeLength = 5
    random_Apple_x_coordinates = round(random.randrange(
        0, display_width - block_size) / 10.0) * 10.0
    random_Apple_y_coordinates = round(random.randrange(
        0, display_height - block_size) / 10.0) * 10.0
    lead_x = display_width / 2
    lead_x_change = 10
    lead_y = display_height / 2
    lead_y_change = 0
    gameExit = True
    gameOver = False
    speed = 10
    flag = 1
    flag2 = 0
    fail_music_play = True
    while gameExit:
        if score_bool is True:
            message_to_screen("your score is " + str(score), red, 0)
        while gameOver:
            gameDisplay.fill(white)
            if music_bool is True:
                if fail_music_play is True:
                    music("fail.mp3")
                    fail_music_play = False
            message_to_screen("Game Over !!!", red, -50)
            message_to_screen("your score is " + str(score), red, 0)
            message_to_screen(
                "Press 'R' To Play again or 'M' for Menu or 'Q' to Quit", red, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = False
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameLoop()
                    if event.key == pygame.K_m:
                        game_intro()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Screen Boundries
        if lead_x < 0 or lead_x+block_size > display_width or lead_y+block_size > display_height or lead_y < 0:
            gameOver = True

        # Snake Movement
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Apple location and Creation
        Apple(random_Apple_x_coordinates, random_Apple_y_coordinates)

        # Collision Detection
        for eachSegment in snakeBody[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snakeHead = [lead_x, lead_y]
        snakeBody.append(snakeHead)
        if len(snakeBody) > snakeLength:
            del snakeBody[0]
        snake(block_size, snakeBody)
        clock.tick(FPS)

        if ((random_Apple_x_coordinates <= lead_x < random_Apple_x_coordinates + apple_thickness) or (
            random_Apple_x_coordinates < lead_x + block_size <= random_Apple_x_coordinates + apple_thickness)) and (
            (random_Apple_y_coordinates <= lead_y < random_Apple_y_coordinates + apple_thickness) or (
                random_Apple_y_coordinates < lead_y + block_size <= random_Apple_y_coordinates + apple_thickness)):
            random_Apple_x_coordinates = round(random.randrange(
                0, display_width - block_size))  # / 10.0) * 10.0
            random_Apple_y_coordinates = round(random.randrange(
                0, display_height - block_size))  # / 10.0) * 10.0
            gameDisplay.fill(purple, rect=[random_Apple_x_coordinates, random_Apple_y_coordinates, apple_thickness,
                                           apple_thickness])
            snakeLength += 1
            score += 1
            if score % 11 == 0:
                speed += 2

        pygame.display.update()
        background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not flag == 1:
                        direction = "left"
                        lead_x_change = -speed
                        lead_y_change = 0
                        flag2 = 0
                        flag = 1
                elif event.key == pygame.K_RIGHT:
                    if not flag == 1:
                        direction = "right"
                        lead_x_change = speed
                        lead_y_change = 0
                        flag2 = 0
                        flag = 1
                elif event.key == pygame.K_UP:
                    if not flag2 == 1:
                        direction = "up"
                        lead_y_change = -speed
                        lead_x_change = 0
                        flag2 = 1
                        flag = 0
                elif event.key == pygame.K_DOWN:
                    if not flag2 == 1:
                        direction = "down"
                        lead_y_change = speed
                        lead_x_change = 0
                        flag2 = 1
                        flag = 0
    pygame.quit()
    quit()


def game_intro():
    music("boot.mp3", -1)
    startBackground()
    game = True
    while game:
        # User Can Only Quit the game OR Use the button Function to Escape the menu, using the buttons!
        for event in pygame.event.get():
            button(rect_x_corner, rect1_y_corner, rect_width, rect_height, inactive_color1, active_color1, black,
                   "Play", "Play")
            button(rect_x_corner, rect2_y_corner, rect_width, rect_height, inactive_color2, active_color2, black,
                   "Options", "Options")
            button(rect_x_corner, rect3_y_corner, rect_width, rect_height, inactive_color3, active_color3, black,
                   "Credits", "Credits")
            button(rect_x_corner, rect4_y_corner, rect_width, rect_height, inactive_color4, active_color4, black,
                   "Quit", "Quit")
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
            pygame.display.update()


def button(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color, text="Random_Text", action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_x_center = rect_x_corner + (rect_width / 2)
    rect_y_center = rect_y_corner + (rect_height / 2)
    gameDisplay.fill(inactive_color, rect=[
                     rect_x_corner, rect_y_corner, rect_width, rect_height])
    if rect_x_corner + rect_width > mouse[0] > rect_x_corner and rect_y_corner + rect_height > mouse[1] > rect_y_corner:
        gameDisplay.fill(active_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text, text_color, rect_x_center,
                        rect_y_center, text_style, text_size=big_text)
        pygame.display.update()
        if click[0] == 1 and action is not None:
            if action == "Play":
                gameLoop()
            if action == "Options":
                Options()
            if action == "Credits":
                Credits()
            if action == "Quit":
                pygame.quit()
                quit()
            if action == "Back":
                startBackground()
                pygame.display.update()
                game_intro()
    else:
        gameDisplay.fill(inactive_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text, text_color, rect_x_center,
                        rect_y_center, text_style, text_size=medium_text)


def Credits():
    game_credits = True
    gameDisplay.fill(white)
    while game_credits is True:
        for event in pygame.event.get():
            clock.tick(100)
            # def button(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color, text="Random_Text", action=None):
            message_to_screen("The Game is made by :",
                              green, -150, "freesasbold.ttf", 50)
            message_to_screen("Ahmed Tarek", red, -40)
            message_to_screen("omar Wael", black, 40)
            button((rect_x_corner + 200), (rect3_y_corner + 100), rect_width, rect_height, inactive_color3,
                   active_color3, black, "Back", "Back")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def show_score():
    global score
    message_to_screen("Score: "+str(score), white, -0, "freesasbold.ttf", 0)


def switch_button3(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color):
    global score_state, score_bool
    global score_state1, score_state2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_x_center = rect_x_corner + (rect_width / 2)
    rect_y_center = rect_y_corner + (rect_height / 2)
    gameDisplay.fill(inactive_color, rect=[
                     rect_x_corner, rect_y_corner, rect_width, rect_height])
    if rect_x_corner + rect_width > mouse[0] > rect_x_corner and rect_y_corner + rect_height > mouse[1] > rect_y_corner:
        gameDisplay.fill(active_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(score_state, text_color, rect_x_center,
                        rect_y_center, text_size=text_size)
        pygame.display.update()
        if click[0] == 1:
            if score_state == score_state1:
                score_state = score_state2
                score_bool = False
            elif score_state == score_state2:
                score_state = score_state1
                score_bool = True
    else:
        gameDisplay.fill(inactive_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(score_state, text_color, rect_x_center, rect_y_center)


def switch_button(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color):
    global text_style_name, text_style
    global text_style1_name, text_style2_name, text_style3_name
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_x_center = rect_x_corner + (rect_width / 2)
    rect_y_center = rect_y_corner + (rect_height / 2)
    gameDisplay.fill(inactive_color, rect=[
                     rect_x_corner, rect_y_corner, rect_width, rect_height])
    if rect_x_corner + rect_width > mouse[0] > rect_x_corner and rect_y_corner + rect_height > mouse[1] > rect_y_corner:
        gameDisplay.fill(active_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text_style_name, text_color, rect_x_center,
                        rect_y_center, text_style, text_size=big_text)
        pygame.display.update()
        if click[0] == 1:
            if text_style_name == text_style1_name:
                text_style_name = text_style2_name
                text_style = text_style2
            elif text_style_name == text_style2_name:
                text_style_name = text_style1_name
                text_style = text_style1
    else:
        gameDisplay.fill(inactive_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text_style_name, text_color,
                        rect_x_center, rect_y_center, text_style)


def switch_button2(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color):
    global music_state, music_bool
    global music_state1, music_state2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_x_center = rect_x_corner + (rect_width / 2)
    rect_y_center = rect_y_corner + (rect_height / 2)
    gameDisplay.fill(inactive_color, rect=[
                     rect_x_corner, rect_y_corner, rect_width, rect_height])
    if rect_x_corner + rect_width > mouse[0] > rect_x_corner and rect_y_corner + rect_height > mouse[1] > rect_y_corner:
        gameDisplay.fill(active_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(music_state, text_color, rect_x_center,
                        rect_y_center, text_size=text_size)
        pygame.display.update()
        if click[0] == 1:
            if music_state == music_state1:
                music_state = music_state2
                music_bool = False
            elif music_state == music_state2:
                music_state = music_state1
                music_bool = True
    else:
        gameDisplay.fill(inactive_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(music_state, text_color, rect_x_center, rect_y_center)


def switch_button1(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color):
    global text_size_name, text_size
    global text_size1_name, text_size2_name
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_x_center = rect_x_corner + (rect_width / 2)
    rect_y_center = rect_y_corner + (rect_height / 2)
    gameDisplay.fill(inactive_color, rect=[
                     rect_x_corner, rect_y_corner, rect_width, rect_height])
    if rect_x_corner + rect_width > mouse[0] > rect_x_corner and rect_y_corner + rect_height > mouse[1] > rect_y_corner:
        gameDisplay.fill(active_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text_size_name, text_color, rect_x_center,
                        rect_y_center, text_size=text_size)
        pygame.display.update()
        if click[0] == 1:
            if text_size_name == text_size1_name:
                text_size_name = text_size2_name
                text_size = small_text
                guy = True
            elif text_size_name == text_size2_name:
                text_size_name = text_size1_name
                text_size = medium_text
                guy = False
    else:
        gameDisplay.fill(inactive_color, rect=[
                         rect_x_corner, rect_y_corner, rect_width, rect_height])
        message_to_rect(text_size_name, text_color,
                        rect_x_center, rect_y_center)


def Options():
    game_options = True
    gameDisplay.blit(introBackground, [0, 0])
    while game_options is True:
        for event in pygame.event.get():
            clock.tick(FPS)
            # def button(rect_x_corner, rect_y_corner, rect_width, rect_height, inactive_color, active_color, text_color, text="Random_Text", action=None):
            button(rect_x_corner-round(display_width/3.0), rect1_y_corner-round(display_height/7.5),
                   rect_width, rect_height, inactive_color3, active_color3, black, text="Resolution", action=None)
            button(rect_x_corner-round(display_width/3.0), rect2_y_corner-round(display_height/7.5),
                   rect_width, rect_height, inactive_color2, active_color2, black, text="Music", action=None)
            switch_button2(rect_x_corner, rect2_y_corner - round(display_height / 7.5), rect_width, rect_height,
                           inactive_color2, active_color2, black)
            button(rect_x_corner-round(display_width/3.0), rect3_y_corner-round(display_height/7.5),
                   rect_width, rect_height, inactive_color3, active_color3, black, text="Font Size", action=None)
            switch_button1(rect_x_corner, rect3_y_corner - round(display_height / 7.5), rect_width, rect_height,
                           inactive_color2, active_color2, black)
            button(rect_x_corner-round(display_width/3.0), rect4_y_corner-round(display_height/7.5),
                   rect_width, rect_height, inactive_color2, active_color2, black, text="Show Score", action=None)
            switch_button3(rect_x_corner, rect4_y_corner - round(display_height / 7.5), rect_width, rect_height,
                           inactive_color2, active_color2, black)
            button(rect_x_corner - round(display_width / 3.0), rect5_y_corner - round(display_height / 7.5),
                   rect_width, rect_height, inactive_color2, active_color2, black, text="Font Style", action=None)
            switch_button(rect_x_corner, rect5_y_corner - round(display_height / 7.5),
                          rect_width, rect_height, inactive_color2, active_color2, black)
            button(rect_x_corner+round(display_width/2.75), (rect5_y_corner-display_height/20),
                   rect_width, rect_height, inactive_color3, active_color3, black, text="Back", action="Back")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
