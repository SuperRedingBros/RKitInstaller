import os
import json
import pygame
import sys
import pathlib
import installer

path = str(pathlib.Path(__file__).parent.resolve())
print("hello: "+str(installer.getPath()))


# print(os.listdir(path+"/Modules/Guis"))


def getModule(module):
    if not os.path.exists(path + "/Modules/"):
        os.mkdir(path + "/Modules/")
    installer.compatibilityGit(module["URL"], path + "/Modules/" + module["Name"])
    sys.path.append(path + "/Modules/" + module["Name"])


getModule({"URL": "https://github.com/SuperRedingBros/GUIs.git", "Name": "Guis"})
import guis

pygame.init()
usefull = False
looping = True
dw = 1280
dh = 640
ldw = 1280
ldh = 640
variabletest = 0
print("#4")
clock = pygame.time.Clock()
screen = guis.mainWidget("blue", inglobals=globals(), style={}, data={})
list = guis.vlistWidget("List", screen)
hlist = guis.hlistWidget("Hlist", list)
guis.emptyWidget("Empty", hlist, style={"W": "pygame.display.get_window_size()[0]/2-32", "H": 32})
fontpath = str(pathlib.PurePath(guis.path, "assets/Xolonium-Bold.ttf"))
guis.textWidget("Text", hlist, style={"W": 128, "H": 64, "Text": "RCade", "Font": {"File": fontpath, "Scale": 40,
                                                                                   "Italics": False,
                                                                                   "Underline": False}})
print("#4.25")
if True:
    if usefull:
        gameDisplay = pygame.display.set_mode((dw, dh), pygame.FULLSCREEN, pygame.RESIZABLE)
        s = pygame.display.get_window_size()
        dw = s[0]
        dh = s[1]
    else:
        print("#4.24")
        gameDisplay = pygame.display.set_mode((dw, dh), pygame.RESIZABLE)
        print("#4.26")
    s = pygame.display.get_window_size()
    print("#4.29")
    dw = s[0]
    dh = s[1]
    # pygame.display.set_icon(pygame.image.load( "./assets/p.png"))
    pygame.display.set_caption('RCade')
print("#4.5")

games = {}


def Main():
    global games
    if os.path.exists(path + "/games.json"):
        file = open(path + "/games.json")
        games = json.loads(file.read())
        render()
    else:
        print("No games found :(")


def runGame(game):
    # print(games[game])
    for x in games[game]["Requirments"]:
        getModule(x)
    if not os.path.exists(path + "/Games/"):
        os.makedirs(path + "/Games/")
    installer.compatibilityGit(games[game]["URL"], path + "/Games/" + game)
    print(path + "/Games/" + game)
    sys.path.append(path + "/Modules/")
    sys.path.append(path + "/Games/" + game)
    exec(open(path + "/Games/" + game + "/Main.py").read())

ready = False
print("#5")


def render():
    global ready
    vlist = guis.vlistWidget("List", list)
    for x in games:
        overlay = guis.overlayWidget("Overlay", vlist)
        guis.buttonWidget("Hello", overlay, action="runGame('" + x + "')",
                          style={"W": "pygame.display.get_window_size()[0]", "H": 32, "Background": None})
        gamehlist = guis.hlistWidget("Hlist", overlay)
        guis.emptyWidget("Empty", gamehlist, style={"W": "pygame.display.get_window_size()[0]/2-128", "H": 32})
        guis.imageWidget("Img", gamehlist, style={"W": "32", "H": "32", "Image": path + "/" + games[x]["Icon"]})
        guis.textWidget("Text", gamehlist, style={"W": "pygame.display.get_window_size()[0]-32", "H": 32, "Text": x})
    while looping:
        if ready:
            screen.redraw(gameDisplay)
        # print(x)
        pygame.event.pump()
        for event in pygame.event.get():
            if hasattr(pygame,"APP_WILLENTERFOREGROUND") and event.type == pygame.APP_WILLENTERFOREGROUND:
                ready = True
            if event.type == pygame.WINDOWSHOWN:
                ready = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                screen.prossesinputs("Keydown", event, gameDisplay, globals())
            if event.type == pygame.KEYUP:
                screen.prossesinputs("Keyup", event, gameDisplay, globals())
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.prossesinputs("Mousedown", event, gameDisplay, globals())
            if event.type == pygame.MOUSEMOTION:
                screen.prossesinputs("Mousemove", event, gameDisplay, globals())
            if event.type == pygame.MOUSEBUTTONUP:
                screen.prossesinputs("Mouseup", event, gameDisplay, globals())
            if event.type == pygame.FINGERDOWN:
                pass
            if event.type == pygame.FINGERUP:
                pass
            if event.type == pygame.VIDEORESIZE:
                ls = pygame.display.get_window_size()
                guis.dw = ls[0]
                guis.dh = ls[1]
                gameDisplay.fill((0, 0, 0))
                pygame.display.update()
            if event.type == pygame.WINDOWLEAVE:
                screen.prossesinputs("Mouseleave", event, gameDisplay, globals())
        #screen.update()
        pygame.display.update()


Main()
print("Hello World!!!")
