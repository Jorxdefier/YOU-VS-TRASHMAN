# Name: Jordan Strand
# Date: June. 04, 2021
# Class: ICS3U1
# Description: This is the final summative, Jordan feels like he's gonna have a bad time
# Creating the user input to start the game.
print("HELLO, welcome to my game of YOU VS. TRASHMAN. \nIn this game you are tasked with defeating the evil Business trashman, \nwho won't stop polluting, so you'd better stop him! \nTo play, you move your character around \nwith the arrow keys, avoiding the trash. \nThe mouse is not required for this game. \nTo select either 'fight' or 'heal', press the enter key.")
print("------------------------------------")
# Making it so that the game won't start until you press 'ENTER'
start = " "
while start != "":
    start = input("Read over the rules to play the game, \nif you are ready for a bad time, press ENTER: ")
    if start != "":
        print("Why don't you wanna play the game? \nTry again")
if start == "":
    print("Thank you for pressing start, \nprepare yourself!")    
# Starting to create the game by importing modules, and defining the borders
import pygame, math, random
pygame.init()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
width = 800
height = 600
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("YOU-VS-TRASHMAN")
# List for where the border is
border_values = [310, 288, 490, 468]
# Opening a file to get the information for the main character, and appending it to a list. This is so that if someone wants to change some aspects of the heart, instead of changing the whole code, they can just change the file values
heart_values = []
heart = open("StrandMainCharacter.txt", "r")
while start == "":
    values = heart.readline()
    values = values.rstrip("\n")
    heart_values.append(values)
    if values == "":
        break
    if int(values) >= 0:
        for i in range(2, int(values)):
            if (int(values)) >= 0:
                heart_values.append(values)
                break
# Drawing the scenes. These will be all the pygame-drawn assets throughout my game
def drawHeart(location, y, colour): 
    pygame.draw.rect(screen, BLACK, (location-11, y-int(heart_values[6]), 22, 22))
    pygame.draw.circle(screen, colour, (location+int(heart_values[1]), y), int(heart_values[1]))
    pygame.draw.circle(screen, colour, (location-int(heart_values[1]), y), int(heart_values[1]))
    pygame.draw.polygon(screen, colour, ([location+int(heart_values[3]), y+int(heart_values[5])], [location-int(heart_values[3]), y+int(heart_values[5])], [location, y+int(heart_values[6])]))    
def border(a, b, c, d):
    pygame.draw.rect(screen, WHITE, (a, b, c, d), int(heart_values[1]))
def buttons(e, f, g, h):
    pygame.draw.rect(screen, ORANGE, (e, f, g, h))
def PaperBalls(random_place):
    if random_place_true == 1:
        pygame.draw.circle(screen, BLACK, (450-random_place,(300+n)-1), 13)
        pygame.draw.circle(screen, WHITE, (450-random_place,300+n), 13)
        pygame.draw.line(screen, BLACK, (445-random_place,300+n), (440-random_place,295+n), 3)
        pygame.draw.line(screen, BLACK, (445-random_place,300+n), (442-random_place,308+n), 3)
        pygame.draw.line(screen, BLACK, (455-random_place,289+n), (450-random_place,300+n), 3)    
        pygame.draw.circle(screen, BLACK, (350+random_place,(300+n)-1), 13)
        pygame.draw.circle(screen, WHITE, (350+random_place,300+n), 13)
        pygame.draw.line(screen, BLACK, (345+random_place,300+n), (340+random_place,295+n), 3)
        pygame.draw.line(screen, BLACK, (345+random_place,300+n), (342+random_place,308+n), 3)
        pygame.draw.line(screen, BLACK, (355+random_place,289+n), (350+random_place,300+n), 3) 
    elif random_place_true == 2:
        pygame.draw.circle(screen, BLACK, (450+random_place,(300+n)-1), 13)
        pygame.draw.circle(screen, WHITE, (450+random_place,300+n), 13)
        pygame.draw.line(screen, BLACK, (445+random_place,300+n), (440+random_place,295+n), 3)
        pygame.draw.line(screen, BLACK, (445+random_place,300+n), (442+random_place,308+n), 3)
        pygame.draw.line(screen, BLACK, (455+random_place,289+n), (450+random_place,300+n), 3)    
        pygame.draw.circle(screen, BLACK, (350-random_place,(300+n)-1), 13)
        pygame.draw.circle(screen, WHITE, (350-random_place,300+n), 13)
        pygame.draw.line(screen, BLACK, (345-random_place,300+n), (340-random_place,295+n), 3)
        pygame.draw.line(screen, BLACK, (345-random_place,300+n), (342-random_place,308+n), 3)
        pygame.draw.line(screen, BLACK, (355-random_place,289+n), (350-random_place,300+n), 3)         
    pygame.draw.circle(screen, BLACK, (400,(300+n)-1), 13)
    pygame.draw.circle(screen, WHITE, (400,300+n), 13)
    pygame.draw.line(screen, BLACK, (400,295+n), (410,305+n), 3)
    pygame.draw.line(screen, BLACK, (400,295+n), (390,305+n), 3)    
