""" _________________________________________
/                                            \ 
| Implementation of the Space Invaders Game  |
|  Jeremy Bargy          2022                |
|  Remember to have fun!                     |
\____________________________________________/

attribute for png icons:
OUTER-SPACE.PNG --> <a href="https://www.flaticon.com/free-icons/space" title="space icons">Space icons created by Freepik - Flaticon</a>
SPACE-SHIP.PNG --> <a href="https://www.flaticon.com/free-icons/space-ship" title="space-ship icons">Space-ship icons created by Freepik - Flaticon</a>
ALIEN.PNG --> <a href="https://www.flaticon.com/free-icons/miscellaneous" title="miscellaneous icons">Miscellaneous icons created by Mayor Icons - Flaticon</a>
MISSILE.PNG --> <a href="https://www.flaticon.com/free-icons/bomb" title="bomb icons">Bomb icons created by Freepik - Flaticon</a>
LINE.PNG --> <a href="https://www.flaticon.com/free-icons/line" title="line icons">Line icons created by Ze Leah - Flaticon</a>
EXPLOSION (1).PNG --> <a href="https://www.flaticon.com/free-icons/explosion" title="explosion icons">Explosion icons created by Freepik - Flaticon</a>
EXPLOSION (2).PNG --> <a href="https://www.flaticon.com/free-icons/explosion" title="explosion icons">Explosion icons created by Good Ware - Flaticon</a>
DIAGONAL_LINE.PNG --> <a href="https://www.flaticon.com/free-icons/line" title="line icons">Line icons created by Freepik - Flaticon</a>
ALIEN (1).PNG --> <a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by smalllikeart - Flaticon</a>
UFO.PNG --> <a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Freepik - Flaticon</a>
SPACESHIP.PNG --> <a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Freepik - Flaticon</a>

attribute for background:
2352.jpg --> <a href='https://www.freepik.com/vectors/meteor'>Meteor vector created by vectorpouch - www.freepik.com</a>

attribute for sounds:
ZAPSPLAT_CARTOON_SCI_FI_BEAM --> Sound from Zapsplat.com

"""

# Import the required PYGAME module and save it to shorthand of PYG & RANDOM module & MATH module
import pygame as pyg
from pygame import mixer 
import random

# the pygame module needs to be initialized
pyg.init()
WIDTH = 1900
HEIGHT = 1000

# SET the display size of pygame to 1000 x 800
screen = pyg.display.set_mode( (WIDTH, HEIGHT) )
# SET the GAME title and icon
pyg.display.set_caption( "SPACE DEFENDERS" )
icon = pyg.image.load( "outer-space.png" )
pyg.display.set_icon( icon )

############################################################################
#                             FONT & TEXTS                                 #
############################################################################
# FONT FOR GAME TEXT
MAIN_FONT = pyg.font.Font('freesansbold.ttf', 69)
GAME_OVER_FONT = pyg.font.Font('freesansbold.ttf', 75)
MID_FONT = pyg.font.Font('freesansbold.ttf', 35)
CREDIT_FONT =  pyg.font.Font('freesansbold.ttf', 50)
# credits
attribute1 = "Credits"
programmer = "Programmer, Producer, & Director - Jeremy Bargy"
attribute2 = 'Space icons created by Freepik - Flaticon'
attribute3 = 'Space-ship icons created by Freepik - Flaticon'
attribute4 = 'Miscellaneous icons created by Mayor Icons - Flaticon' 
attribute5 = 'Bomb icons created by Freepik - Flaticon'             
attribute6 = 'Explosion icons created by Freepik - Flaticon'
attribute7 = 'Explosion icons created by Good Ware - Flaticon'
attribute8 = 'Meteor vector created by vectorpouch - www.freepik.com'
attribute9 = 'Sound from Zapsplat.com'
attribute10 = 'Alien icons created by smalllikeart'
attribute11 = "Spaceship icons created by Freepik"
attribute12 = 'Sound from Zapsplat.com'
# FUNCTIONALITY FOR GAME OVER TEXT
def game_over_text():
    over_text = GAME_OVER_FONT.render( "GAME OVER", True, ( 255, 0, 0) )
    screen.blit( over_text, ( WIDTH/2 - over_text.get_width()/2, 500 ) )
    return_text = MID_FONT.render("Press enter to return to main menu... ", True, (255, 0, 0 ))
    screen.blit( return_text, (WIDTH /2 - return_text.get_width()/2 , 600 ) ) 
