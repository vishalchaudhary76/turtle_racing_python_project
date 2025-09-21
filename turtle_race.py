import turtle
import time
import random

COLORS = ['red', 'green', 'yellow' , 'black', 'grey','blue', 'brown' , 'silver' , 'orange' , 'cyan' ]


WIDTH, HEIGHT = 800,600
 

 
def get_number_of_racers():
    racers=0
    while True:
        try:
            racers=int(input("Enter the number of racers (2 - 10 ): "))
        

            if 2<=racers<=10:
                return racers
            else:
                print("Please select the number between (2 - 10)")
        except ValueError:
            print("Please Enter a valid number...")
def race(colors):
    turtles = create_turtles(color)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles=[]
    spacingx =  WIDTH// (len(colors)+1)
    for i, color in enumerate (colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1) * spacingx ,-HEIGHT//2 + 20)
        racer.pendown()

        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")

racers=get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
color=COLORS[:racers]

winner = race(color)
print("The winner is the turtle with color", winner)

time.sleep(5)
turtle.done() 