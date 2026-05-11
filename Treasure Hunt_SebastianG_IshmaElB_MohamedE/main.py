from gamelib import *

#Game functions (Modular Programming)
def scuba_update():
    scuba.draw()

    #Postitioning Scuba's health bar
    scubahealthbar.moveTo( scuba.x - 30, scuba.y + 35)
    scubahealthbar.width = scuba.health/2
    
    if keys.Pressed[K_LEFT]:
        scuba.x -= 3
    if keys.Pressed[K_RIGHT]:
        scuba.x += 3
    if keys.Pressed[K_UP]:
        scuba.y -= 3
    if keys.Pressed[K_DOWN]:
        scuba.y += 3
        
def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,7000)
        y = randint(100, 500)
        objects[i].moveTo(x,y)
        s = randint(4,8)
        objects[i].setSpeed(s, 90)
        objects[i].visible = True

def power_update():
    for i in range(len(healthpods)):
        healthpods[i].move()
        if scuba.collidedWith( healthpods[i] ):
            scuba.health += 5
            healthpods[i].visible = False

    for i in range(len(tridents)):
        tridents[i].move()
        if scuba.collidedWith( tridents[i]):
            scuba.ammo += 1
            tridents[i].visible = False
            
#Main Program
game = Game(800,600, "Treasure Hunt")
bk = Image("images/ocean.WEBP", game)
bk.resizeTo(800,600)

#Scuba diver animation
scuba = Animation("images/scuba.png", 9, game, 1700/8, 425/2, 6)
scuba.resizeBy(-45)

#Inital amount of tridents that the scuba has
scuba.ammo = 0

#create helth bar for scuba
scubahealthbar = Shape("bar", game, scuba.health, 10, green)

#Swordfishs
swordfishs = []

for i in range(40):
    sf = Animation("images/swordfish.png", 5, game, 1100/5, 152, 3)
    sf.resizeBy(-65)
    swordfishs.append(sf)
positionObjects(swordfishs)

#Sharks
sharks = []

for i in range(20):
    s = Animation("images/shark.png", 10, game, 2100/ 5, 326/2)
    s.resizeBy(-55)
    sharks.append(s)
positionObjects(sharks)

#Orcas
orcas = []

for i in range(20):
    o = Animation("images/orca.png", 9, game, 1700/5, 464/2)
    o.resizeBy(-55)
    orcas.append(o)
positionObjects(orcas)

#Megaladon animation
megaladon = Animation("images/megaladon.png", 12, game, 9600/5, 5760/3)
megaladon.resizeBy(-77)
megaladon.moveTo(900,300)
megaladon.setSpeed(1,90)

#Megaladon2
megaladon2 = Animation("images/megaladon.png", 12, game, 9600/5, 5760/3)
megaladon2.resizeBy(-96)
megaladon2.moveTo(50, game.height - 50)

#Healthpods
healthpods = []

for i in range(5):
    h = Animation("images/firstaid.png", 40, game, 257, 250)
    h.resizeBy(-85)
    healthpods.append(h)
positionObjects(healthpods)

#Goldbar images
goldbars = []
for i in range(35):
    g = Image("images/goldbar.png", game)
    g.resizeBy(-93)
    goldbars.append(g)
positionObjects(goldbars)

#Goldbar2 image
goldbar2 = Image("images/goldbar.png", game)
goldbar2.resizeBy(-92)
goldbar2.moveTo(50, game.height - 50)

#Diamond images
diamonds = []
for i in range(17):
    d = Image("images/diamond.png", game)
    d.resizeBy(-90)
    diamonds.append(d)
positionObjects(diamonds)

#Diamond2 image
diamond2 = Image("images/diamond.png", game)
diamond2.resizeBy(-87)
diamond2.moveTo(50, game.height - 50)

#Trident images
tridents = []

for i in range(10):
    t = Image("images/trident.png", game)
    t.resizeBy(-70)
    tridents.append(t)