def PaperBalls2(random_place):  
    if random_place_true == 1:
        pygame.draw.circle(screen, BLACK, (400+random_place,(300+n)-1), 12)
        pygame.draw.circle(screen, WHITE, (400+random_place,300+n), 12)        
        pygame.draw.circle(screen, BLACK, ((300+n)-1,400+random_place), 12)
        pygame.draw.circle(screen, WHITE, (300+n,400+random_place), 12)
        pygame.draw.circle(screen, BLACK, ((500-n)+1,400+random_place), 12)
        pygame.draw.circle(screen, WHITE, (500-n,400+random_place), 12)
        pygame.draw.circle(screen, BLACK, (400+random_place,(500-n)+1), 12)
        pygame.draw.circle(screen, WHITE, (400+random_place,500-n), 12)        
    if random_place_true == 2:
        pygame.draw.circle(screen, BLACK, (400-random_place,(300+n)-1), 12)
        pygame.draw.circle(screen, WHITE, (400-random_place,300+n), 12)        
        pygame.draw.circle(screen, BLACK, ((300+n)-1,400-random_place), 12)
        pygame.draw.circle(screen, WHITE, (300+n,400-random_place), 12)
        pygame.draw.circle(screen, BLACK, ((500-n)+1,400-random_place), 12)
        pygame.draw.circle(screen, WHITE, (500-n,400-random_place), 12)        
        pygame.draw.circle(screen, BLACK, (400-random_place,(500-n)+1), 12)
        pygame.draw.circle(screen, WHITE, (400-random_place,500-n), 12)    
def Earth(random_position):
    if random_position == 1:
        pygame.draw.circle(screen, BLACK, (400,(300+n)-1), 50)
        pygame.draw.circle(screen, BLUE, (400,300+n), 50)
        pygame.draw.polygon(screen, GREEN, ([365,290+n], [390,270+n], [390,310+n]))
        pygame.draw.polygon(screen, GREEN, ([390,310+n], [385,330+n], [395,320+n]))
        pygame.draw.polygon(screen, GREEN, ([410,300+n], [420,290+n], [420,320+n]))
        pygame.draw.polygon(screen, GREEN, ([420,290+n], [430,270+n], [435,280+n]))
    if random_position == 2:
        pygame.draw.circle(screen, BLACK, (400+50,(300+n)-1), 50)
        pygame.draw.circle(screen, BLUE, (400+50,300+n), 50)
        pygame.draw.polygon(screen, GREEN, ([365+50,290+n], [390+50,270+n], [390+50,310+n]))
        pygame.draw.polygon(screen, GREEN, ([390+50,310+n], [385+50,330+n], [395+50,320+n]))
        pygame.draw.polygon(screen, GREEN, ([410+50,300+n], [420+50,290+n], [420+50,320+n]))
        pygame.draw.polygon(screen, GREEN, ([420+50,290+n], [430+50,270+n], [435+50,280+n]))
    if random_position == 3:
        pygame.draw.circle(screen, BLACK, (400-50,(300+n)-1), 50)
        pygame.draw.circle(screen, BLUE, (400-50,300+n), 50)
        pygame.draw.polygon(screen, GREEN, ([365-50,290+n], [390-50,270+n], [390-50,310+n]))
        pygame.draw.polygon(screen, GREEN, ([390-50,310+n], [385-50,330+n], [395-50,320+n]))
        pygame.draw.polygon(screen, GREEN, ([410-50,300+n], [420-50,290+n], [420-50,320+n]))
        pygame.draw.polygon(screen, GREEN, ([420-50,290+n], [430-50,270+n], [435-50,280+n]))              
