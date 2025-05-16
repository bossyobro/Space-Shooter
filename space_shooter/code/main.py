import pygame
from random import randint, uniform
from db import *
class Player(pygame.sprite.Sprite): 
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('space_shooter/images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

        # transform test
        

        # mask
        self.mask = pygame.mask.from_surface(self.image)
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        self.rect.clamp_ip(pygame.FRect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = ((randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))))
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        
    
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()
class Meteor(pygame.sprite.Sprite):

    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.original_surf = surf
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 2000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(20,50)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        # rotation
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)

def collisions():
    global running, game_over
    collision_sprites = (pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask))
    if collision_sprites:
        running = False
        game_over = True

    
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

def display_score(current_time):
    text_surf = font.render(str(current_time), True, (255,240,255))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    screen.blit(text_surf, text_rect)
    pygame.draw.rect(screen, (255,240,255), text_rect.inflate(20,10).move(0,-8), 5, 10)


# Game setup

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set_icon will also change the Icon of the program
pygame.display.set_caption("Space Shooter")
running = True
score = 0
clock = pygame.time.Clock()

# Import
meteor_surf = pygame.image.load('space_shooter/images/meteor.png').convert_alpha()
laser_surf = pygame.image.load('space_shooter/images/laser.png').convert_alpha()
star_surf = pygame.image.load('space_shooter/images/star.png').convert_alpha()
font = pygame.font.Font('space_shooter/images/Oxanium-Bold.ttf', 40)


# Sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)  

# Custom events -> meteoer event

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 350)

  
while running:
    dt  = clock.tick(60) / 1000
    score = pygame.time.get_ticks()
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
    #Update
    all_sprites.update(dt)

    collisions()

    # Draw the game
    screen.fill('#3a2e3f')
    display_score(score)
    all_sprites.draw(screen)

    # Draw test
    pygame.display.update() 

if game_over:
    input_active = True
    input_text = ''
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color('lightskyblue3')
    input_color = color_inactive
    input_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 50, 300, 50)
    font_large = pygame.font.Font(None, 80)

    while input_active:
        screen.fill((20, 10, 30))  # Background color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False 
                    print(f"Player entered name: {input_text}")  
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Draw "Game Over" text
        game_over_surf = font_large.render("GAME OVER", True, (255, 50, 50))
        game_over_rect = game_over_surf.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
        enter_name_surf = font.render("Enter your name below: ", True, (255, 50, 50))
        enter_name_rect = game_over_surf.get_rect(center=(WINDOW_WIDTH//2 -55 , WINDOW_HEIGHT//2 - 10))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(enter_name_surf, enter_name_rect)

        # Draw input box
        pygame.draw.rect(screen, input_color, input_rect, 2)
        name_surf = font.render(input_text, True, (255, 255, 255))
        screen.blit(name_surf, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.update()

    if input_active == False:
        sql = "INSERT INTO scores (username, score) VALUES (%s, %s)" 
        vals = (input_text, score)
        mycursor.execute(sql,vals)
        dbconn.commit()

pygame.quit()