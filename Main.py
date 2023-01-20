import os
import json
import pygame
import guis

pygame.init()
usefull = False
looping=True
dw = 1280
dh = 640
ldw = 1280
ldh = 640
variabletest = 0
looping=True
clock = pygame.time.Clock()
screen = guis.mainWidget("blue",inglobals=globals(),style={},data={})

if __name__ == '__main__':
    if usefull:
        gameDisplay = pygame.display.set_mode((ldw, ldh), pygame.FULLSCREEN,pygame.RESIZABLE )
        s = pygame.display.get_window_size()
        dw = s[0]
        dh = s[1]
    else:
        gameDisplay = pygame.display.set_mode((ldw, ldh),pygame.RESIZABLE)
    s = pygame.display.get_window_size()
    dw = s[0]
    dh = s[1]
    #pygame.display.set_icon(pygame.image.load( "./assets/p.png"))
    pygame.display.set_caption('RCade')

def Main():
    if(os.path.exists("games.json")):
        file = open("games.json")
        games = json.loads(file.read())
        for x in games:
            pass#games[x]["Icon"] = pygame.image.load( games[x]["Icon"])
        render(games)
    else:
        print("No games found :(")

def render(games):
    vlist = guis.vlistWidget("List",screen)
    for x in games:
        hlist = guis.hlistWidget("Hlist",vlist)
        guis.imageWidget("Img",hlist,style={"W":"32","H":"32","Image":games[x]["Icon"]})
        guis.textWidget("Text",hlist,style={"W":"pygame.display.get_window_size()[0]-32","H":32,"Text":x})
    while looping:
        screen.redraw(gameDisplay)
            #print(x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.update()
        pygame.display.update()

Main()
print("Hello World!!!")