def TrashCan():
    pygame.draw.rect(screen, BLACK, ((310+n)-1,280,20,160))
    pygame.draw.circle(screen, BLACK, (310+n,420), 10)
    pygame.draw.circle(screen, BLACK, (310+n,400), 10)
    pygame.draw.circle(screen, BLACK, (310+n,380), 10)
    pygame.draw.circle(screen, BLACK, (310+n,360), 10)
    pygame.draw.circle(screen, BLACK, (310+n,340), 10)
    pygame.draw.circle(screen, BLACK, (310+n,320), 10)
    pygame.draw.circle(screen, BLACK, (310+n,300), 10)
    pygame.draw.rect(screen, GREY, (310+n,280,20,160))
    pygame.draw.line(screen, BLACK, (320+n,280), (320+n,440), 2)
    pygame.draw.circle(screen, BLACK, ((320+n)-1,440), 10)
    pygame.draw.circle(screen, GREY, (320+n,440), 10)
    pygame.draw.circle(screen, BLACK, ((320+n)-1,470), 10)
    pygame.draw.circle(screen, GREY, (320+n,470), 10)  
myClock = pygame.time.Clock()
running = True
x = 200
y = 550
# Importing text and images
fontLoad = pygame.font.SysFont("Comic Sans MS",30)
fontSecondLoad = pygame.font.SysFont("Comic Sans MS",20)
loading_screen = fontLoad.render("Welcome to my Game!", 1, (255, 255, 255))
loading = fontSecondLoad.render("Use the arrow keys to move your character,", 1, (255, 255, 255))
second_loading = fontSecondLoad.render("press enter to either attack or heal!", 1, (255, 255, 255))
third_loading = fontSecondLoad.render("Avoid the trash at all costs!", 1, (255, 255, 255))
screen.blit(loading_screen, pygame.Rect(50,100,50,50))
screen.blit(loading, pygame.Rect(50,180,50,50))
screen.blit(second_loading, pygame.Rect(50,210,50,50))
screen.blit(third_loading, pygame.Rect(50,240,50,50))
pygame.display.flip()
pygame.time.wait(6000)
pygame.draw.rect(screen, BLACK, (0, 0, 800, 600))
border(300, 280, 200, 200)
businessmanPic = pygame.image.load("Strandbusinessman.jpg")
businessmanPic = pygame.transform.scale(businessmanPic, (150, 150))
screen.blit(businessmanPic, pygame.Rect(320,128,20,20))
pygame.display.flip()
pygame.time.wait(1000)
SpeechBubble = pygame.image.load("StrandSpeechBubble.png")
SpeechBubble = pygame.transform.scale(SpeechBubble, (240, 150))
screen.blit(SpeechBubble, pygame.Rect(440,70,30,30))
pygame.display.flip()
pygame.time.wait(500)
explosion = pygame.image.load("StrandExplosion.jpg")
explosion = pygame.transform.scale(explosion, (150, 150))
# Making and rendering some text
fontBusiness = pygame.font.SysFont("Comic Sans MS",12)
fontAct = pygame.font.SysFont("Comic Sans MS",20)
fontHealth = pygame.font.SysFont("Comic Sans MS",30)
fontWin = pygame.font.SysFont("Comic Sans MS",100)
fontLose = pygame.font.SysFont("Comic Sans MS",50)
fontLoseSub = pygame.font.SysFont("Comic Sans MS",20)
fontEpicWin = pygame.font.SysFont("Comic Sans MS",20)
miss = fontHealth.render("YOU MISSED", 1, (255, 255, 255))
fight = fontAct.render("FIGHT", 1, (255, 255, 255))
heal = fontAct.render("HEAL", 1, (255, 255, 255))
text = fontBusiness.render("Haha, I am an evil trash business man!", 1, (0, 0, 0))
new_text = fontBusiness.render("I'm gonna keep polluting a whole ton!", 1, (0, 0, 0))
screen.blit(text, pygame.Rect(450,100,50,50))
screen.blit(new_text, pygame.Rect(450,120,50,50))
pygame.display.flip()
pygame.time.wait(50)
# Using a sound to make it sound like he's talking in the begining
Talking = pygame.mixer.Sound("StrandTalking.wav")
Talking.play()
for count in range(10):
    pygame.time.wait(100)
    Talking.play()
