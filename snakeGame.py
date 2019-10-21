###
# Simple snake game based on SimpleGraphics
# Random Movement of badger
# Time increases when snake eats fruit
#Time decreases from one fruit to another
# Game over if snake hit wall or badger or time is over
###

from SimpleGraphics import *
import random

#Initializing variables
width = 50
height = 50
scale = 10
snake1headx = 10
snake1heady = 10
snake1tailx = 10
snake1taily = 9
badgerx = 5
badgery = 25
badgerdir = 2
fruitx = 40
fruity = 40
snake1energy = 250
snake1dir = 1
snake1alive = True
badgersize = 3

#Render function which is called in game loop
def render() :
	resize( width * scale, height * scale)
	background ("green")
	setColor("yellow")
	rect(fruitx*scale,fruity*scale,1*scale,1*scale)
	setColor("red")
	rect(snake1headx*scale,snake1heady*scale,1*scale,1*scale)
	rect(snake1tailx*scale,snake1taily*scale,1*scale,1*scale)
	setColor("black")
	rect(badgerx*scale,badgery*scale,badgersize*scale,badgersize*scale)
	text(10*scale, 5*scale,str(snake1energy))

	

#Game Loop
while (not closed()) and snake1alive:
	keys = getHeldKeys()
	
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
		
	snake1tailx = snake1headx
	snake1taily = snake1heady
		
	if snake1dir == 1:
		snake1heady -= 1
	elif snake1dir == 2:
		snake1headx += 1
	elif snake1dir == 3:
		snake1heady += 1
	elif snake1dir == 4:
		snake1headx -= 1
		
	snake1energy -= 1
	
	if random.randint(0,100) <= 15:
		badgerdir = random.randint(1,4)
	
	
	if badgerdir == 1:
		badgery -= 1
	elif snake1dir == 2:
		badgerx += 1
	elif badgerdir == 3:
		badgery += 1
	elif badgerdir == 4:
		badgerx -= 1
	
	
	if badgerx < 0:
		badgerx = width
	elif badgerx > width:
		badgerx = 0
	elif badgery < 0:
		badgery = height
	elif badgery > width:
		badgery = 0
		
	if snake1headx > width or snake1energy <= 0 or snake1headx < 0 or snake1heady < 0 or snake1heady > height:
		snake1alive = False
	
	
	if snake1headx == fruitx and snake1heady == fruity:
		snake1energy += 100
		fruitx = random.randint(5,width - 5)
		fruity = random.randint(5,width - 5)
	
	if snake1headx >= badgerx and snake1headx <= badgerx + badgersize:
		if snake1heady >= badgery and snake1heady <= badgery + badgersize:
			snake1alive = False
		
	clear()
	
	render()
	update()
	sleep(0.06)
	
# Showing final message
if snake1alive == False:
	text(250, 250, "Game Over. Your score: " + str(snake1energy))
