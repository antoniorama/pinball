import pygame, math, random

# Random module
rand_range = [-1, 0, 1]

SCREEN_SIZE = (1000,600)
pygame.display.set_caption('Pinball')

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)

BALL = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/bola.png')
vx, vy = 6, 6
in_vx, in_vy = 6, 6
ball_v = (vx, vy)
WALLS = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/base.png')

LEFT_ARROW_1 = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/left_1.png')
LEFT_ARROW_3= pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/left_3_f.png')

RIGHT_ARROW_1 = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/right_1.png')
RIGHT_ARROW_3 = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/right_3.png')

OBS_1 = pygame.Rect(250,100,35,150)
OBS_1_2 = pygame.Rect(350,100,35,150)
OBS_1_SCORE = pygame.Rect(285,175,75,2)
OBS_1_IMG, obs_1_img_cords = pygame.image.load('/Users/antoniorama/Desktop/LEIC/Scripts/pinball pygame/score_cross.png'), (292, 158)
OBS_1_IMG = pygame.transform.scale(OBS_1_IMG, (50,50))

OBS_2 = pygame.Rect(1000-350,100,35,150)
OBS_2_2 = pygame.Rect(1000-250,100,35,150)
OBS_2_SCORE = pygame.Rect(1000-350+35,175,75,2)
OBS_2_IMG, obs_2_img_cords = OBS_1_IMG, (693,158)
OBS_2_IMG = pygame.transform.scale(OBS_2_IMG, (50,50))

OBS_3 = pygame.Rect(475,150,50,50)

OBS_4 = pygame.Rect(150,350,100,100)

OBS_5 = pygame.Rect(1000-OBS_4.x-OBS_4.width, OBS_4.y, OBS_4.width, OBS_4.height)

obs_list = [OBS_1, OBS_1_2, OBS_2, OBS_2_2, OBS_3, OBS_4, OBS_5]
score_obs_list = [(OBS_1_SCORE, 10), (OBS_2_SCORE, 10)]
non_col_list = [(OBS_1_IMG, obs_1_img_cords), (OBS_2_IMG, obs_2_img_cords)]

# Colors
PINK_RGB = (255,20,147)
BLACK_RGB = (0,0,0)

# Text Variables

# Score
score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

def negative(x):
    if x <= 0:
        return x
    else:
        return -1 * x 

def draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords):
    global score

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
    for obs in obs_list:
        if obs == OBS_4 or obs == OBS_5:
            pygame.draw.rect(SCREEN, PINK_RGB, obs, 20)
        else:
            pygame.draw.rect(SCREEN, PINK_RGB, obs)


    for obs in non_col_list:
        SCREEN.blit(obs[0], obs[1])

    # Text stuff
    score_text = game_font.render(f"Score: {int(score)}", False, BLACK_RGB)
    SCREEN.blit(score_text, (800,570))
    pygame.display.update()
    return (rect_left_arrow_1, rect_right_arrow_1)

def main():
    ball = pygame.Rect(500, 500, 16, 16)
    global vx, vy, score, rand_range
    clock = pygame.time.Clock()
    running = True

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

        # colisões
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

        if ball.colliderect(draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords)[0]): # colision with the left arrow
            vy = abs(vy)

        if ball.colliderect(draw_screen(ball, left_arrow, left_arrow_cords, right_arrow, right_arrow_cords)[1]): # colision with the right arrow
            vy = abs(vy)

        # Colisões com obstáculos
        for obs in obs_list:
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
                score += obs[1] / 2

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
            running = False

        print(vx,vy)
    pygame.quit()

if __name__ == '__main__':
    main()