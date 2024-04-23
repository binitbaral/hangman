# python version 3.10 works with pygame version 2.5.0
from ast import Break, For
from tokenize import Triple
from turtle import distance, goto, width
import pygame
import math
import random

pygame.init()         #initialize pygame module
WIDTH, HEIGHT = 900,600
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ("Hangman Game")
# background_image = pygame.image.load("background.png").convert()




#button variables
RADIUS = 20
GAP = 15
letters =[]  # a list
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty = 500
A = 65
#determining x and y position for each button
for i in range(26):
  x= startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y= starty + ((i // 13)*(GAP + RADIUS *2))
  letters.append([x,y,chr (A + i),True])  
  
#font TYPE
FONT_TYPE=pygame.font.SysFont('Times New Roman',30)
WORD_FONT =pygame.font.SysFont('Times New Roman',60)
TITLE_FONT = pygame.font.SysFont('Times New Roman',70)
INTRO_FONT = pygame.font.SysFont('Times New Roman',35)
  

#loading images
images = []     # a list
for i in range(7):
    image=pygame.image.load(str(i)+".png")
    images.append(image)
    
    
    
     
#game variables  
hangman_status =0
words=['HELLO','DEERWALK','PYTHON','VSCODE','PYGAME','COMPUTER','SCIENCE','TELEVISION','TEACHER','YEAR','BASKETBALL','EGYPT','ANNAPURNA','NIKE','MICROSOFT']
word = random.choice(words)
guessed = []     # represent the letters we've guessed
hint=['greeting','institute','language','coding platform','code library','device','subject','media','job','time frame','sport','african country','mountain','shoe','tech company']

words_hard=['CHLORINE','NEANDER','COCKPIT','PEEKABOO','FLABBERGAST','XYLOPHONE','WALTZ']
hint_hard=['chemical','species','vehicle area','child game','synonym for shocked','musical instrument','dance']
word_hard=random.choice(words_hard)
guessed_hard=[]

 

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (58,69,84)
GREEN =(124,252,0)
RED = (255, 0, 0)
BEIGE = (245,245,220)
MAROON =(173, 69, 47)



FPS = 60    # defines pace/speed of the game
clock = pygame.time.Clock()      # clock object counts at 60fps. It is a function in pygame.time module.


run = True

def draw():
  
     
     win.fill(WHITE)     # changing bg color
     
     
     text=INTRO_FONT.render("___________________________________________________________",1,BLACK)
     win.blit(text,(WIDTH/2 - text.get_width()/2, 400))
     
     
     #drawing title
     text = INTRO_FONT.render("LETS PLAY!",1,GREY)
     win.blit(text,(WIDTH/2 - text.get_width()/2, 20))
     
     # draw word
     display_word = ''
     for letter in word:
         if letter in guessed:
             display_word += letter + ' '
         else:
             display_word += '_ '
     text = WORD_FONT.render(display_word,1,BLACK)
     win.blit(text,(400,170))
    
     
                 
     
     #draw buttons
     for letter in letters:
         x,y,ltr,visible = letter
         if visible:
          pygame.draw.circle(win, BLACK,(x,y), RADIUS, 3)
          text= FONT_TYPE.render(ltr,1,GREY)    # render(what we want to render, anti aliasing , color of the font)
          win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))  # win.blit is the actual drawing
          
          
         
     #hint
     for i in range(15):
         if word in words[i]:
          text=FONT_TYPE.render('Hint:',1,BLACK)
          win.blit(text,(400,300))
          text=FONT_TYPE.render(hint[i],1,BLACK)
          win.blit(text,(480,300))
         
     
     # adding images   
     win.blit(images[hangman_status],(70,120))      
     pygame.display.update()
  
def draw_hard():
  
     
     win.fill(WHITE)     # changing bg color
     
     
     text=INTRO_FONT.render("___________________________________________________________",1,BLACK)
     win.blit(text,(WIDTH/2 - text.get_width()/2, 400))
     
     
     #drawing title
     text = INTRO_FONT.render("LETS PLAY!",1,GREY)
     win.blit(text,(WIDTH/2 - text.get_width()/2, 20))
     
     # draw word
     display_word = ''
     for letter in word_hard:
         if letter in guessed_hard:
             display_word += letter + ' '
         else:
             display_word += '_ '
     text = WORD_FONT.render(display_word,1,BLACK)
     win.blit(text,(400,170))
    
     
                 
     
     #draw buttons
     for letter in letters:
         x,y,ltr,visible = letter
         if visible:
          pygame.draw.circle(win, BLACK,(x,y), RADIUS, 3)
          text= FONT_TYPE.render(ltr,1,GREY)    # render(what we want to render, anti aliasing , color of the font)
          win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))  # win.blit is the actual drawing
          
          
         
     #hint
     for i in range(7):
         if word_hard in words_hard[i]:
          text=FONT_TYPE.render('Hint:',1,BLACK)
          win.blit(text,(400,300))
          text=FONT_TYPE.render(hint_hard[i],1,BLACK)
          win.blit(text,(480,300))
         
     
     # adding images   
     win.blit(images[hangman_status],(70,120))      
     pygame.display.update()   

