from SimpleGraphics import *
import random

'''
game width
game height
scale factor
snake 1 head x/y
snake 1 tail x/y
fruit x/y
energy snake 1/2

'''

width = 50
height = 50
scale = 10
snake1headx = 250
snake1heady = 250
snake1tailx = 10
snake1taily = 9
badgerx = 15
badgery = 25
badger2x = 30
badger2y = 30
badger3x = 20
badger3y = 25
badgerdir = 2
fruitx = random.randint(5, width - 5)
fruity = random.randint(5, width - 5)
snake1energy = 250
snake1dir = 1
snake1alive = True
badgersize = 3
face = loadImage("DiptoFace.gif")
food = loadImage("food.gif")
vh = loadImage("vh.gif")
ulab = loadImage("ulab.gif")
corona = loadImage("corona.gif")


def render():
	resize(width * scale, height * scale)
	background("green")
	setColor("green")
	rect(fruitx*scale, fruity*scale, 1*scale, 1*scale)
	drawImage(food, fruitx*scale-10, fruity*scale-5)
	setColor("black")
	#rect(badgerx*scale, badgery*scale, badgersize*scale, badgersize*scale)
	drawImage(vh, badgerx*scale, badgery*scale)
	#rect(badger2x*scale, badger2y*scale, badgersize*scale, badgersize*scale)
	drawImage(ulab, badger2x*scale, badger2y*scale)
	#rect(badger3x*scale, badger3y*scale, badgersize*scale, badgersize*scale)
	drawImage(corona, badger3x*scale, badger3y*scale)
	text(10*scale, 5*scale, str(snake1energy))
	setColor("green")
	#rect(snake1headx, snake1heady, 39, 55)
	drawImage(face, snake1headx, snake1heady)
	setColor("red")


while (not closed()) and snake1alive:
	keys = getHeldKeys()

	#set dorection as to which key pressed
	if "Up" in keys:
		print("player one up")
		snake1dir = 1
	elif "Right" in keys:
		print("player one right")
		snake1dir = 2
	elif "Left" in keys:
		print("Player one left")
		snake1dir = 4
	elif "Down" in keys:
		print("player one down")
		snake1dir = 3

	if snake1dir == 1:
		snake1heady -= 6
	elif snake1dir == 2:
		snake1headx += 6
	elif snake1dir == 3:
		snake1heady += 6
	elif snake1dir == 4:
		snake1headx -= 6

	snake1energy -= 1

    #FOR BADGER 1
	if random.randint(0, 100) <= 15:
		badgerdir = random.randint(1, 4)

	if badgerdir == 1:
		badgery -= 1
	elif snake1dir == 2:
		badgerx += 1
	elif badgerdir == 3:
		badgery += 1
	elif badgerdir == 4:
		badgerx -= 1

    #FOR BADGER 2
	if random.randint(0, 100) <= 50:
		badgerdir = random.randint(1, 4)

	if badgerdir == 1:
		badger2y -= 1
	elif snake1dir == 2:
		badger2x += 1
	elif badgerdir == 3:
		badger2y += 1
	elif badgerdir == 4:
		badger2x -= 1

	if badger2x < 0:
		badger2x = width
	elif badger2x > width:
		badger2x = 0
	elif badger2y < 0:
		badger2y = height
	elif badger2y > width:
		badger2y = 0

    #FOR BADGER 3
	if random.randint(0, 100) <= 50:
		badgerdir = random.randint(1, 4)

	if badgerdir == 1:
		badger3y -= 1
	elif snake1dir == 2:
		badger3x += 1
	elif badgerdir == 3:
		badger3y += 1
	elif badgerdir == 4:
		badger3x -= 1

	if badger3x < 0:
		badger3x = width
	elif badger3x > width:
		badger3x = 0
	elif badger3y < 0:
		badger3y = height
	elif badger3y > width:
		badger3y = 0

	if snake1headx + 39 > width*scale or snake1energy <= 0 or snake1headx < 0 or snake1heady < 0 or snake1heady + 55 > height*scale:
		snake1alive = False

	print("Fruitx" + str(fruitx*10))
	print("Fruity" + str(fruity*10))
	print("snake1headx" + str(snake1headx))
	print("snake1heady" + str(snake1heady))
    
	if snake1headx <= fruitx*10 and snake1headx + 39 >= fruitx*10:
		print("here")
		if snake1heady <= fruity*10 and snake1heady + 55 >= fruity*10:
			snake1energy += 100
			fruitx = random.randint(5,width - 5)
			fruity = random.randint(5,width - 5)

	if snake1headx <= badgerx*scale + badgersize*scale and snake1headx+39 >= badgerx*scale:
		if snake1heady <= badgery*scale + badgersize*scale and snake1heady+55 >= badgery*scale:
			snake1alive = False
	if snake1headx <= badger2x*scale + badgersize*scale and snake1headx+39 >= badger2x*scale:
		if snake1heady <= badger2y*scale + badgersize*scale and snake1heady+55 >= badger2y*scale:
			snake1alive = False
	if snake1headx <= badger3x*scale + badgersize*scale - 10 and snake1headx+39 >= badger3x*scale:
		if snake1heady <= badger3y*scale + badgersize*scale - 10 and snake1heady+55 >= badger3y*scale:
			snake1alive = False

	clear()
	render()
	update()
	sleep(0.06)

if snake1alive == False:
	text(250, 250, "Game Over. Your score: " + str(snake1energy))
