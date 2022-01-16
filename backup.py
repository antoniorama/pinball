import pygame, math, random
from functions import negative as negative
import functions 

one_nine = ['1','2','3','4','5','6','7','8','9']

# Music
pygame.mixer.init()
pygame.mixer.music.load('./music/pinball_music.mp3')
pygame.mixer.music.play()

# Colors
PINK_RGB = (255,20,147)
BLACK_RGB = (0,0,0)
CYAN_RGB = (0,255,255)

# Random module
rand_range = [-1, 0, 1]

SCREEN_SIZE = (1000,600)
pygame.display.set_caption('Pinball')

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.init()

BLUE_BACKGROUND = pygame.image.load('./imgs/light-blue-wallpaper.webp')

BALL = pygame.image.load('./imgs/bola.png')
STEEL_BALL = pygame.image.load('./imgs/steel_ball.png')
STEEL_BALL = pygame.transform.scale(STEEL_BALL, (40,45))

vx, vy = 6, 6
in_vx, in_vy = 6, 6
ball_v = (vx, vy)
WALLS = pygame.image.load('./imgs/base.png')

LEFT_ARROW_1 = pygame.image.load('./imgs/left_1.png')
LEFT_ARROW_3= pygame.image.load('./imgs/left_3_f.png')

RIGHT_ARROW_1 = pygame.image.load('./imgs/right_1.png')
RIGHT_ARROW_3 = pygame.image.load('./imgs/right_3.png')

OBS_1 = pygame.Rect(250,100,35,150)
OBS_1_2 = pygame.Rect(350,100,35,150)
OBS_1_SCORE = pygame.Rect(285,175,75,2)
OBS_1_IMG, obs_1_img_cords = pygame.image.load('./imgs/score_cross.png'), (292, 158)
OBS_1_IMG = pygame.transform.scale(OBS_1_IMG, (50,50))

OBS_2 = pygame.Rect(1000-350-35,100,35,150)
OBS_2_2 = pygame.Rect(1000-250-35,100,35,150)
OBS_2_SCORE = pygame.Rect(1000-390+35,175,75,2)
OBS_2_IMG, obs_2_img_cords = OBS_1_IMG, (693-35,158)
OBS_2_IMG = pygame.transform.scale(OBS_2_IMG, (50,50))

OBS_3 = pygame.Rect(475,150,50,50)

OBS_4 = pygame.Rect(150,350,125,125)
BAR_WIDHT = 20
OBS_4_IMG = pygame.Rect(OBS_4.x+BAR_WIDHT,OBS_4.y+BAR_WIDHT,OBS_4.width-2*BAR_WIDHT,OBS_4.height-2*BAR_WIDHT)

OBS_5 = pygame.Rect(SCREEN_SIZE[0]-OBS_4.x-OBS_4.width, OBS_4.y, OBS_4.width, OBS_4.height)
OBS_5_IMG = pygame.Rect(OBS_5.x+BAR_WIDHT,OBS_5.y+BAR_WIDHT,OBS_5.width-2*BAR_WIDHT,OBS_5.height-2*BAR_WIDHT)

obs_list_pink = [OBS_1, OBS_1_2, OBS_2, OBS_2_2, OBS_3, OBS_4, OBS_5]
obs_list_not_pink = [(OBS_4_IMG, CYAN_RGB),(OBS_5_IMG, CYAN_RGB)]
non_col_list = [(OBS_1_IMG, obs_1_img_cords), (OBS_2_IMG, obs_2_img_cords)]

# Fonts
score_font = pygame.font.Font("freesansbold.ttf", 32)
inside_box_font = pygame.font.Font("./fonts/PKMN-Pinball.ttf", 45)
title_font = pygame.font.Font("./fonts/PKMN-Pinball.ttf", 75)
button_font = pygame.font.Font("./fonts/PKMN-Pinball.ttf", 55)
author_font = pygame.font.Font("freesansbold.ttf", 16)
final_score_font = pygame.font.Font("./fonts/PKMN-Pinball.ttf", 25)