# FUNCTIONALITY FORMAIN MENU TEXT
def main_menu_text():
    menu_text = MAIN_FONT.render("SPACE DEFENDER", True, (7, 34, 39) )
    screen.blit( menu_text, (WIDTH /2 - menu_text.get_width()/2, 250) )
    welcome_text = MAIN_FONT.render("We are under attack!", True, (7, 34, 39 ))
    screen.blit( welcome_text, (WIDTH /2 - menu_text.get_width()/2 - 45, 500))
    #INSTRUCTIONS FOR MAIN MENU OPTIONS
    controls_game_text = MID_FONT.render("Press left and right arrows to move ", True, (7, 34, 39 ))
    screen.blit( controls_game_text, (WIDTH /2 - menu_text.get_width()/2 , 650))
    fire_game_text = MID_FONT.render("Press the space bar to fire ", True, (7, 34, 39 ))
    screen.blit( fire_game_text, (WIDTH /2 - menu_text.get_width()/2 , 700))
    start_game_text = MID_FONT.render("Press enter to to enter the battle... ", True, (7, 34, 39 ))
    screen.blit( start_game_text, (WIDTH /2 - menu_text.get_width()/2 , 750))
    start_game_text = MID_FONT.render("Press C to view credits... ", True, (7, 34, 39 ))
    screen.blit( start_game_text, (WIDTH /2 - menu_text.get_width()/2 , 800))
# FUNCTIONALITY FOR CREDITS TEXT
def credit_text():
    main_text = GAME_OVER_FONT.render(attribute1, True, (7, 34, 39) )
    screen.blit( main_text, (WIDTH /2 - main_text.get_width()/2, 200) )
    attribute_text1 = MID_FONT.render( programmer, True, (7, 34, 39) )
    screen.blit( attribute_text1, (WIDTH /2 - attribute_text1.get_width()/2, 300 ) )
    attribute_text2 = MID_FONT.render( attribute2, True, (7, 34, 39) )
    screen.blit( attribute_text2, (WIDTH /2 - attribute_text2.get_width()/2, 300 + (35) ) )
    attribute_text3 = MID_FONT.render( attribute3, True, (7, 34, 39) )
    screen.blit( attribute_text3, ( WIDTH /2 - attribute_text3.get_width()/2, 300 + (35 * 2) ) )
    attribute_text4 = MID_FONT.render( attribute4, True, (7, 34, 39) )
    screen.blit( attribute_text4, ( WIDTH /2 - attribute_text4.get_width()/2, 300 + (35 * 3) ) )
    attribute_text5 = MID_FONT.render( attribute5, True, (7, 34, 39) )
    screen.blit( attribute_text5, ( WIDTH /2 - attribute_text5.get_width()/2, 300 + (35 * 4) ) )
    attribute_text6 = MID_FONT.render( attribute6, True, (7, 34, 39) )
    screen.blit( attribute_text6, ( WIDTH /2 - attribute_text6.get_width()/2, 300 + (35 * 5) ) )
    attribute_text7 = MID_FONT.render( attribute7, True, (7, 34, 39) )
    screen.blit( attribute_text7, ( WIDTH /2 - attribute_text7.get_width()/2, 300 + (35 * 6) ) )
    attribute_text8 = MID_FONT.render( attribute8, True, (7, 34, 39) )
    screen.blit( attribute_text8, ( WIDTH /2 - attribute_text8.get_width()/2, 300 + (35 * 7) ) )
    attribute_text9 = MID_FONT.render( attribute9, True, (7, 34, 39) )
    screen.blit( attribute_text9, ( WIDTH /2 - attribute_text9.get_width()/2, 300 + (35 * 8) ) )
    attribute_text10 = MID_FONT.render( attribute10, True, (7, 34, 39) )
    screen.blit( attribute_text10, ( WIDTH /2 - attribute_text10.get_width()/2, 300 + (35 * 9 ) ) )
    attribute_text11 = MID_FONT.render( attribute11, True, (7, 34, 39) )
    screen.blit( attribute_text11, ( WIDTH /2 - attribute_text11.get_width()/2, 300 + (35 * 10 ) ) )
    #INSTRUCTIONS TP RETURN TO MAIN MENU
    main_game_text = MID_FONT.render("Press enter to return to main menu...  ", True, (7, 34, 39 ))
    screen.blit( main_game_text, (WIDTH /2 - main_game_text.get_width()/2 , 300 + (35 * 12 ) ) )