positionObjects(tridents)

#Trident image
trident = Image("images/trident.png", game)
trident.resizeBy(-70)

#Trident2 image
trident2 = Image("images/trident.png", game)
trident2.resizeBy(-70)
trident2.moveTo(220, game.height - 50)

#Weapon to shoot using the tridents
weapon = Image("images/trident.png", game)
weapon.resizeBy(-70)
weapon.setSpeed(8,270)
#weapon.visible = False

#font
f = Font( white, 48, black, "Cosmic Sans MS")

#Game Start Screen Images
title = Image("images/title.png", game)
title.resizeBy(-35)
title.moveTo(400, 127)
scuba.y = 250

#story acts as a placeholdher for story_on and story_off
story = Image("images/story1.png", game)
story.resizeBy(-20)
story.y = 550
story_off = Image("images/story1.png", game)
story_on = Image("images/story2.png",game)

storyText = Image("images/storytext.png", game)
storyText.resizeBy(30)
storyText.visible = False

#howto acts as placeholder for howto_on and howto_off
howtoplay = Image("images/howtoplay1.png",game)
howtoplay.resizeBy(-20)
howtoplay.y = 450
howtoplay_off = Image("images/howtoplay1.png",game)
howtoplay_on = Image("images/howtoplay2.png",game)

howtoplayText = Image("images/howtoplaytext.png", game)
howtoplayText.resizeBy(30)
howtoplayText.visible = False

#play acts as placeholder for play_on and play_off
play = Image("images/play1.png",game)
play.resizeBy(-20)
play.y = 350
play_off = Image("images/play1.png",game)
play_on = Image("images/play2.png",game)


#Game End Screen Images
gameover = Image("images/GameOver.png", game)
gameover.y = 100

YouWin = Image("images/YouWin.png", game)

YouLose = Image("images/YouLose.png", game)
#Game Start Screen
mouse.visible = False

while not game.over:
    game.processInput()
    bk.draw()

    #Image for start screen
    title.draw()
    scuba.draw()
    story.draw()
    howtoplay.draw()
    play.draw()
    # draw how to play text and story text
    howtoplayText.draw()
    storyText.draw()
    #trident is the pointer for the start screen
    weapon.moveTo(mouse.x, mouse.y)

    #interaction with trident and the images in the start screen
    if weapon.collidedWith(play,"rectangle"):
        play.setImage(play_on.image)#makes the color of the image dark blue
    else:
        play.setImage(play_off.image) #makes the color of the image light blue

    if weapon.collidedWith(howtoplay,"rectangle"):
        howtoplay.setImage(howtoplay_on.image)#makes the color of the image dark blue
    else:
        howtoplay.setImage(howtoplay_off.image) #makes the color of the image light blue

    if weapon.collidedWith(story,"rectangle"):
        story.setImage(story_on.image)#makes the color of the image dark blue
    else:
        story.setImage(story_off.image) #makes the color of the image light blue

    #How to play text image
    if weapon.collidedWith(howtoplay, "rectangle") and mouse.LeftClick:
        howtoplayText.visible = True

    #Story text image
    if weapon.collidedWith(story, "rectangle") and mouse.LeftClick:
        storyText.visible = True
        
    #How to close the how to play text or story text & retun to the start screen
    if keys.Pressed[K_SPACE]:
        howtoplayText.visible = False
        storyText.visible = False

    #Interaction with play image
    if weapon.collidedWith(play, "rectangle") and mouse. LeftClick:
        game.over = True
        
    game.update(30)

#Game
game.over = False

