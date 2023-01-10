from ursina import *
import random as rn


def update():
    cube.x += 0.01
    # cube.y += 0.01
    # cube.z += 0.1
    # cube.rotation_x += 1
    # cube.rotation_y += 1
    cube.rotation_z += 1

    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    cube.color = color.rgb(r,g,b)


app = Ursina()

cube = Entity(model="cube", color=color.rgb(200,200,0), scale=2)

app.run()