pygame.display.flip()
pygame.time.wait(2000)
# Playing the song
Megalovania = pygame.mixer.Sound("StrandMegalovania.wav")
Megalovania.play()
pygame.draw.rect(screen, BLACK, (440,50,250,152))
buttons(100,520,200,50)
buttons(500,520,200,50)
screen.blit(fight, pygame.Rect(110,530,200,50))
screen.blit(heal, pygame.Rect(510,530,200,50))
pygame.display.flip()
pygame.time.wait(50)
# Some game states
key_left = False
key_right = False
key_up = False
key_down = False
# The main game loop, some sounds, and making counters to tell the game when to switch phases, and what the damage is. Also making the text to see what the enemies health is, and see what yours is. Also making the health bars.
counter = 0
your_health = 100
enemy_health = 100
enemy_current_health = fontHealth.render("TRASHMAN HP: %i"%(enemy_health), 1, (255, 255, 255))
your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
screen.blit(enemy_current_health, pygame.Rect(50,50,100,100))
screen.blit(your_current_health, pygame.Rect(500,50,100,100))
def healthBar(i, j, which_health):
    pygame.draw.rect(screen, WHITE, (i,88,104,30))
    pygame.draw.rect(screen, RED, (j,90,100,25))
    pygame.draw.rect(screen, GREEN, (j,90,which_health,25))
healthBar(78, 80, enemy_health)
healthBar(528, 530, your_health)
Ping = pygame.mixer.Sound("StrandPing.wav")
Hurt = pygame.mixer.Sound("StrandTakingDamage.wav")
Enemy_hurt = pygame.mixer.Sound("StrandInflictingDamage.wav")
Recovery = pygame.mixer.Sound("StrandRecovery.wav")
dead_music = pygame.mixer.Sound("StrandDeadMusic.wav")
Congratulations = pygame.mixer.Sound("StrandCongratulations.wav")
win = 0
lose = 0
n = 1
attack_phase = 0
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
# Seeing whether the key is pressed down or not
        if evnt.type == pygame.KEYDOWN and (counter%2) != 0:
            if evnt.key == pygame.K_LEFT:
                key_left = True
            if evnt.key == pygame.K_RIGHT:
                key_right = True
            if evnt.key == pygame.K_UP:
                key_up = True
            if evnt.key == pygame.K_DOWN:
                key_down = True
# Making character move for attack stage and heal stage
        if evnt.type == pygame.KEYDOWN and (counter%2) == 0:
            keys = pygame.key.get_pressed()
            if x == 200:
                if keys[pygame.K_RIGHT]:
                    x = x + 400
                    pygame.draw.rect(screen, ORANGE, (x-411,y-10,22,22))
                    Ping.play()                
            if x == 600:
                if keys[pygame.K_LEFT]:
                    x = x - 400
                    pygame.draw.rect(screen, ORANGE, (x+389,y-10,22,22))
                    Ping.play()                         
