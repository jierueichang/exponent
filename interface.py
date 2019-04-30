'''EXPONENT UI'''
import pygame, sys, mathematics
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((320,480))
pygame.display.set_caption('Exponent')

fpsClock = pygame.time.Clock()

query = ''

expfont = pygame.font.Font(None,25)

class button():
    def __init__(self, text, command, xpos, ypos):
        self.text = text
        self.command = command
        self.rect = rect
    def render():
        pass

def graph(equation, xvalues, w=320, h=300):
    print 'graphing'
    yvalues = []
    for i in xvalues:
        try:
            x = i
            yvalues.append(eval(equation))
        except:    pass
    pygame.draw.rect(screen,(255,255,255),(0,0,w,h))
    for i in range(len(xvalues)):
        pygame.draw.rect(surface,(0,0,0),(i*(len(xvalues)/w,h-yvalues[i],3,3)))

rows = []
upshift = 0
while True:
    screen.fill((0, 0, 0))
    x, y = pygame.mouse.get_pos()
    for i in range(len(rows)):
        rowtext = expfont.render(rows[i],1,(255,255,255))
        #screen.blit(rowtext,(20,400-20*i))
        screen.blit(rowtext,(20,400-120-upshift+20*i))
    pygame.draw.rect(screen,(220,220,255),(0,300,320,30))
    pygame.draw.rect(screen,(20,20,20),(0,330,320,30))
    pygame.draw.rect(screen,(200,200,255),(0,360,320,120))
    screen.blit(expfont.render(query,1,(0,0,0)),(20,310))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == 13:
                print query
                try:
                    eval(query)
                except:
                    result = mathematics.compute(query)
                print result
                rows.append(query)
                rows.append('   --> '+str(result))
                rows.append('~~~~~~~~~~~~~~~~~~~~~~~')
                query = ''
                upshift+=60
            elif event.key == 303 or event.key == 304:
                pass
            elif event.key == 8:
                query = query[:-1]
            elif event.key == K_UP:
                upshift -= 20
            elif event.key == K_DOWN:
                upshift += 20
            else:
                #print event.key
                #print event.unicode
                query += event.unicode
    pygame.display.update()
    fpsClock.tick(10)
