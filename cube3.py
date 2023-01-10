from ursina import *

def update():
    for cube in cubes:
        cube.rotation_x += 1
        cube.rotation_y += 1



app = Ursina()

cube1 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(3,2,0))
cube2 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(0,-2,0))
cube3 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(0,2,0))
cube4 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(3,-2,0))
cube5 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(-3,2,0))
cube6 = Entity(model="cube", scale=1.5 , texture="sky_sunset", position=(-3,-2,0))

cubes = [cube1,cube2,cube3,cube4,cube5,cube6]

app.run()