def main_menu():
    steel_ball_coords_play = (345,270)
    steel_ball_coords_exit = (360,417)
    steel_ball_coords = steel_ball_coords_play
    while True:
        SCREEN.blit(BLUE_BACKGROUND,(0,0))
        SCREEN.blit(STEEL_BALL, steel_ball_coords)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Title : 'PINBALL'
        title = title_font.render(f"PinBall", True, PINK_RGB)
        SCREEN.blit(title, (275,50))

        # Play Button
        play_button = button_font.render(f"play", True, PINK_RGB)
        SCREEN.blit(play_button, (400,250))

        # Exit Button
        exit_button = button_font.render(f"exit", True, PINK_RGB)
        SCREEN.blit(exit_button, (415,400))

        # Author
        author = author_font.render(f"by antoniorama", True, (0,0,0))
        SCREEN.blit(author, (875,580))

        # Button mechanics
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_DOWN]:
            steel_ball_coords = steel_ball_coords_exit

        if keys_pressed[pygame.K_UP]:
            steel_ball_coords = steel_ball_coords_play

        if (keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]) and steel_ball_coords == steel_ball_coords_play:
            break

        if (keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]) and steel_ball_coords == steel_ball_coords_exit:
            pygame.quit()

        pygame.display.update()

def game_lost(final_score_n):
    pygame.mixer.music.stop()
    steel_ball_coords_play = (345,270)
    steel_ball_coords_exit = (360,417)
    steel_ball_coords = steel_ball_coords_play

    while True:
        SCREEN.blit(BLUE_BACKGROUND,(0,0))
        SCREEN.blit(STEEL_BALL, steel_ball_coords)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Title : 'Game Over'
        title = title_font.render(f"GameOver", True, PINK_RGB)
        SCREEN.blit(title, (200,50))

        # Final Score
        final_score = final_score_font.render(f"final score  {final_score_n}", True, PINK_RGB)
        SCREEN.blit(final_score, (15,550))

        # Play Button
        play_button = button_font.render(f"menu", True, PINK_RGB)
        SCREEN.blit(play_button, (400,250))

        # Exit Button
        exit_button = button_font.render(f"exit", True, PINK_RGB)
        SCREEN.blit(exit_button, (415,400))

        # Author
        author = author_font.render(f"by antoniorama", True, (0,0,0))
        SCREEN.blit(author, (875,580))

        # Button mechanics
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_DOWN]:
            steel_ball_coords = steel_ball_coords_exit

        if keys_pressed[pygame.K_UP]:
            steel_ball_coords = steel_ball_coords_play

        if (keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]) and steel_ball_coords == steel_ball_coords_play:
            main()

        if (keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]) and steel_ball_coords == steel_ball_coords_exit:
            pygame.quit()
        
        pygame.display.update()

def draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords, ind_left, ind_right, score):
    # Jogo básico, sem obstáculos
    SCREEN.fill((0,255,255))
    pygame.draw.rect(SCREEN, PINK_RGB, pygame.Rect(0,0,60,600)) # left bar
    pygame.draw.rect(SCREEN, PINK_RGB, pygame.Rect(1000-60,0,60,600)) # right bar
    pygame.draw.rect(SCREEN, PINK_RGB, pygame.Rect(0,0,1000,25)) # top bar
    SCREEN.blit(BALL, (ball.x, ball.y)) # bola
    pygame.draw.rect(SCREEN, PINK_RGB, pygame.Rect(60,565,305,35)) # bottom left bar
    pygame.draw.rect(SCREEN, PINK_RGB, pygame.Rect(635,565,330,35)) # bottom right bar
    SCREEN.blit(left_arrow, left_arrow_cords) # draw left arrow
    rect_left_arrow_1 = pygame.Rect(left_arrow_cords[0], left_arrow_cords[1], 101, 36) # left arrow hitbox
#    pygame.draw.rect(SCREEN, PINK_RGB, rect_left_arrow_1, 1) # temp hitbox
    SCREEN.blit(right_arrow, right_arrow_cords) # draw right arrow
    rect_right_arrow_1 = pygame.Rect(right_arrow_cords[0], right_arrow_cords[1], 101, 36) # right arrow hitbox
