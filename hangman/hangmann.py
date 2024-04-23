import math
import random
import pygame
from playsound import playsound
from pygame import mixer


pygame.init()        
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")


#button variables
SIZE = 25
GAP = 5
letters = []
startx = 45
starty = 180
A = 65
for i in range(26):
    x = startx + ((SIZE * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + SIZE * 2))
    letters.append([x, y, chr(A + i), True])
      
  
#font TYPE
LETTER_FONT = pygame.font.SysFont('cambriacambriamath', 40)
WORD_FONT = pygame.font.SysFont('cambriacambriamath', 60)
TITLE_FONT = pygame.font.SysFont('inkfree', 70)
END_FONT = pygame.font.SysFont('inkfree', 50)
  

#loading images
images = []
for i in range(7):
    image = pygame.image.load(str(i) + ".png")
    images.append(image)
    
    
    
     
#game variables  
hangman_status = 0
words = ["POKHARA","KATHMANDU","DEERWALK","APPLE","CRICKET","RABBIT","FINLAND","CAMERA","APARTMENT","COFFEE","DIABETES","PETROL","CARROT","HOSPITAL","GOLD","NURSE"]
word = random.choice(words)
guessed = []
hint=["CITY","CITY","COLLEGE","FRUIT","GAME","ANIMAL","COUNTRY","GADGET","BUILDING","DRINK","DISEASE","FUEL","VEGETABLE","BUILDING","JWELERY","JOB"]


 

#colors
SKY = (135, 206, 235)
BLACK = (0,0,0)
RED = (255,24,24)
GREEN = (124,252,0)

#background
BG = pygame.transform.scale(pygame.image.load("C:/Users/binit/OneDrive/Desktop/hangman/bkkk.png"), (WIDTH, HEIGHT))
bgmain = pygame.transform.scale(pygame.image.load('mainmenu.png'), (WIDTH,HEIGHT))


#background sound
mixer.music.load('background.mp3')
mixer.music.play(-1)


FPS = 60    
clock = pygame.time.Clock()      
run = True    

        
def draw():
  
     
    screen.blit(BG, (0,0))

    # draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    screen.blit(text, (140,25))

    text = LETTER_FONT.render("GUESS THE WORD", 1, BLACK)
    screen.blit(text, (265,125))
    
    #draw lines
    text = LETTER_FONT.render("_____________________________________", 1, BLACK)
    screen.blit(text, (140,78))
    text = LETTER_FONT.render("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 1, BLACK)
    screen.blit(text, (0,260))
    text = LETTER_FONT.render("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 1, BLACK)
    screen.blit(text, (0,145))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, RED)
    screen.blit(text, (100, 420))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            text = LETTER_FONT.render(ltr, 1, BLACK)
            screen.blit(text, (x,y))
            
    #hint
    for i in range(16):
         if word in words[i]:
          text=LETTER_FONT.render('Hint:',1,RED)
          screen.blit(text,(320,300))
          text=LETTER_FONT.render(hint[i],1,RED)
          screen.blit(text,(390,300))        

    screen.blit(images[hangman_status], (500, 270))
    pygame.display.update()
     
def menu():

    screen.blit(bgmain, (0,0))
      
    texta=WORD_FONT.render("PLAY",1,RED)
    screen.blit(texta,(450,400))
  
   
  
    pygame.display.update()
    pygame.time.delay(3000)
    
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posi_x, posi_y = pygame.mouse.get_pos()
                distance = math.sqrt((500 - posi_x) ** 2 + (450 - posi_y) ** 2)
                
                
                if distance < 50:
                   return 'Play Game'
                
           
gotoplay = menu()
          
                                                 
def display_message(message):
    ln = 400
    br = 430
    hg = 500
    pygame.time.delay(1000)
    screen.blit(BG, (0,0))

   
    text = TITLE_FONT.render(message,1,BLACK)
    screen.blit(text,(WIDTH/2 - text.get_width()/2,100))
      
    if hangman_status==6:
       text = WORD_FONT.render("IT WAS",1,BLACK)
       screen.blit(text,(230,200))  
       text = WORD_FONT.render(word,1,RED)
       screen.blit(text,(385,200))
      
      
    text = LETTER_FONT.render("PLAY AGAIN:",1,BLACK)
    screen.blit(text,(170,417))

    # yes
    text1 = LETTER_FONT.render("YES", 1, GREEN)
    screen.blit(text1, (ln - text1.get_width() / 2, br - text1.get_height() / 2))

    # no
    text = LETTER_FONT.render("NO", 1, RED)
    screen.blit(text, (hg - text.get_width() / 2, br - text.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(3000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                distance = math.sqrt((ln - pos_x) ** 2 + (br - pos_y) ** 2)
                if distance < SIZE:
                    return True 
                distance = math.sqrt((hg - pos_x) ** 2 + (br - pos_y) ** 2)
                if distance < SIZE:
                    return False  

def reset_game():
    global hangman_status, guessed, word
    hangman_status = 0
    guessed = []
    word = random.choice(words)
    for letter in letters:           
        letter[3] = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x , m_y = pygame.mouse.get_pos()    
            for letter in letters:
              x,y,ltr,visible = letter
              if visible:
               dis = math.sqrt((x- m_x)**2 + (y- m_y)**2)
               if dis<SIZE:
                  letter[3]=False
                  playsound("click.wav")
                  guessed.append(ltr)
                  if ltr not in word:
                      hangman_status += 1
                 
                     
 
    draw()
  
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
                
    if won:
        playsound("win.mp3")
        play_again = display_message("CONGRATULATIONS")
        if play_again:
            reset_game()
        else:
            break

    if hangman_status == 6:
        playsound('lose.wav')
        play_again = display_message("YOU LOST")
        if play_again:
            reset_game()
        else:
            break
               

pygame.quit()  

