from ursina import *
import random
 
app = Ursina()

bdx = 0.07
dx = 0.05
dy = 0.05
score = 0
dead = False

txt = ['shore','rainbow','sky_sunset','grass','sky_default',]
bg = Entity(parent=scene, model='quad', texture=txt[random.randrange(len(txt))], scale=(22,12.5), color=color.light_gray)
 
def update():
    global dx, dy, score, dead, bdx
 
    if not(dead):
        if held_keys['right arrow']: board.x += bdx
        if held_keys['left arrow']: board.x -= bdx
 
        ball.x += dx
        ball.y += dy
 
        if ball.x >= 7 or ball.x <= -7: dx *= -1
        if ball.y >= 4: dy *= -1
        if ball.y <= -4: dead = True
        if board.x >= 5: board.x = 5
        if board.x <= -5: board.x = -5

 
        hit_info = ball.intersects()
        if hit_info.hit:
            dy *= -1
            # dx *= -1
 
            if hit_info.entity in boxes:
                ball.color = color.random_color()
                board.color = ball.color
                destroy(hit_info.entity)
                score += 1
                # dx += 0.01
                dy += 0.01
                bdx += 0.01
            
        print_on_screen("SCORE: "+str(score), position=(-0.8,0.5))
 
    else:
        destroy(board)
        destroy(ball)
        for i in boxes:
            destroy(i)
            print_on_screen("GAME OVER!", position=(-0.05,0.2))
            print_on_screen("FINAL SCORE: "+str(score), position=(-0.07,0.15))
 
box_1 = Entity(model="cube", color=color.cyan, texture="brick", scale=(1,0.5,0.5), position=(-10,4,0), collider="box")
boxes = []
for i in range(6,-7,-1):
    for j in range(1,7):
        boxes.append(duplicate(box_1, x=i, y=j/2 + 0.5, color=color.random_color()))
 
board = Entity(model="cube", color=color.orange, texture="brick", scale=(4,0.5,0.5), position=(0,-4,0), collider="box")
ball = Entity(model="sphere", color=color.orange, scale=0.5, position=(0,-2,0), collider="box")
app.run()