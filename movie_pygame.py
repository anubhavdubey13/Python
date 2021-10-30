import pygame
from pygame.font import Font
#pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 900, 600 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

COUNTER_FONT = pygame.font.SysFont('comicsans', 40)
GUESS_FONT = pygame.font.SysFont('comicsans', 80)

pygame.display.set_caption('Guess the movie!')

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

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
    WIN.blit(guess_text, (WIDTH//4, HEIGHT//2-60))

    pygame.display.update()

def main():

    guess = ''#'M_V__/N_M_'

    inputbox = InputBox(10,10,140,32)

    counter = 9
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            inputbox.handle_event(event)
        print(inputbox.stored_val())

        inputbox.update()
        
        #WIN.fill((30,30,30))
        draw_window(counter, guess)
        inputbox.draw(WIN)
        pygame.display.flip()
        
        
    main()

main()