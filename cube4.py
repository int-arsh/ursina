from ursina import *

def update():
    cube.rotation_x += 1
    cube.rotation_y += 1

app = Ursina()

cube = Entity(model="cube", scale=2, texture= "cubepe.jpeg")

app.run()

