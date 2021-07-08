import turtle
import time
import random

WIDTH,HEIGHT = 500,500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

#ASK USERS FOR THE NUMBER OF TURTLES
def racers_input():
	while True:
		racers = input("Please select the number of racers(1-10): ")
		if racers.isdigit():
		   racers = int(racers)
		else:
			print('Number of racers is not numeric. Please select again!')
			continue
		if 2 <= racers <= 10:
			return racers
		else:
			print('Number of racers should be between 2 and 10. Please select again!')

#DRAW THE FINISH LINE
def _finish_line():
	t = turtle.Turtle()
	t.color('red')
	t.speed(8)
	t.penup()
	t.setpos(-WIDTH/2,HEIGHT/2-10)
	t.pendown()
	t.forward(WIDTH+10)

#INITIATE GAME SCREEN
def screen_init():
	screen = turtle.Screen()
	screen.setup(WIDTH,HEIGHT)
	screen.title("Turtle Race")
	_finish_line()

#CREATE TURTLES
def create_turtles(racers_num):
	racers = []

	distance = WIDTH/(racers_num+1)
	x = - WIDTH/2

	for i in range(racers_num):
		x += distance
		t = turtle.Turtle()
		t.shape('turtle')
		t.color(COLORS[i])
		t.left(90)
		t.penup()
		t.setpos(x, -150)
		t.pendown()
		# print(t.pos())
		racers.append(t)

	return racers

#START THE RACE
def race(racers):

	while True:
		for racer in racers:
			pace = random.randrange(5,20)
			racer.forward(pace)

			x, y = racer.pos()
			if y>= HEIGHT/2 -10:
				return COLORS[racers.index(racer)]

def play_again():
	play = input('Do you want to play again(Y or N): ')
	if play.upper()[0] == 'Y':
		return True
	else:
		return False

if __name__ == "__main__":

	while True:
		racers_num = racers_input()
		screen_init()
		racers = create_turtles(racers_num)
		winner = race(racers)
		print("\n{} WINS!!!\n".format(winner.upper()))
		if play_again():
			turtle.clearscreen()
		else:
			print('\nTHANK YOU FOR PLAYING!!!')
			break