# This is the heal button. I'm making it so that if the player's health is less than 100, they have the option to heal themselves if the heart is over the optional button
            if evnt.key == pygame.K_RETURN and x == 600 and your_health < 100:
                Recovery.play()
                random_number = random.randint(5,10)
                your_health += random_number
                your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
                pygame.draw.rect(screen, BLACK, (650,50,55,40))
                screen.blit(your_current_health, pygame.Rect(500,50,100,100))
                healthBar(528, 530, your_health)               
                counter += 1
                x = 400
                y = 400
                pygame.draw.rect(screen, BLACK, (0,500,800,100))
                attack_phase = random.randint(1,4)
# This is the attack button. I'm making it so that if they press this button, they will attack the enemy and initiate the attack phase
            if evnt.key == pygame.K_RETURN and x == 200:
                Ping.play()
                hit_or_miss = random.randint(1,100)
                # Having a random chance for you to miss your attack, a five percent chance to be exact
                if hit_or_miss <= 95:                
                    random_number = random.randint(5,15) # This decides how much damage you do
                    enemy_health -= random_number
                    enemy_current_health = fontHealth.render("TRASHMAN HP: %i"%(enemy_health), 1, (255, 255, 255))
                    pygame.draw.line(screen, RED, (450,170), (330,250), 5)
                    Enemy_hurt.play()
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    pygame.draw.rect(screen, BLACK, (320,128,150,150))
                    pygame.display.flip()
                    pygame.time.wait(200)                
                    screen.blit(businessmanPic, pygame.Rect(320,128,20,20))
                    pygame.display.flip()
                    pygame.time.wait(200)                 
                    pygame.draw.rect(screen, BLACK, (320,128,150,150))
                    pygame.display.flip()
                    pygame.time.wait(200)                               
                    screen.blit(businessmanPic, pygame.Rect(320,128,20,20))
                    pygame.draw.rect(screen, BLACK, (290,50,55,50))
                    screen.blit(enemy_current_health, pygame.Rect(50,50,100,100))
                    healthBar(78, 80, enemy_health)
                if hit_or_miss > 95: # If you miss, you do no damage
                    screen.blit(miss, pygame.Rect(600,300,200,50))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    pygame.draw.rect(screen, BLACK, (600,300,200,50))
                if enemy_health <= 0:
                    win += 1
                    running = False
                counter += 1
                x = 400
                y = 400
                pygame.draw.rect(screen, BLACK, (0,500,800,100))
                attack_phase = random.randint(1,4)
                # These numbers down here indicate whether to move certain attacks in a random position, so that the player doesn't get used to the same four attacks, because they're different everytime
                random_place_true = random.randint(1,2)
                random_place = random.randint(0,20)
                random_position = random.randint(1,3)
  # This is checking whether the player should be moving or not              
        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_LEFT:
                key_left = False
            if evnt.key == pygame.K_RIGHT:
                key_right = False
            if evnt.key == pygame.K_UP:
                key_up = False
            if evnt.key == pygame.K_DOWN:
                key_down = False
