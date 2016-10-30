import pygame, random

pygame.init()

pygame.mixer.init()
# loading music
pygame.mixer.music.load("batman_theme.mp3")
try:
    batmanAttackSound = pygame.mixer.Sound("batman.wav")
    JokerattackSound = pygame.mixer.Sound("bullet.mp3")
    batmanLost = pygame.mixer.Sound("pushups.mp3")
    jokerHealthSound = pygame.mixer.Sound("serious.mp3") # joker health is 500
    jokerHealthSound2 = pygame.mixer.Sound("smile.mp3") # joker health 100
    batmanWon = pygame.mixer.Sound("batman.mp3")
except:
    print ("File not Found")
    pass
#define window and objects size 
dispalyWidth  = 1024
dispalyHeight  = 600
carSize = 128
jokerSize = 250
batLogoSizeL = 380
batLogoSizeW = 200
FPS = 60

#colors
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
purple = (138,43,226)

#set window
gameDisplay = pygame.display.set_mode((dispalyWidth,dispalyHeight))
pygame.display.set_caption("Batman vs. Joker")
clock =  pygame.time.Clock()

# load images from current directory
try:
    batMobile = pygame.image.load('batman.png')
    joker1 = pygame.image.load('joker.png')
    batLogo1 = pygame.image.load('batmanlogo.png')
    funnyBat = pygame.image.load('funnyBat.png')
    batarang1 = pygame.image.load('batarang.png')
except:
    print ("File not Found")
    pass

# setting objects 

def batCar(x,y):
    gameDisplay.blit(batMobile,(x,y))

def joker(x,y):
    gameDisplay.blit(joker1,(x,y))

def batLogo(x,y):
    gameDisplay.blit(batLogo1,(x,y))

def funnyBatman(x,y):
    gameDisplay.blit(funnyBat,(x,y))

def batarang(x,y):
    gameDisplay.blit(batarang1,(x,y))

# crash detection    
    
def detectCrash(x1,y1,w1,h1,x2,y2,w2,h2):
    if(x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True

    elif(x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
         return True

    elif(x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
         return True

    elif(x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
         return True
    else:
        return False

# displaying text    
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#creating button

def button(msg,x,y,w,h,ic,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Courier",15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#quit game function
    
def quitGame():
    pygame.quit()
    quit()

def gameWin(winner,number):
    winner = pygame.font.SysFont("Courier", 115)

    if number ==1:

        the_text = winner.render("You Won!!!", True, yellow)
        #pygame.mixer.music.stop
        #JokerattackSound.play()
    elif number == 2:
        the_text = winner.render("You Lost!!!", True, purple)
        #pygame.mixer.Sound.play(batmanLost)
    gameDisplay.blit(the_text, (270, 250))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitGame()

        gameDisplay.fill(black)
        batLogo(((dispalyWidth * .30)),((dispalyHeight * .30)))
        gameDisplay.blit(the_text, (220, 50))
        button("Play Again",300,450,100,50,yellow,gameLoop)
        button("Quit",640,450,100,50,purple,quitGame)

        pygame.display.update()
        clock.tick(15)


def gameIntro():

    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitGame()

        gameDisplay.fill(black)
        my_font = pygame.font.SysFont("Courier",72)

        the_text = my_font.render("Batman vs.",True, yellow)
        the_text1 = my_font.render("Joker",True, purple)
        gameDisplay.blit(the_text, (200, 50))
        gameDisplay.blit(the_text1, (673, 50))
        batLogo(((dispalyWidth * .30)),((dispalyHeight * .30)))

        button("Start",300,450,100,50,yellow,gameLoop)
        button("Quit",640,450,100,50,purple,quitGame)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    pygame.mixer.music.stop()
    my_font = pygame.font.SysFont("Courier", 16)
    winner = pygame.font.SysFont("Courier", 72)

    x = (dispalyWidth * .45)
    y = (dispalyHeight * .01)
    x2 = (dispalyWidth * .21)
    y2 = (dispalyHeight * .32)
    x3 = (dispalyWidth * .30)
    y3 = (dispalyHeight * .30)
    time = 100
    xchange = 0
    ychange = 0
    x2change = 0
    y2change = 0

    vector = (random.random() * 5, random.random() *5)
    jokerPosition = (x2, y2)
    jokerHealth = 1000
    batmanHealth = 1000
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                quitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   xchange = -5
                elif event.key == pygame.K_RIGHT:
                    xchange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     xchange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                   ychange = -5
                elif event.key == pygame.K_DOWN:
                    ychange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                     ychange = 0
        x += xchange
        y += ychange

        jokerPosition = (jokerPosition[0] + vector[0],
                        jokerPosition[1] + vector[1])

        gameDisplay.fill(black)
        batLogo(x3,y3)

        batCar(x,y)
        joker(jokerPosition[0],jokerPosition[1])

        the_text = my_font.render("Joker's Health = {0}"
                  .format(jokerHealth), True, white)

        gameDisplay.blit(the_text, (10, 10))

        the_text2 = my_font.render("Batman's Health = {0}"
                  .format(batmanHealth), True, white)

        gameDisplay.blit(the_text2, (780, 10))

        jokerDying = detectCrash(x,y,carSize,carSize,jokerPosition[0],jokerPosition[1],jokerSize,jokerSize)

        batmanHealthIncrease = detectCrash(x,y,carSize,carSize,x3,y3,batLogoSizeL,batLogoSizeW)

        if (x > dispalyWidth - carSize or x < 0) or (y > dispalyHeight - carSize or y < 0) :
            x = random.random() *(dispalyWidth)
            y = random.random() *(dispalyHeight)

        if (jokerPosition[0] > dispalyWidth - jokerSize or jokerPosition[0] < 0):
            vector = (-vector[0], vector[1])

        if (jokerPosition[1] > dispalyHeight - jokerSize or jokerPosition[1] < 0) :
            vector = (vector[0], -vector[1])

        if jokerDying == True and batmanHealthIncrease == False:
            jokerHealth -=1
            time +=1
            batarang(jokerPosition[0], jokerPosition[1])

            #batmanAttackSound.play(1)
            if time >=0:
                time = 100
            if jokerHealth == 500 :
                print(x)
                #jokerHealthSound.play()
            if jokerHealth <= 1000:
                pygame.mixer.Sound.play(batmanAttackSound)
                #jokerHealthSound2.play()

        if jokerDying == False and batmanHealthIncrease == False:
            batmanHealth -=1
            funnyBatman(x,y)

            #JokerattackSound.play()
            if batmanHealth == 500 :
               print ("hi")

        if batmanHealthIncrease == True:
            if not (time <=0):
                batmanHealth +=2
                time -=1
                if batmanHealth >= 1000:
                    batmanHealth = 1000
            if time <=0:
                batmanHealth -=2


        if jokerHealth <= 0:
            gameWin(winner,1)

        if (batmanHealth <= 0 ):
            gameWin(winner,2)

        pygame.display.update()
        clock.tick(FPS)

gameIntro()
gameLoop()