############################################################################
#                           LOAD IMAGES                                    #
############################################################################
# SET the background of pygame
#BACKGROUND = pyg.image.load( os.path.join("assets", '2352.jpg') )
BACKGROUND = pyg.image.load( '2352.jpg' )
BACKGROUND = pyg.transform.scale( BACKGROUND, (1900, 1000) )
# CREATE PLAYER ICON
#PLAYER_IMG = pyg.image.load( os.path.join( 'assets', 'space-ship.png' ) )
PLAYER_IMG = pyg.image.load( 'space-ship.png' )
PLAYER_IMG = pyg.transform.scale( PLAYER_IMG, (60, 60) )
# CREATE MISSILE ICON
#MISSILE_IMG = pyg.image.load( os.path.join( 'assets', 'missile (1).png' ) )
MISSILE_IMG = pyg.image.load( 'missile (1).png' )
MISSILE_IMG = pyg.transform.rotate( MISSILE_IMG, (45) )
# CREATE ENEMY ICON
#ENEMY_IMG = pyg.image.load( os.path.join( "assets", 'alien.png' ) )
ENEMY_IMG = pyg.image.load( 'alien.png' )
ENEMY_IMG = pyg.transform.scale( ENEMY_IMG, (60, 60) ) 
ENEMY_IMG2 = pyg.image.load( 'alien (1).png' )
ENEMY_IMG2 = pyg.transform.scale( ENEMY_IMG2, (60, 60) )
ENEMY_IMG3 = pyg.image.load( 'ufo.png' )
ENEMY_IMG3 = pyg.transform.scale( ENEMY_IMG3, (60, 60) )
ENEMY_IMG4 = pyg.image.load( 'spaceship.png' )
ENEMY_IMG4 = pyg.transform.scale( ENEMY_IMG4, (60, 60) )
# CREATE LASER ICON
#LASER_IMG = pyg.image.load( os.path.join( "assets", "line.png"))
LASER_IMG = pyg.image.load( "line.png")
LASER_PIC = pyg.image.load("diagonal-line.png")
LASER_PIC = pyg.transform.rotate( LASER_PIC, (45) )
# CREATE EXPLODE ICONS
#EXPLODE_IMG =  pyg.image.load( os.path.join("assets", 'explosion (1).png' ) )
#EXPLODE_IMG2 =  pyg.image.load( os.path.join("assets", 'explosion (2).png' ) )
EXPLODE_IMG =  pyg.image.load( 'explosion (1).png' )
EXPLODE_IMG2 = pyg.image.load( 'explosion (2).png' )

###############################################################################
#                               SOUNDS                                        #
###############################################################################
# CREATE BACKGROUND SOUND
menu_music = "alexander_gastrell_dark_world_operating_table_drone_mood_atmosphere_007.mp3"
game_track_alpha = "music_zapsplat_game_music_action_agressive_pounding_tense_electro_synth_028.mp3"
game_track_beta = "music_zapsplat_game_music_action_mild_agressive_bass_synth_breakbeat_027.mp3"
game_track_charile = "music_zapsplat_game_music_action_dark_electro_lo_fi_dirty_025.mp3"
music_selection = {
                "main":menu_music,
                "game_track1": game_track_alpha,
                "game_track2": game_track_beta,
                "game_track3": game_track_charile
                }
# CREATE MISSILE SOUND
MISSILE_SOUND = mixer.Sound("cartoon_rocket_launch.mp3")
MISSILE_SOUND.set_volume(0.169)
# CREATE LASER SOUND
LASER_SOUND = mixer.Sound("zapsplat_cartoon_sci_fi_beam_001_64213.mp3")
LASER_SOUND.set_volume(0.169)
# CREATE EXPLOSION SOUND
EXPLOSION_SOUND = mixer.Sound("zapsplat_science_fictyion_explosion_puff_smoke_medium_001_45027.mp3")
EXPLOSION_SOUND.set_volume(0.9969)

###############################################################################
#                            GAME CLASSES                                     #
###############################################################################
# BLUEPRINT FOR FIRE PROJECTILES
class Projetile:
    def __init__(self, x, y, img, sound):
        self.x = x
        self.y = y
        self.img = img
        self.fire_sound = sound
        self.mask = pyg.mask.from_surface(self.img)

    def __str__(self):
        return "Projectile Object"

    def draw( self):
        screen.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