# Making the character move for defense stage, and also having it so that depending on the attack phase, the enemy will do diferent attacks based on what phase that is.
   # This is the paperballs collision section
    if attack_phase == 1 and (counter%2) != 0:
        if random_place_true == 1:
            paper1_distance = math.hypot(400 - x, 300+n - y)
            paper2_distance = math.hypot(450-random_place - x, 300+n - y)
            paper3_distance = math.hypot(350+random_place - x, 300+n - y)
        if random_place_true == 2:
            paper1_distance = math.hypot(400 - x, 300+n - y)
            paper2_distance = math.hypot(450+random_place - x, 300+n - y)
            paper3_distance = math.hypot(350-random_place - x, 300+n - y)            
        if paper1_distance <= 5 + 13 or paper2_distance <= 5 + 13 or paper3_distance <= 5 + 13:
            Hurt.play()
            your_health -=1
            your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
            pygame.draw.rect(screen, BLACK, (650,50,55,40))
            screen.blit(your_current_health, pygame.Rect(500,50,100,100))
            healthBar(528, 530, your_health)
            if your_health <= 0:
                lose += 1
                running = False
   # This is the other collision detector         
    elif attack_phase == 2 and (counter%2) != 0:
        if random_place_true == 1:
            paper4_distance = math.hypot(400+random_place - x, 300+n - y)
            paper5_distance = math.hypot(300+n - x, 400+random_place - y)
            paper6_distance = math.hypot(500-n - x, 400+random_place - y)
            paper7_distance = math.hypot(400+random_place - x, 500-n - y)
        if random_place_true == 2:
            paper4_distance = math.hypot(400-random_place - x, 300+n - y)
            paper5_distance = math.hypot(300+n - x, 400-random_place - y)
            paper6_distance = math.hypot(500-n - x, 400-random_place - y)               
            paper7_distance = math.hypot(400-random_place - x, 500-n - y)
        if paper4_distance <= 5 + 12 or paper5_distance <= 5 + 12 or paper6_distance <= 5 + 12 or paper7_distance <= 5 + 12:
            Hurt.play()
            your_health -=1
            your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
            pygame.draw.rect(screen, BLACK, (650,50,55,40))
            screen.blit(your_current_health, pygame.Rect(500,50,100,100))
            healthBar(528, 530, your_health)
            if your_health <= 0:
                lose += 1
                running = False
# This is the third attack phase collision detector
    elif attack_phase == 3 and (counter%2) != 0:
        if random_position == 1:
            distance = math.hypot(400 - x, 300+n - y)
        if random_position == 2:
            distance = math.hypot(450 - x, 300+n - y)
        if random_position == 3:
            distance = math.hypot(350 - x, 300+n - y)
        if distance <= 5 + 50:
            Hurt.play()
            your_health -=1
            your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
            pygame.draw.rect(screen, BLACK, (650,50,55,40))
            screen.blit(your_current_health, pygame.Rect(500,50,100,100))
            healthBar(528, 530, your_health)
            if your_health <= 0:
                lose += 1
                running = False  
# This is the fourth attack phase hit detection
    elif attack_phase == 4 and (counter%2) != 0:
        bar_distance = math.hypot(320+n - x, 440 - y)
        circle_distance = math.hypot(320+n - x, 470 - y)
        circle2_distance = math.hypot(310+n - x, 420 - y)
        circle3_distance = math.hypot(310+n - x, 400 - y)
        circle4_distance = math.hypot(310+n - x, 380 - y)
        circle5_distance = math.hypot(310+n - x, 360 - y)
        circle6_distance = math.hypot(310+n - x, 340 - y)
        circle7_distance = math.hypot(310+n - x, 320 - y)
        circle8_distance = math.hypot(310+n - x, 300 - y)
        if bar_distance <= 5 + 8 or circle_distance <= 5 + 8 or circle2_distance <= 5 + 10 or circle3_distance <= 5 + 10 or circle4_distance <= 5 + 10 or circle5_distance <= 5 + 10 or circle6_distance <= 5 + 10 or circle7_distance <= 5 + 10 or circle8_distance <= 5 + 10:
            Hurt.play()
            your_health -=1
            your_current_health = fontHealth.render("YOUR HP: %i"%(your_health), 1, (255, 255, 255))
            pygame.draw.rect(screen, BLACK, (650,50,55,40))
            screen.blit(your_current_health, pygame.Rect(500,50,100,100))
            healthBar(528, 530, your_health)
            if your_health <= 0:
                lose += 1
                running = False            
