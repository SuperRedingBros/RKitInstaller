import os
import json
import pygame
import git
import sys
import pathlib
path = str(pathlib.Path(__file__).parent.resolve())
print(path)
def getModule(module):
    if(not os.path.exists(path+"/Modules/"+module["Name"])):
        repo = git.Repo.clone_from(module["URL"], path+"/Modules/"+module["Name"])
        repo.close()
    else:
        repo = git.Repo(path+"/Modules/"+module["Name"])
        repo.remotes.origin.pull()
        repo.close()
    sys.path.append(path+"\\Modules\\"+module["Name"])
getModule({"URL":"https://github.com/SuperRedingBros/GUIs.git","Name":"Guis"})
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
list = guis.vlistWidget("List",screen)
hlist = guis.hlistWidget("Hlist",list)
guis.emptyWidget("Empty",hlist,style={"W":"pygame.display.get_window_size()[0]/2-32","H":32})
fontpath = str(pathlib.PurePath(guis.path,"assets/Xolonium-Bold.ttf"))
guis.textWidget("Text",hlist,style={"W":128,"H":64,"Text":"RCade","Font":{"File":fontpath,"Scale":40,
"Italics":False,
"Underline":False}})




if True:
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

games = None

def Main():
    global games
    if(os.path.exists(path+"/games.json")):
        file = open(path+"/games.json")
        games = json.loads(file.read())
        for x in games:
            pass#games[x]["Icon"] = pygame.image.load( games[x]["Icon"])
        render(games)
    else:
        print("No games found :(")

def runGame(game):
    #print(games[game])
    for x in games[game]["Requirments"]:
        getModule(x)
    if(not os.path.exists(path+"/Games/"+game)):
        repo = git.Repo.clone_from(games[game]["URL"], path+"/Games/"+game)
        repo.close()
    else:
        repo = git.Repo(path+"/Games/"+game)
        repo.remotes.origin.pull()
        repo.close()
    print(path+"\\Games\\"+game)
    sys.path.append(path+"\\Modules\\")
    sys.path.append(path+"\\Games\\"+game)
    exec(open(path+"/Games/"+game+"/Main.py").read())

def render(games):
    vlist = guis.vlistWidget("List",list)
    for x in games:
        overlay = guis.overlayWidget("Overlay",vlist)
        guis.buttonWidget("Hello",overlay,action="runGame('"+x+"')",style={"W":"pygame.display.get_window_size()[0]","H":32,"Background":None})
        hlist = guis.hlistWidget("Hlist",overlay)
        guis.emptyWidget("Empty",hlist,style={"W":"pygame.display.get_window_size()[0]/2-128","H":32})
        guis.imageWidget("Img",hlist,style={"W":"32","H":"32","Image":path+"/"+games[x]["Icon"]})
        guis.textWidget("Text",hlist,style={"W":"pygame.display.get_window_size()[0]-32","H":32,"Text":x})
    while looping:
        screen.redraw(gameDisplay)
            #print(x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                screen.prossesinputs("Keydown",event,gameDisplay,globals())
            if event.type == pygame.KEYUP:
                screen.prossesinputs("Keyup",event,gameDisplay,globals())
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.prossesinputs("Mousedown",event,gameDisplay,globals())
            if event.type == pygame.MOUSEMOTION:
                screen.prossesinputs("Mousemove",event,gameDisplay,globals())
                mouse = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                screen.prossesinputs("Mouseup",event,gameDisplay,globals())
            if event.type == pygame.FINGERDOWN:
                pass
            if event.type == pygame.FINGERUP:
                pass
            if event.type == pygame.VIDEORESIZE:
                s = pygame.display.get_window_size()
                guis.dw = s[0]
                guis.dh = s[1]
                gameDisplay.fill((0,0,0))
                pygame.display.update()
            if  event.type == pygame.WINDOWLEAVE:
                screen.prossesinputs("Mouseleave",event,gameDisplay,globals())
        screen.update()
        pygame.display.update()

Main()
print("Hello World!!!")
