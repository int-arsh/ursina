from ursina import *
import random as rn

speed1 = 0.1
speed2 = -0.1


def update():
    global speed1,speed2

    cube1.x += speed1
    if abs(cube1.x) >= 4:
        speed1 *= -1

    cube2.y += speed2
    if abs(cube2.y) >= 4:
        speed2 *= -1

    cube3.x += speed2
    if abs(cube3.x) >= 4:
        speed2 *= -1

    cube4.y += speed1
    if abs(cube4.y) >= 4:
        speed1 *= -1

    cube5.x += speed2
    if abs(cube5.x) >= 4:
        speed2 *= -1

    cube5.y += speed2
    if abs(cube5.y) >= 4:
        speed2 *= -1

    cube6.x += speed1
    if abs(cube6.x) >= 4:
        speed1 *= -1

    cube6.y += speed2
    if abs(cube6.y) >= 4:
        speed2 *= -1

    cube7.x += speed1
    if abs(cube7.x) >= 4:
        speed1 *= -1

    cube7.y += speed1
    if abs(cube7.y) >= 4:
        speed1 *= -1

    cube8.x += speed2
    if abs(cube8.x) >= 4:
        speed2 *= -1

    cube8.y += speed1
    if abs(cube8.y) >= 4:
        speed1 *= -1

    


    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)

    cube1.color = color.rgb(r,g,b)
    cube2.color = color.rgb(r,g,b)
    cube3.color = color.rgb(r,g,b)
    cube4.color = color.rgb(r,g,b)
    cube5.color = color.rgb(r,g,b)
    cube6.color = color.rgb(r,g,b)
    cube7.color = color.rgb(r,g,b)
    cube8.color = color.rgb(r,g,b)


app = Ursina()

cube1 = Entity(model="cube", scale=1)
cube2 = Entity(model="cube", scale=1)
cube3 = Entity(model="cube", scale=1)
cube4 = Entity(model="cube", scale=1)

cube5 = Entity(model="cube", scale=1)
cube6 = Entity(model="cube", scale=1)
cube7 = Entity(model="cube", scale=1)
cube8 = Entity(model="cube", scale=1)



# camera.position = (3,3,-20)
app.run()