#    pygame.draw.rect(SCREEN, PINK_RGB, rect_right_arrow_1, 1) # temp hitbox

    # Obstáculos
    for obs in obs_list_pink:
        pygame.draw.rect(SCREEN, PINK_RGB, obs)

    for obs in obs_list_not_pink:
        pygame.draw.rect(SCREEN, obs[1], obs[0])

    for obs in non_col_list:
        SCREEN.blit(obs[0], obs[1])

    # Text stuff

    # Left box number
    left_obs_score = inside_box_font.render(f"{int(one_nine[ind_left])}", True, PINK_RGB)
    SCREEN.blit(left_obs_score, (OBS_4_IMG.x+27,OBS_4_IMG.top+10))
    
    # Right box number
    left_obs_score = inside_box_font.render(f"{int(one_nine[ind_right])}", True, PINK_RGB)
    SCREEN.blit(left_obs_score, (OBS_5_IMG.x+27,OBS_5_IMG.top+10))

    # General Score
    score_text = score_font.render(f"Score: {int(score)}", False, BLACK_RGB)
    SCREEN.blit(score_text, (800,570))

    global score_obs_list
    score_obs_list = [(OBS_1_SCORE, 5), (OBS_2_SCORE, 5), (OBS_4, int(one_nine[ind_left])), (OBS_5, int(one_nine[ind_right]))]

    pygame.display.update()
    return (rect_left_arrow_1, rect_right_arrow_1)

def main():
    main_menu()
    score = 0
    ball = pygame.Rect(500, 500, 16, 16)
    global vx, vy, rand_range
    clock = pygame.time.Clock()
    running = True
    ind_left, ind_right = 0, 0

    # main loop
    while running:
        clock.tick(60) # 60 fps
        game_over = False

        # sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Arrow movement
        left_arrow, left_arrow_cords = LEFT_ARROW_1, (350,565)
        right_arrow, right_arrow_cords = RIGHT_ARROW_1, (550,565)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            left_arrow = LEFT_ARROW_3
            left_arrow_cords = (350,540)

        if keys_pressed[pygame.K_RIGHT]:
            right_arrow = RIGHT_ARROW_3
            right_arrow_cords = (550,540)

        # Colisões
        if ball.left <= 60 or ball.right >= 1000-60: # colisão com a barra esquerda e a direita 
            vx = vx*-1 + random.choice(rand_range)            
            if vy > 0:
                vy = round(math.sqrt(abs((in_vx ** 2 + in_vy ** 2) - vx ** 2)))
            else:
                vy = - round(math.sqrt(abs((in_vx ** 2 + in_vy ** 2) - vx ** 2)))

        if ball.top <= 25 or (ball.bottom >= 600-35 and (ball.right <= 350 or ball.left >= 600)): # colisão com o topo e chão 
            vy = round(vy*-1 + random.choice(rand_range))
            if vx > 0:
                vx = round(math.sqrt(abs((in_vx ** 2 + in_vy ** 2) - vy ** 2)))
            else:
                vx = - round(math.sqrt(abs((in_vx ** 2 + in_vy ** 2) - vy ** 2)))

        if ball.colliderect(draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords, ind_left, ind_right, score)[0]): # colision with the left arrow
            vy = abs(vy)

        if ball.colliderect(draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords, ind_left, ind_right, score)[1]): # colision with the right arrow
            vy = abs(vy)

        # Colisões com obstáculos
        for obs in obs_list_pink:
            if ball.colliderect(obs):
                if (negative(vx) <= ball.right - obs.left <= abs(vx) or negative(vx) <= ball.left - obs.right <= abs(vx)):
                    if vx < 0:
                        vx = abs(vx)
                    else:
                        vx = negative(vx)
                else:
                    if vy < 0:
                        vy = abs(vy)
                    else:
                        vy = negative(vy)

        # Scores
        for obs in score_obs_list:
            if ball.colliderect(obs[0]):
                score += obs[1]
                
                if obs[0] == OBS_4:
                    ind_left = functions.ind_plus_1_lap(one_nine, ind_left)

                if obs[0] == OBS_5:
                    ind_right = functions.ind_plus_1_lap(one_nine, ind_right)

        # Velocidades
        ball.x += vx
        ball.y -= vy

        # making sure that v doesn't reach stupid values:
        if abs(vx) > 9 or abs(vx) < 3 or abs(vy) > 9 or abs(vy) < 3:
            if vx > 0 and vy > 0:
                vx, vy = in_vx , in_vy
            elif vx < 0 and vy > 0:
                vx, vy = -in_vx, in_vy
            elif vx > 0 and vy < 0:
                vx, vy = in_vx, -in_vy
            else:
                vx, vy = -in_vx, -in_vy
        
        # perder o jogo
        if ball.y >= 600:
            game_lost(score)

if __name__ == '__main__':
    main()