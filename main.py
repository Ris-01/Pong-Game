import pygame
import os
pygame.init()


BLACK = 0, 0, 0
WHITE = 255, 255, 255
WIDTH = 700
HEIGHT = 500
HANDLE_WIDTH = 15
HANDLE_HEIGHT = 120
FPS = 60
VEL = 5
BALL_RADIUS = 10
global LEFT_HANDLE_x
global LEFT_HANDLE_y 
global RIGHT_HANDLE_x
global RIGHT_HANDLE_y  
global SCORE_1 
global SCORE_2
    
global ball_direction 
global ball_direction_Y

LEFT_HANDLE_x =0
LEFT_HANDLE_y = HEIGHT/2 - HANDLE_HEIGHT/2
RIGHT_HANDLE_x = WIDTH - HANDLE_WIDTH
RIGHT_HANDLE_y = HEIGHT/2 - HANDLE_HEIGHT/2
SCORE_1 = 0
SCORE_2 = 0


left_handle = pygame.Rect(LEFT_HANDLE_x, LEFT_HANDLE_y, HANDLE_WIDTH, HANDLE_HEIGHT)
right_handle = pygame.Rect(RIGHT_HANDLE_x, RIGHT_HANDLE_y , HANDLE_WIDTH, HANDLE_HEIGHT)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

# fonts used 
SCORE_FONT = pygame.font.SysFont('Arial' , 40)
WIN_FONT = pygame.font.SysFont('Arial' , 80)

# importing sound
Pong_hit = pygame.mixer.Sound(os.path.join('Assets','Pong33.mp3'))
winnin_sound = pygame.mixer.Sound(os.path.join('Assets','Clapping.mp3')) 


def draw_window(left_handle, right_handle,X, Y, SCORE_1, SCORE_2):
    WIN.fill(BLACK)
    left_score = SCORE_FONT.render("Score " + str(SCORE_1) , 1 ,WHITE)
    right_score = SCORE_FONT.render("Score " + str(SCORE_2) , 1 ,WHITE)
    WIN.blit(left_score , (10, 10))
    WIN.blit(right_score , (WIDTH - right_score.get_width()-10, 10))
    pygame.draw.rect(WIN, WHITE, left_handle)
    pygame.draw.rect(WIN, WHITE, right_handle)
    pygame.draw.circle(WIN, WHITE, (X,Y), 10)
    
    pygame.display.update()


# Handles motion of the handle
def handle_motion(key_pressed, left_handle, right_handle ):
   
    if key_pressed[pygame.K_w] and left_handle.y-10 >=0:
        left_handle.y -= VEL
    if key_pressed[pygame.K_s] and left_handle.y + HANDLE_HEIGHT + 10 <= HEIGHT:
        left_handle.y +=VEL
    if key_pressed[pygame.K_UP] and right_handle.y - 10 >= 0:
        right_handle.y -= VEL
    if key_pressed[pygame.K_DOWN] and right_handle.y + HANDLE_HEIGHT +10 <= HEIGHT:
        right_handle.y += VEL



def Winner(text):
    winner = WIN_FONT.render(text, 1, WHITE)
    WIN.blit(winner, (WIDTH/2 - winner.get_width()/2, HEIGHT/2 - winner.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    
   


def main():
    ball_direction_Y = 0
    ball_direction = 5
    
    global LEFT_HANDLE_x
    global LEFT_HANDLE_y 
    global RIGHT_HANDLE_x
    global RIGHT_HANDLE_y  
    global SCORE_1 
    global SCORE_2
    LEFT_HANDLE_x =0
    LEFT_HANDLE_y = HEIGHT/2 - HANDLE_HEIGHT/2
    RIGHT_HANDLE_x = WIDTH - HANDLE_WIDTH
    RIGHT_HANDLE_y = HEIGHT/2 - HANDLE_HEIGHT/2
    SCORE_1 = 0
    SCORE_2 = 0
    
    X = WIDTH/2
    Y = HEIGHT/2 
   
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        

        # controls the Y direction of the ball
        if Y + BALL_RADIUS >= HEIGHT:
            Pong_hit.play()
            ball_direction_Y*=-1
        elif Y + BALL_RADIUS-10 <=0:
            Pong_hit.play()
            ball_direction_Y*=-1
    
        # contols the X direction of the ball
        if ball_direction >0:
            if X+ BALL_RADIUS > right_handle.x   and right_handle.y <Y< right_handle.y + HANDLE_HEIGHT/2:
                ball_direction*=-1
                ball_direction_Y= -4
                Pong_hit.play()
            if X+BALL_RADIUS > right_handle.x and right_handle.y+ HANDLE_HEIGHT/2  <Y< right_handle.y + HANDLE_HEIGHT:
                Pong_hit.play()
                ball_direction*=-1
                ball_direction_Y= 4

            if X+ BALL_RADIUS == right_handle.x and Y == right_handle.y + HANDLE_HEIGHT/2:
                Pong_hit.play()
                ball_direction*=-1

        if ball_direction <0:
            if X + BALL_RADIUS < left_handle.x + HANDLE_WIDTH +10 and left_handle.y <=Y<= left_handle.y + HANDLE_HEIGHT/2:
                Pong_hit.play()
                ball_direction*=-1
                ball_direction_Y= -4
            if X+ BALL_RADIUS < left_handle.x + HANDLE_WIDTH +10 and left_handle.y+HANDLE_HEIGHT/2  <=Y<= left_handle.y + HANDLE_HEIGHT:
                Pong_hit.play()
                ball_direction*=-1
                ball_direction_Y= 4        
            if X+ BALL_RADIUS == left_handle.x+ HANDLE_WIDTH+10 and Y == left_handle.y + HANDLE_HEIGHT/2:
                Pong_hit.play()
                ball_direction*=-1
         
        
        # This handles the scoring of right player
        if X > right_handle.x +HANDLE_WIDTH:
            SCORE_1 +=1
            X = WIDTH/2
            Y = HEIGHT/2
            ball_direction_Y = 0
            ball_direction=-5
            right_handle.y = RIGHT_HANDLE_y
            left_handle.y = LEFT_HANDLE_y
        
        # This handles the scoring of the left player 
        if X  < left_handle.x:
            SCORE_2 +=1
            X = WIDTH/2
            Y = HEIGHT/2
            ball_direction_Y = 0
            ball_direction = 5
            right_handle.y = RIGHT_HANDLE_y
            left_handle.y = LEFT_HANDLE_y
        

        if SCORE_1 >= 10:
            winnin_sound.play()
            Winner("Hurraah!! Left Wins")
            
            break
        if SCORE_2 >= 10:
            winnin_sound.play()
            Winner("Huraah!! Right Wins")
            
            break
        X +=ball_direction
        Y += ball_direction_Y
           
        key_pressed = pygame.key.get_pressed()
        draw_window(left_handle, right_handle,X, Y, SCORE_1, SCORE_2)
        handle_motion(key_pressed,left_handle, right_handle)
    main()  
        
if __name__ == "__main__":
    main() 