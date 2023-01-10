from ursina import *

def input(key):
    if key == 'right arrow':
        box.x += 2
    if key == 'left arrow':
        box.x += -2
    if key == 'up arrow':
        box.y += 2
    if key == 'down arrow':
        box.y += -2

    if key == 'c':
        box.color = color.random_color()

    if key == 'x':
        box.rotation_x += 45
    if key == 'y':
        box.rotation_y += 45
    if key == 'z':
        box.rotation_z += 45

def update():
    if held_keys['w']:
        box.y += 0.05
    if held_keys['s']:
        box.y -= 0.05
    if held_keys['a']:
        box.x -= 0.05
    if held_keys['d']:
        box.x += 0.05

    if held_keys['r']:
        box.rotation_z += 30

    if held_keys['q']:
        box.color = color.random_color()



app = Ursina()

box = Entity(model="cube", texture="white_cube", scale=1.5, color=color.red)

app.run()
