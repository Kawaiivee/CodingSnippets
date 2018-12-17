from turtle import *
from collections import deque
import random
import sys

S = Screen()
WIDTH = 480
HEIGHT = 360
S.setup(WIDTH, HEIGHT)
S.bgcolor("#000000")
S.tracer(3)

P1 = Turtle()
P1.hideturtle()
P1.penup()
P1.color("#00FF00")
P1.setpos(0,0)
#P1.pendown()

dotsize = 10
distance = 5
behavior = .5
set = 5
shapes = {}		#append to this one for each defined entity-object on screen
body = deque([])
bodysize = 8

def Player1():
	P1.dot(dotsize)
	tmp = P1.pos()
	body.append(tmp)
	rX = tmp[0]+random.randint(-set,set)*distance
	rY = tmp[1]+random.randint(-set,set)*distance
	if rX > behavior*WIDTH:
		rX = -tmp[0]+random.randint(-set,set)*distance
	if rX < -behavior*WIDTH:
		rX = tmp[0]+random.randint(set,set)*distance
	if rY > behavior*HEIGHT:
		rY = -tmp[1]+random.randint(-set,set)*distance
	if rY < -behavior*HEIGHT:
		rY = tmp[0]+random.randint(set,set)*distance
	P1.setpos(rX,rY)

P2 = Turtle()
P2.hideturtle()
P2.pen()
P2.color("#000000")
P2.setpos(0,0)

def Player2():
	if len(body)> bodysize:
		tmp = body.popleft()
		P2.setpos(tmp)
		P2.dot(dotsize)
	else:
		pass

#paints 1 frame of all objects in local 'shapes' dictionary
def paint():
	for objects in shapes:
		shapes[objects]()

def main():
	if len(sys.argv) > 1:
		flag = sys.argv[1]
	else:
		flag = ''
	#manually iterate frames
	if flag == '-i':
		S.onkey(paint, 'z')
		S.onkey(paint, 'x')
		S.onkey(exit, 'q')
		S.listen()
		mainloop()

	#update frame automatically
	else:
		paint()
#append to dictionary all the shape-entity-objects here
shapes['p1'] = Player1
shapes['p2'] = Player2
while True:
	main()
