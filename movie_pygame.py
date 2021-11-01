import pygame
from pygame.font import Font
#pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 900, 600 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

COUNTER_FONT = pygame.font.SysFont('comicsans', 40)
GUESS_FONT = pygame.font.SysFont('comicsans', 60)

pygame.display.set_caption('Guess the movie!')

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

vowels = ['a','e','i','o','u']

# for input box
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

# Input text box using class
class InputBox:

    def __init__(self,x,y,w,h,text=''):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.store_value = ''
        
    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = COLOR_ACTIVE
            else:
                self.active = False
                self.color = COLOR_INACTIVE
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    self.store_value = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                
                self.txt_surface = FONT.render(self.text, True, self.color)

    def stored_val(self):
        return self.store_value

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, WIN):
        WIN.blit(self.txt_surface,(self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(WIN, self.color, self.rect, 2)


def draw_text(text):
    txt = FONT.render(text,1,WHITE)
    WIN.blit(txt, (WIDTH/2,HEIGHT/2))
    pygame.display.update()

def draw_window(counter, guess):
    WIN.fill(BLACK)
    
    counter_text = COUNTER_FONT.render('Guesses Left:' + str(counter), -1, WHITE)
    WIN.blit(counter_text, (WIDTH-counter_text.get_width() - 10, 10))

    guess_text = GUESS_FONT.render(guess,-1, WHITE)
    WIN.blit(guess_text, (100, HEIGHT//2-60))

    pygame.display.update()

def movie_format(movie):
    
    movie = movie.lower()

    guess = []
    for m in movie:
        if m in vowels:
            guess.append(m)
        elif m == ' ':
            guess.append('/')
        else:
            guess.append('_')

    guess =  ''.join(guess)   
    return guess, movie

def the_game(movie, guess, user_input):
    counter = 9
    list_guessed_letters = vowels.copy()
    while (counter > 0) and (' _ ' in guess):
        letter = user_input.lower()
        
        if letter in list_guessed_letters:
            #print('Letter already guessed or it is vowel. Try again')
            pass
        else: 
            if letter in movie:
                for i in range(0, len(movie),1):
                    if movie[i] == letter:
                        guess[i] = letter
            else:
                counter -= 1
                if counter == 0:
                    print('Game Over. You lost. The movie is', movie)
        
        if ' _ ' not in guess:
            print('You guessed right! The movie is', movie)
        else:
            print(''.join(guess))
            print('Guesses left:', counter)
        
        list_guessed_letters.append(letter)

def the_game2(movie, guess, letter):
    the_list = []
    [the_list.append(guess[i]) for i in range(len(guess))] 
    
    if letter in movie:
        for i in range(len(movie)):
            if movie[i] == letter:
                the_list[i] = letter
    updated_guess = ''.join(the_list)
    return updated_guess

the_game2('kal ho', '_a_/_o','k')

# def main():

#     guess = ''#'M_V__/N_M_'

#     inputbox = InputBox(10,10,140,32)
#     inputbox_G = InputBox(10,500,140,32)

#     counter = 9
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
            
#             inputbox.handle_event(event)
#             inputbox_G.handle_event(event)      

#         guess, movie = movie_format(inputbox.stored_val()) 
#             #guess += inputbox_G.stored_val()
#         # while '_' in guess:
#         #     guess = the_game2(movie, guess, inputbox_G.stored_val())

#         inputbox.update()
#         inputbox_G.update()
#         #print(inputbox.stored_val())
#         #WIN.fill((30,30,30))

#         draw_window(counter, guess)
#         inputbox.draw(WIN)
#         inputbox_G.draw(WIN)
#         pygame.display.flip()        
        
#     main()

# main()


# where I am getting stuck:
# 1. not able to substitute dashes. Seems like there is an extra character
# Will be building this from scratch
# and go slow

def main():

    guess = ''

    inputbox = InputBox(10,10,140,32)
    inputbox_G = InputBox(10,500,140,32)

    counter = 9
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  
            
            inputbox_G.handle_event(event)
            inputbox.handle_event(event)

        if guess == '':
            guess,movie = movie_format(inputbox.stored_val())
        else:
            guess = the_game2(movie, guess, inputbox_G.stored_val()) # simple does it. Phew!!!!

        inputbox.update()
        inputbox_G.update()
            
        draw_window(counter, guess)
        inputbox.draw(WIN)
        inputbox_G.draw(WIN)
        pygame.display.flip()        
        
    main()

main()

# the part about printing guess on the screen is working. It was working previously as well
# the part to be solved is replacing at exact position - even this is working
# The bottleneck is preventing update of 'guess' because as it restarts the process again instead of saving the string - sorted
# next step: a functional counter