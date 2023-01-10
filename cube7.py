from ursina import *
import random as rn

dx = 0.05

def update():
    global dx
    ball.x += dx

def ball_pos():
    global dx
    dx *= -1

def hello():
    print_on_screen("Hello", position=(rn.randint(-3,3)*-0.1,rn.randint(-3,3)*-0.1))

app = Ursina()

ball = Entity(model="sphere", position=(0,2,0))

b = Button(color=color.azure, scale=0.25, text='Submit', text_color=color.green, text_origin=(0,0), icon="sword")

b.tooltip=Tooltip("Click here")
# b.on_click = hello
b.on_click = ball_pos

app.run()