# This is attack phase 1, this phase has three paperballs coming down from the sky at you
    if (counter%2) != 0 and attack_phase == 1:
        if key_left == True:
            x -= 1           
        if key_right == True:
            x += 1           
        if key_up == True:
            y -= 1           
        if key_down == True:
            y += 1
        if n == 160 or n > 160:
            buttons(100,520,200,50)
            buttons(500,520,200,50)
            screen.blit(fight, pygame.Rect(110,530,200,50))
            screen.blit(heal, pygame.Rect(510,530,200,50))
            pygame.draw.rect(screen, BLACK, (300,280,200,200))
            x = 200
            y = 550
            n = 0
            counter += 1
        n += 1
        PaperBalls(random_place)
        if n == 1:
            pygame.draw.rect(screen, (BLACK), (290,280,220,220))
# This is attack phase 2, this takes the familliar paper balls from before, and adds a twist to them        
    if (counter%2) != 0 and attack_phase == 2:
        if key_left == True:
            x -= 1          
        if key_right == True:
            x += 1           
        if key_up == True:
            y -= 1       
        if key_down == True:
            y += 1
        if n == 200 or n > 200:
            buttons(100,520,200,50)
            buttons(500,520,200,50)
            screen.blit(fight, pygame.Rect(110,530,200,50))
            screen.blit(heal, pygame.Rect(510,530,200,50))
            pygame.draw.rect(screen, BLACK, (300,280,200,200))
            x = 200
            y = 550
            n = 0
            counter += 1
        n += 1
        PaperBalls2(random_place)
        if n == 1:
            pygame.draw.rect(screen, (BLACK), (285,280,230,235))        
# This is attack phase 3, it draws a big earth which you then have to avoid            
    if (counter%2) != 0 and attack_phase == 3:
        if key_left == True:
            x -= 1         
        if key_right == True:
            x += 1          
        if key_up == True:
            y -= 1         
        if key_down == True:
            y += 1
        if n == 150 or n > 150:
            buttons(100,520,200,50)
            buttons(500,520,200,50)
            screen.blit(fight, pygame.Rect(110,530,200,50))
            screen.blit(heal, pygame.Rect(510,530,200,50))
            screen.blit(enemy_current_health, pygame.Rect(50,50,100,100))
            pygame.draw.rect(screen, BLACK, (300,280,200,210))
            x = 200
            y = 550
            n = 0
            counter += 1    
        n += 1  
        Earth(random_position)
        if n == 1:
            pygame.draw.rect(screen, (BLACK), (290,280,220,220))
            pygame.draw.rect(screen, (BLACK), (300,253,200,25))
            screen.blit(businessmanPic, pygame.Rect(320,128,20,20))
# This is attack phase 4, it draws a garbage can which you have to carefully navigate through
    if (counter%2) != 0 and attack_phase == 4:
        if key_left == True:
            x -= 1         
        if key_right == True:
            x += 1          
        if key_up == True:
            y -= 1         
        if key_down == True:
            y += 1     
        if n == 170 or n > 170:
            buttons(100,520,200,50)
            buttons(500,520,200,50)
            screen.blit(fight, pygame.Rect(110,530,200,50))
            screen.blit(heal, pygame.Rect(510,530,200,50))
            pygame.draw.rect(screen, BLACK, (300,280,200,200))
            x = 200
            y = 550
            n = 0
            counter += 1
        n += 1
        TrashCan()
        if n == 1:
            pygame.draw.rect(screen, (BLACK), (290,280,220,220))           
# Seeing where the border is, and if the heart is there, then it can't go any further
    if x == border_values[0]:
        x += 1
    if x == border_values[2]:
        x -= 1
    if y == border_values[1]:
        y += 1
    if y == border_values[3]:
        y -= 1  
# Drawing the whole game
    drawHeart(x, y, RED)
    border(300, 280, 200, 200)
    pygame.display.flip()
    myClock.tick(60)