#Level 1 Game Loop
while not game.over:
    game.processInput()
    bk.draw()

    scuba_update()
    power_update()
  
    for i in range(len(swordfishs)):
        swordfishs[i].move()
        if scuba.collidedWith( swordfishs[i] ):
            scuba.health -= 4
            swordfishs[i].visible = False
            
    for i in range(len(goldbars)):
        goldbars[i].move()
        if scuba.collidedWith( goldbars[i]):
            goldbars[i].visible = False
            game.score += 1
        
    
    #Game Score for Goldbars
    goldbar2.draw()
    game.drawText("x " + str(game.score), 90, game.height - 70, f)
    
    #Ammo count text
    trident2.draw()
    game.drawText("x " + str(scuba.ammo), 250, game.height -70, f)
    
    if game.score == 20 or scuba.health <= 0:
        game.over = True
        
    game.drawText("Level 1", 10, 5)
    
    game.update(30)

#Level 2
game.over = False
positionObjects(healthpods)
positionObjects(tridents)
positionObjects(sharks)
positionObjects(orcas)

#Level 2 Game Loop

game.score = 0 #Reset value of game score for 2nd level
while not game.over and scuba.health > 0:
    game.processInput()
    bk.draw()

    weapon.move()
    scuba_update()
    power_update()
    
    for i in range(len(sharks)):
        sharks[i].move()
        if scuba.collidedWith(sharks[i]):
            scuba.health -= 10
            sharks[i].visible = False

        if weapon.collidedWith(sharks[i]):
            sharks[i].visible = False
            weapon.visble = False

    for i in range(len(orcas)):
        orcas[i].move()
        if scuba.collidedWith(orcas[i]):
            scuba.health -= 10
            orcas[i].visible = False


        if weapon.collidedWith(orcas[i]):
            orcas[i].visible = False
            weapon.visibe = False
    
    for i in range(len(diamonds)):
        diamonds[i].move()

        if scuba.collidedWith( diamonds[i]):
            diamonds[i].visible = False
            game.score += 1

    #Scuba shooting tridents
    if keys.Pressed[K_SPACE] and scuba.ammo > 0 and weapon.visible == False:
        weapon.moveTo( scuba.x, scuba.y )
        scuba.ammo -= 1
        weapon.visible = True
        
    if weapon.y < 0:
        weapon.visible = False
        
    #Game Score for Diamonds
    diamond2.draw()
    game.drawText("x " + str(game.score), 90, game.height -70, f)

    #Ammo count text
    trident2.draw()
    game.drawText("x " + str(scuba.ammo), 250, game.height -70, f)
    
    if game.score == 10 or scuba.health == 0:
        game.over = True

    
    game.drawText("Level 2", 10, 5)
                      
    game.update(30)

#Level 3
game.over = False
positionObjects(healthpods)

#Level 3 Game loop

while not game.over and scuba.health > 0:
    game.processInput()
    bk.draw()

    scuba_update()
    power_update()
    megaladon.move()

    if scuba.collidedWith(megaladon):
        scuba.health -= 20


    if weapon.collidedWith(megaladon):
        megaladon.health -= 10

    if megaladon.health < 0:
        megaladon.visble = False
        game.over = True

    #Display for Megaladon's health
    megaladon2.draw()
    game.drawText(":" + str(megaladon.health), 90, game.height - 70, f)
    
    #Ammo count text
    trident2.draw()
    game.drawText("x " + str(scuba.ammo), 250, game.height -70, f)
    game.drawText("Level 3", 10, 5)

    #Scuba shooting tridents
    if keys.Pressed[K_SPACE] and scuba.ammo > 0 and weapon.visible == False:
        weapon.moveTo( scuba.x, scuba.y )
        scuba.ammo -= 1
        weapon.visible = True
        
    if weapon.y < 0:
        weapon.visible = False

    if scuba.health < 0:
        game.over = True
        
    game.update(30)
#Game Over Screen
game.over = False

while not game.over:
    game.processInput()
    bk.draw()

    gameover.draw()

    #You win and You lose Images
    if scuba.health >= 0:
        YouWin.draw()
    else:
        YouLose.draw()

    game.update(30)
game.quit()