# BLUEPRINT FOR GAME OBJECTS
class Game_Obj:
    COOLDOWN = 60

    def __init__(self, x, y, x_change, y_change, health = 100):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.health = health
        self.obj_img = None
        self.fire_obj = None
        self.fire_sound = None
        self.explode_img = EXPLODE_IMG
        self.explode_img2 = EXPLODE_IMG2
        self.explode_sound = EXPLOSION_SOUND
        self.ammo = []
        self.cool_down = 0
        
    def __str__(self):
        return "Game Object"
    
    def draw(self):
        screen.blit(self.obj_img, (self.x, self.y) )
        for projectile in self.ammo:
            projectile.draw()

    def fire_move(self, velocity, obj):
        self.cooloff()
        for projectile in self.ammo:
           projectile.move(velocity)
           if projectile.off_screen(HEIGHT):
                self.ammo.remove(projectile)
           elif projectile.collision(obj):
                obj.health -= 15
                self.ammo.remove(projectile)
    
    def cooloff(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def get_width(self):
        return self.obj_img.get_width()

    def get_height(self):
        return self.obj_img.get_height()

# BLUEPRINT FOR PLAYER GAME OBJECT
class Player(Game_Obj):
    def __init__(self, x, y, x_change, y_change, health =100):
        super().__init__(x, y, x_change, y_change, health)
        
        self.obj_img = PLAYER_IMG
        self.fire_obj = MISSILE_IMG
        self.fire_sound = MISSILE_SOUND
        self.mask = pyg.mask.from_surface(self.obj_img)
        self.max_health = health
        
    def __str__(self):
        return "Player Object"

    def fire(self):
        if self.cool_down == 0:
            projectile = Projetile(self.x, self.y, self.fire_obj, self.fire_sound)
            projectile.fire_sound.play()
            self.ammo.append(projectile)
            self.cool_down += 1

    # fire obj movement logic
    def fire_move(self, velocity, objs):
        self.cooloff()
        # for fire obj available move with given velocity
        for projectile in self.ammo:
           projectile.move(velocity)
           # if fire obj leaves screen, remove fired obj
           if projectile.off_screen(HEIGHT):
                self.ammo.remove(projectile)
           else:
                #  if fire obj from fired objects makes collision
                for obj in objs:
                    if projectile.collision(obj):
                        self.explode_sound.play()
                        screen.blit(self.explode_img, (obj.x, obj.y))
                        screen.blit(self.explode_img2, (obj.x + 25, obj.y -15))
                        objs.remove(obj)
                        if projectile in self.ammo:
                            self.ammo.remove(projectile)

    # drwa functionality for player obj w/ health bar
    def draw( self):
        super().draw()
        self.healthbar()

    # heatlthbar functionality -> green bar over red bar w? width set to obj img width, green width set porpotionaly to health/max health
    def healthbar(self):
        pyg.draw.rect(screen, ( 255, 0, 0 ), ( self.x, self.y + self.obj_img.get_height() + 10, self.obj_img.get_width(), 10 ) )
        pyg.draw.rect(screen, ( 0, 255, 0 ), ( self.x, self.y + self.obj_img.get_height() + 10, self.obj_img.get_width() * (self.health / self.max_health), 10 ) )
        
# BLUEPRINT FOR ENEMY GAME OBJECTS
class Enemy(Game_Obj):
    enemy_type = {
        "alpha": (ENEMY_IMG),
        "beta": (ENEMY_IMG2),
        "charile": (ENEMY_IMG3),
        "delta": (ENEMY_IMG4)
        }

    def __init__(self, x, y, x_change, y_change, enemy, health =100):
        super().__init__(x, y, x_change, y_change, health)
        self.obj_img = self.enemy_type[enemy]
        self.fire_obj = LASER_PIC
        self.fire_sound = LASER_SOUND
        self.mask = pyg.mask.from_surface(self.obj_img)

    def __str__(self):
        return "Enemy Object"

    def fire(self):
        if self.cool_down == 0:
            projectile = Projetile(self.x, self.y, self.fire_obj, self.fire_sound)
            projectile.fire_sound.play()
            self.ammo.append(projectile)
            self.cool_down += 1

    def move(self):
        self.x += self.x_change

# CALCULATE MASKS FOR OVERLAPPING OFFSETS FOR COLLISION LOGIC
def collide( obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    #RETURN COORDINATE OF INTERSECTION OR NONE
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():

    # INITIALIZE GAME VARIABLES
    run = True

    music_choice = music_selection[random.choice( ["game_track1", "game_track2", "game_track3"] ) ]
    mixer.music.load(music_choice)
    mixer.music.play(-1)

    #score = 0
    lives = 3
    wave_length = 6
    level = 0
    lost = False
    lost_count = 0
    PLAYER_VELOCITY = 6.9
    fire_vel = 10
    enemy_list = []
    
    # CREATE PLAYER
    player = Player(925, 925, 0, 0)
    
    #REDRAW WINDOW
    def game_window():
            # CREATE LEVEL CAPTIONS & BACKGROUND
            screen.blit( BACKGROUND, ( 0, 0 ) )
            lives_label = MAIN_FONT.render( f"Lives: {lives}", True, ( 0, 255, 0 ) )
            level_label = MAIN_FONT.render( f"Level: {level}", True, ( 0,255,0 ) )
            screen.blit( lives_label, ( 10, 10) )
            screen.blit( level_label, ( WIDTH - level_label.get_width() - 10, 10) )
            # DRAW ENEMIES
            for enemy in enemy_list:
                enemy.draw()
            # DRAW PLAYER
            if player.health <= 0:
                player.health += 100
                player.draw()
            else:
                player.draw()

            # LOST TEXT
            if lost:
                game_over_text()
                for event in pyg.event.get():
                    if event.type == pyg.QUIT:
                        quit()

                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_RETURN:
                            main_menu()
            # UPDATE DISPLAY
            pyg.display.update()

    # GAME LEVEL LOGIC
    while run:
       
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                quit()

        if player.health <= 0:
            lives -= 1

        game_window()

        if lives <= 0:
            lost = True
            lost_count +=1
    
        if lost:
            if lost_count > 60 * 100:
                #run = False
                main_menu()
            else:
                continue

        if len(enemy_list) == 0:
            level += 1
            wave_length += 2
            for i in range(wave_length):
                direction = random.randint( 0, 1 )
                if direction == 0:
                    x_change = 2.69
                elif direction == 1:
                    x_change = -2.69
                bad_guy = Enemy( random.randrange( 10, 1800), random.randrange( -120, 60 ), x_change, 40, random.choice( ["alpha", "beta", "charile", "delta"] ) )
                enemy_list.append(bad_guy)

        # KEYBOARD CONTROL LOGIC
        keys = pyg.key.get_pressed()

        if keys[pyg.K_LEFT]:    #LEFT MOVEMENT
            player.x_change = (0-PLAYER_VELOCITY)
        #
        if keys[pyg.K_RIGHT]:   #RIGHT MOVEMENT
            player.x_change = PLAYER_VELOCITY
        # IF LEFT OR RIGHT KEY NOT PRESSED
        if keys[pyg.K_LEFT] == False and keys[pyg.K_RIGHT] == False:
            player.x_change = (0)
        #
        if keys[pyg.K_UP]:  #UP KEY PRESSES
            pass
        if keys[pyg.K_DOWN]: #DOWN KEY PRESS
            pass
        if keys[pyg.K_SPACE]: #SPACE BAR PRESS
            player.fire()
        
        # CALCULATE movement change amount for player  
        player.x += player.x_change
        # STOP player from leaving the screen with boundaries
        if player.x <=0:
            player.x= 0
        elif player.x >= 1839:
            player.x = 1839

        # CREATE ENEMIES
        for enemy in enemy_list[:]:
            enemy.move()
            enemy.fire_move(fire_vel, player)

            if random.randrange(0, 4 * 60) == 1:
                enemy.fire()

            # STOP enemy from leaving the screen with boundaries
            if enemy.x <=0:
                enemy.x_change = 2.69
                enemy.y += enemy.y_change
            elif enemy.x >= 1800:
                enemy.x_change = -2.69
                enemy.y += enemy.y_change

            if collide(enemy, player):
                player.health -= 69
                enemy_list.remove(enemy)
            elif enemy.y >= player.y:
                lives -= 1
                enemy_list.remove(enemy)

        player.fire_move((-fire_vel), enemy_list)
        
# CREDITS MENU FUNCTIONALITY
def credits():
    run = True
    mixer.music.load(music_selection["main"])
    mixer.music.play(-1)
    while run:

        # FILL CREDITS SCREEN AND ATTRIUTIONS
        screen.fill( (79, 189, 186) )
        credit_text()
        pyg.display.update()

        # CHECK FOR EVENTS TO QUIT OR GO TO MAIN MENU
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                quit()

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_RETURN:
                    main_menu()
            
# MAIN MENU FUNCTIONALITY
def main_menu():
    run = True
    
    mixer.music.load(music_selection["main"])
    mixer.music.play(-1)
        
    while run:
        
        # FILL MAIN MENU BACKGROUND AND MENU TEXT
        screen.fill( (79, 189, 186) )
        main_menu_text()
        pyg.display.update()

        # CHECK FOR EVENTS TO QUIT GAME, START GAME, OR SEE CREDITS
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                quit()

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_c:
                    credits()

                if event.key == pyg.K_RETURN:
                    main()

    pyg.quit()

# RUN PROGRAM
main_menu()