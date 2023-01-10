from ursina import *

speed = 0.05
def update():
    global speed
    ball.x += speed

    hit_info = ball.intersects()
    if hit_info.hit:
        speed *= -1
        ball.color = color.random_color()

        if hit_info.entity in boxes:
            speed *= 1.20
            destroy(hit_info.entity)

app = Ursina()

ball = Entity(model="sphere", scale=0.5, color=color.yellow, collider="box")

box_1 = Entity(model="cube", scale=(1,2,1),position=(2,0,0), color=color.cyan,texture = 'white_cube', collider="box")

box_2 = duplicate(box_1, x=-2)
box_3 = duplicate(box_1, x=4)
box_4 = duplicate(box_1, x=-4)
box_5 = duplicate(box_1, x=6)
box_6 = duplicate(box_1, x=-6)

boxes = [box_1, box_2, box_3, box_4, box_5, box_6]

app.run()