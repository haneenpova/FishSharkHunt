from fishClass import Fishy
import pygame as pg 
from keybinds import Keys
import random


def display_score():
    # current_time = pg.time.get_ticks()
    # print(current_time)
    current_time = int(pg.time.get_ticks()/ 1000) - start_time
    score_surf = text_font.render(f'score: {current_time}' , False, "green")
    score_rect = score_surf.get_rect(center = (400, 50))
    pg.draw.rect(window,"Pink",score_rect)      # rect's color
    window.blit(score_surf, score_rect)
    return current_time

#shark animation 
def shark_movements():
    pass


pg.init()

width, height = 800, 580
fps = 60
window = pg.display.set_mode((width, height))
caption = pg.display.set_caption("OHIO SHARKS") 

clock = pg.time.Clock()

# health_font = pg.font.SysFont("comisans", 70)

text_font = pg.font.Font(None, 60)

# health_font = text_font.render("health:", False, 'Black') 
# health_surf = health_font.get_rect(center = (400, 50))  

sea_surface = pg.image.load('G:\\files\\python projects\\ZeTeacher\\graphics\\underwater.png').convert_alpha()

game_active = False

start_time = 0

score = 0

fish = Fishy(
    surface =  pg.image.load("graphics\\fish.png").convert_alpha(),
    rect = pg.Rect(400, 300, 250, 200)

) 
# fish_surface = pg.image.load('D:\\files\\projects\\ZeTeacher\\graphics\\fish.png').convert_alpha()
# fish_surface2 = pg.transform.scale(fish_surface, (250,200))
# fish_rect = fish_surface2.get_rect(bottomright = (600, 500))

shark = Fishy(
    surface = pg.image.load('graphics\\shark2.png').convert_alpha(),
    rect = pg.Rect(40, 265, 290, 270)
)


# shark_surface = pg.image.load('D:\\files\\projects\\ZeTeacher\\graphics\\shark2.png').convert_alpha() #convert_alpha removes the white blocks
# shark2_surface = pg.transform.scale(shark_surface, (290,270))

shark_transformed = pg.transform.scale(shark.surface, (shark.rect.width, shark.rect.height ))

# shark_rect = shark1_surface2.get_rect(bottomleft = (60, 500))

# text_surface = text.render('health', False, "Black")
# fish_x_pos = 350
shark_x_pos = 4

fish_gravity = 0
shark_gravity = 0

shark_y_direction = 0

# shark intro 
shark_intro = pg.image.load('graphics\\shark_into.png').convert_alpha()
shark_intro_scaled = pg.transform.scale(shark_intro, (300,370))
shark_intro_rect = shark_intro_scaled.get_rect(center = (400, 300)) 

# GAME FONT
game_name = text_font.render("Welcome to Ohio Sharks", False, (255, 153, 153)) 
game_name_rect = game_name.get_rect(center = (420, 50))

game_msg = text_font.render("press enter to start", False, (255, 153, 153)) 
game_msg_rect = game_msg.get_rect(center = (400, 500))

#game animation
keys = {

    ord("w"):False,
    ord("s"):False,
    ord("d"):False,
    ord("a"):False,
    pg.K_SPACE:False
        }

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
        if event.type == pg.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
    

        elif event.type == pg.KEYUP:
            if event.key in keys:
                keys[event.key] = False
                

    window.blit(sea_surface, (0,0))

 #fishy animation    
    if keys[ord("s")]:
        if fish_gravity >= 0:
            fish.rect.y += 1
            # print("s")

    if keys [ord("d")]:
        if fish_gravity >= 0:
            fish.rect.x += 1
            # print("d")
        
    if keys [ord("w")]:
        if fish_gravity <= 0:
            fish.rect.x += 1
            fish.rect.y -= 1
            # print("w")
    
    if keys [ord("a")]:
        if fish_gravity >= 0:
            fish.rect.x -= 2
            # print("a")

#shark animation 
    # current_time = int(pg.time.get_ticks()/ 1000) - start_time
    # if current_time % 2:
    random_num = random.randint(1, 1000)
    if shark.rect.top < 50:
        shark_y_direction = 1
    elif shark.rect.bottom > 540:
        shark_y_direction = -1

    elif random_num >  990:
        shark_y_direction = 1
    elif random_num > 980:
        shark_y_direction = -1
    
    
    shark.rect.y += shark_y_direction


    # if keys[ord("s")]:
    #     if shark_gravity >= 0:
    #         shark.rect.y += 3
    #         # print("s")

    # if keys [ord("d")]:
    #     if shark_gravity >= 0:
    #         shark.rect.x += 3
    #         # print("d")
        
    # if keys [ord("w")]:
    #     if shark_gravity <= 0:
    #         shark.rect.x += 2
    #         shark.rect.y -= 2
    #         # print("w")
    
    # if keys [ord("a")]:
    #     if shark_gravity >= 0:
    #         shark.rect.x -= 3
    #         # print("a")

   #restarting game 
    if keys[pg.K_SPACE]:
        fish.rect.x = 400
        shark.rect.x = 40
        game_active = True
        start_time =  int(pg.time.get_ticks()/ 1000)
        

    # fish_health = health_font.render("Health", True, health_surf) #"Health: ", True , (0,0,0)
    if game_active:
        # pg.draw.rect(window, "Pink", health_surf)
        # window.blit(health_font, health_surf )
        

        window.blit(fish.surface, fish.rect)
        fish.rect.x += 3
        if fish.rect.left > 800: 
            fish.rect.right = 50


        # window.blit(shark.surface, shark.rect)
        window.blit(shark_transformed, shark.rect)
        shark.rect.x +=4
        if shark.rect.left > 800: 
            shark.rect.right = 40
        score = display_score()
    

    # window.blit(fish_surface2, (fish_x_pos,300))
    # fish_x_pos += 3
    # if fish_x_pos > 800:
    #     fish_x_pos = 50

    # window.blit(shark1_surface2,(shark_x_pos,250))
    # shark_x_pos +=3
    # if shark_x_pos > 800:
    #     shark_x_pos = 40

    # if print(fish.rect.colliderect(shark.rect)):
    #     print("collision")
        # collision
     
    
        # if shark.rect == fish.rect:
        if shark.rect.colliderect(fish.rect):
            print("collision")
            game_active = False
        

    else:
        window.fill("Blue")
        window.blit(shark_intro_scaled, shark_intro_rect)
        score_msg = text_font.render(f'your score: {score}' , False, "green")
        score_msg_rect = score_msg.get_rect(center = (400, 50) )
        window.blit(game_msg, game_msg_rect)

        if score == 0:
            window.blit(game_name, game_name_rect)
        else:
            window.blit(score_msg, score_msg_rect)
    
    pg.display.update()
    clock.tick(fps)

            