#menu
def menu():

    win.fill(WHITE)
    text=FONT_TYPE.render("Choose level:",1,BLACK)
    win.blit(text,(200,100))
    
    pygame.draw.circle(win, BEIGE,(330,220), 50, 50)   
    texta=FONT_TYPE.render("Easy",1,BLACK)
    win.blit(texta,(300,200))
  
    pygame.draw.circle(win, MAROON,(330,420), 50, 50)
    textb=FONT_TYPE.render("Hard",1,BLACK)
    win.blit(textb,(300,400))
  
    pygame.display.update()
    pygame.time.delay(3000)
    
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posi_x, posi_y = pygame.mouse.get_pos()
                distance = math.sqrt((300 - posi_x) ** 2 + (200 - posi_y) ** 2)
                distance2 = math.sqrt((300 - posi_x) ** 2 + (400 - posi_y) ** 2)
                
                if distance < 50:
                   return 'easy'
                elif distance2<50:
                    return 'hard'
           
selected_level = menu()
mode = 'easy' if selected_level == 'easy' else 'hard'          
              
           
              
# printing end of game result
def display_message(message, word_to_display=None):
    a = 400
    b = 430
    c = 500
    pygame.time.delay(1000)
    win.fill(WHITE)

   
    text = TITLE_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,100))

    if hangman_status == 6:
        text = FONT_TYPE.render("The word was:", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 200))

        if mode == 'easy':
            text = FONT_TYPE.render(word, 1, BLACK)
            win.blit(text, ((WIDTH/2 - text.get_width()/2) + 5, 250))
        elif mode == 'hard' and word_to_display is not None:
            text = FONT_TYPE.render(word_to_display, 1, BLACK)
            win.blit(text, ((WIDTH/2 - text.get_width()/2) + 5, 250))
      
      
    text = FONT_TYPE.render("Do you want to play again?",1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,360))

    # yes
    pygame.draw.circle(win, GREEN, (a, b), RADIUS, 18)
    text1 = FONT_TYPE.render("Y", 1, BLACK)
    win.blit(text1, (a - text1.get_width() / 2, b - text1.get_height() / 2))

    # no
    pygame.draw.circle(win, RED, (c, b), RADIUS,18)
    text = FONT_TYPE.render("N", 1, BLACK)
    win.blit(text, (c - text.get_width() / 2, b - text.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(3000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                distance = math.sqrt((a - pos_x) ** 2 + (b - pos_y) ** 2)
                if distance < RADIUS:
                    return True  # User wants to play again
                distance = math.sqrt((c - pos_x) ** 2 + (b - pos_y) ** 2)
                if distance < RADIUS:
                    return False  # User does not want to play again

def reset_game():
    global hangman_status, guessed, word, guessed_hard,word_hard
    hangman_status = 0
    guessed = []
    word = random.choice(words)
    for letter in letters:           # resets the clicked buttons
        letter[3] = True
    guessed_hard=[]
    word_hard=random.choice(words_hard)
    for letter1 in letters:           # resets the clicked buttons
        letter1[3] = True

def handle_input(letter, guessed_list, word_to_guess):
    if letter not in guessed_list:
        guessed_list.append(letter)
        if mode == 'easy' and letter not in word_to_guess:
            return True  # Incorrect guess
        elif mode == 'hard' and letter not in word_hard:
            return True  # Incorrect guess
    return False  # Correct guess or already guessed

def handle_mode():
    if mode == 'easy':
        draw()
    elif mode == 'hard':
        draw_hard()
        
while run:
    clock.tick(FPS)
  
    
    
    
    for event in pygame.event.get():    # any event that has happened will be stored in this method. event meaning click of the mouse, typing of a letter. dealing with any user input
        if event.type == pygame.QUIT:
            run = False

 
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        if handle_input(ltr, guessed, word) and mode == 'easy':
                            hangman_status += 1
                        elif handle_input(ltr, guessed_hard, word_hard) and mode == 'hard':
                            hangman_status += 1
                        letter[3] = False 
                    
                      
       
    handle_mode()

    won = all(letter in guessed for letter in word) if mode == 'easy' else all(letter in guessed_hard for letter in word_hard)
    lost = hangman_status == 6
    
    if won or lost:
        message = "YOU WON!!!" if won else "YOU LOST :("
        word_to_display = word if mode == 'easy' else word_hard
        
        play_again = display_message(message, word_to_display=word_to_display)
        
        if play_again:
            reset_game()
            mode = 'easy' if selected_level == 'easy' else 'hard'
        else:
            break

pygame.quit()