# Quitting out of the game
Death = pygame.mixer.Sound("StrandDeath.wav")
Explosion = pygame.mixer.Sound("StrandExplosion.wav")
Megalovania.stop()   
if win == 1:  # This is the win screen. If you beat the boss you will be taken to the win screen, other than the lose screen. And if the game detects that you won with 0 damage taken, you'll get a bonus message at the bottom too.
    pygame.draw.rect(screen, BLACK, (0,0,800,600))
    screen.blit(businessmanPic, pygame.Rect(320,128,20,20))
    pygame.display.flip()
    pygame.time.wait(1000)
    screen.blit(SpeechBubble, pygame.Rect(440,70,30,30))
    Dead = fontBusiness.render("Well it appears i've died", 1, (0, 0, 0))
    screen.blit(Dead, pygame.Rect(450,100,50,50))    
    pygame.display.flip()
    Talking.play()
    for count in range(7):
        pygame.time.wait(100)
        Talking.play()
    pygame.display.flip()
    pygame.time.wait(2000)   
    pygame.draw.rect(screen, BLACK, (440,50,250,152))
    pygame.display.flip()
    Explosion.play()
    pygame.time.wait(4000)
    screen.blit(explosion, pygame.Rect(320,128,20,20))
    pygame.display.flip()
    pygame.time.wait(500)
    for i in range(100,300):
        pygame.draw.rect(screen, RED, (425-i,300-i,10,10))
        pygame.draw.rect(screen, RED, (410+i,300-i,10,10))
        pygame.draw.rect(screen, RED, (425-i,200+i,10,10))
        pygame.draw.rect(screen, RED, (410+i,200+i,10,10))
        pygame.display.flip()
    pygame.time.wait(2000)
    for count in range(1,255):
        pygame.draw.rect(screen, (count ,count ,count), (0,0,800,600))
        pygame.display.flip()
        pygame.time.wait(40)
    pygame.time.wait(2000)
    if your_health >= 100:
        epic_win = fontEpicWin.render("AND WITH NO DAMAGE TAKEN NICELY DONE!", 1, (255, 0, 0))
        screen.blit(epic_win, pygame.Rect(50,400,50,50))
    win = fontWin.render("YOU WON!", 1, (255, 0, 0))
    screen.blit(win, pygame.Rect(150,100,50,50))
    Congratulations.play()
    pygame.display.flip()
    running = True
      
if lose == 1:  # This is the lose screen, if you die, then your heart will explode and you have to try again
    pygame.draw.rect(screen, BLACK, (0,0,800,600))
    drawHeart(x, y, RED)
    pygame.display.flip()
    Death.play()
    pygame.time.wait(1000)
    pygame.draw.rect(screen, BLACK, (0, 0, 800, 600))
    for i in range(1,600):
        pygame.draw.rect(screen, BLACK, ((x+i)-1,(y-i)-1,11,11))
        pygame.draw.rect(screen, RED, (x+i,y-i,6,6))
        pygame.draw.rect(screen, BLACK, ((x-i)+1,(y-i)+1,11,11))
        pygame.draw.rect(screen, RED, (x-i,y-i,6,6))
        pygame.draw.rect(screen, BLACK, ((x+i)-1,(y+i)-1,11,11))
        pygame.draw.rect(screen, RED, (x+i,y+i,6,6))
        pygame.draw.rect(screen, BLACK, ((x-i)+1,(y+i)-1,11,11))
        pygame.draw.rect(screen,RED, (x-i,y+i,6,6))
        pygame.display.flip()
    pygame.time.wait(2000)
    dead_music.play()
    lose = fontLose.render("YOU LOST, TRY AGAIN", 1, (255, 255, 255))
    sub_to_jorxdefier = fontLoseSub.render("Your punishment is you now have to subscribe to the YouTube channel Jorxdefier", 1, (255, 255, 255))    
    screen.blit(lose, pygame.Rect(50,100,50,50))
    screen.blit(sub_to_jorxdefier, pygame.Rect(20,400,50,50))
    pygame.display.flip()    
    running = True
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
heart.close()
pygame.quit()
print("Thank you so much for playing my game!")