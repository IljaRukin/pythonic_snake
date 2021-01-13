from tkinter import *
import random

class snake():
	def __init__(self):
		#game mechanics
		self.delay = 100
		self.boundry_bottom = 20
		self.boundry_right = 20
		self.play = False
		self.direction = list()
		self.food = list()
		self.snake = list()

		#Snake GUI elements
		self.size = 20
		self.snake_canvas = list()
		self.food_canvas = None
		#self.root = None
		#self.canvas1 = None
		self.GUI()

		#loop game
		while True:
			self.root.after(1000)

			#countdown
			for t in ['3','2','1']:
				countdown = self.canvas1.create_text(200,200, font=("Purisa", 20), text='start in: '+t)
				self.root.update() #display all
				self.root.after(500)
				self.canvas1.delete(countdown)

			#start game
			self.restart()

	def GUI(self):
		#GUI
		self.root = Tk(screenName='snake')
		self.frame1=Frame(self.root, width=self.size*(self.boundry_right+2), height=self.size*(self.boundry_bottom+2))
		self.frame1.pack_propagate(0)
		self.frame1.pack()
		self.canvas1 = Canvas(self.frame1, background='#999999', width=self.size*(self.boundry_right+2), height=self.size*(self.boundry_bottom+2))
		self.canvas1.pack()

		#Buttons
		self.root.bind('<Left>', self.leftKey)
		self.root.bind('<Right>', self.rightKey)
		self.root.bind('<Up>', self.upKey)
		self.root.bind('<Down>', self.downKey)
		self.root.bind('<space>', self.spaceKey)
		return None

	def restart(self):
		###init game
		self.snake = [[1,10]]
		self.direction = [1,0]
		self.play = True
		self.spawn_food()
		#draw boundry
		self.canvas1.create_rectangle((1)*self.size,(1)*self.size,(self.boundry_right+1)*self.size,(self.boundry_bottom+1)*self.size)
		#draw first segment
		self.snake_canvas = [ self.canvas1.create_oval((self.snake[0][0])*self.size,(self.snake[0][1])*self.size,(self.snake[0][0]+1)*self.size,(self.snake[0][1]+1)*self.size, fill='blue') ]
		self.root.update() #display all
		self.root.after(self.delay)
		###game loop
		while self.play == True:
			#move with delay
			self.root.after(self.delay)
			self.root.update() #update tkinter root to update detected button presses
			self.move()
			self.root.update() #display all
		return None

	def spawn_food(self):
		#generate food, repeat until food is not inside snake
		while True:
			self.food = [random.randint(1,20),random.randint(1,20)]
			if self.food not in self.snake:
				break
		#draw food
		self.food_canvas = self.canvas1.create_rectangle((self.food[0])*self.size,(self.food[1])*self.size,(self.food[0]+1)*self.size,(self.food[1]+1)*self.size, fill='orange')
		return None

	def move(self):
		#compute next head
		head = [self.snake[-1][0]+self.direction[0],self.snake[-1][1]+self.direction[1]]

		#test for collisions
		if (head[0]<1) or (head[1]<1) or (head[0]>self.boundry_right) or (head[1]>self.boundry_bottom) or (head in self.snake):
			self.game_over()
			return None

		#append new segment
		self.snake.append(head)
		#draw segment
		self.snake_canvas.append(self.canvas1.create_oval((head[0])*self.size,(head[1])*self.size,(head[0]+1)*self.size,(head[1]+1)*self.size, fill='blue'))

		#if no food eaten, cut last tail segment. else generate new food
		if head!=self.food:
			self.snake.pop(0)
			self.canvas1.delete(self.snake_canvas.pop(0))
		else:
			self.canvas1.delete(self.food_canvas)
			self.spawn_food()
		return None

	def game_over(self):
		self.play = False
		#update screen
		self.canvas1.delete("all")
		over = self.canvas1.create_text(200,200, font=("Purisa", 20), text='Game Over')
		self.root.update() #display all
		self.root.after(1000)
		self.canvas1.delete(over)

		return None

	def spaceKey(self,event):
		self.game_over()
		return None

	def leftKey(self,event):
		self.direction = [-1,0]
		return None

	def rightKey(self,event):
		self.direction = [1,0]
		return None

	def upKey(self,event):
		self.direction = [0,-1]
		return None

	def downKey(self,event):
		self.direction = [0,1]
		return None

if __name__ == '__main__':
	snake()
