from turtle import *
import random
import time
import sys

S = Screen()
WIDTH = 800
HEIGHT = 400
S.setup(WIDTH, HEIGHT)
S.bgcolor("#000000")
S.tracer(5)

P1 = Turtle()
P1.hideturtle()
P1.pen()
P1.color("#00FF00")
P1.setpos(-WIDTH,HEIGHT)

P2 = Turtle()
P2.hideturtle()
P2.pen()
P2.color("#FF0000")
P2.setpos(-WIDTH,-HEIGHT)

P3 = Turtle()
P3.hideturtle()
P3.pen()
P3.color("#0000FF")
P3.setpos(WIDTH,-HEIGHT)

P4 = Turtle()
P4.hideturtle()
P4.pen()
P4.color("#FFFF00")
P4.setpos(WIDTH,HEIGHT)

dotsize = 1
distance = 2
behavior = 1

def Player1():
	P1.dot(dotsize)
	tmp = P1.pos()
	rX = tmp[0] + random.randint(-10,10)*distance
	rY = tmp[1] + random.randint(-10,10)*distance
	
	if rX < -behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rX > behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rY < -behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	if rY > behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	P1.setpos(rX,rY)
	
def Player2():
	P2.dot(dotsize)
	tmp = P2.pos()
	rX = tmp[0] + random.randint(-10,10)*distance
	rY = tmp[1] + random.randint(-10,10)*distance
	
	if rX < -behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rX > behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rY < -behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	if rY > behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	P2.setpos(rX,rY)
	
def Player3():
	P3.dot(dotsize)
	tmp = P3.pos()
	rX = tmp[0] + random.randint(-10,10)*distance
	rY = tmp[1] + random.randint(-10,10)*distance
	
	if rX < -behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rX > behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rY < -behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	if rY > behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	P3.setpos(rX,rY)
	
def Player4():
	P4.dot(dotsize)
	tmp = P4.pos()
	rX = tmp[0] + random.randint(-10,10)*distance
	rY = tmp[1] + random.randint(-10,10)*distance
	
	if rX < -behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rX > behavior*WIDTH:
		rX = random.randint(-10,10)*distance
	if rY < -behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	if rY > behavior*HEIGHT:
		rY = random.randint(-10,10)*distance
	P4.setpos(rX,rY)
	
def Grid():
	pass

def paint():
	shapes = {'p1':Player1, 'p2':Player2, 'p3':Player3, 'p4':Player4}
	for objects in shapes:
		print('printing objects...')
		shapes[objects]()
		
def main():
	if len(sys.argv) > 1:
		s = sys.argv[1]
	else:
		s = ''
	if s == '-i':
		print("Enter 'i' to iterate:")
		i = input()
		if i == 'i':
			paint()
		elif i == 'q':
			exit()
		else:
			pass
	else:
		paint()
		
while True:
	main()