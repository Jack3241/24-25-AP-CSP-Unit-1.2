import turtle as trtl
import random as rand

# initialize variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()
wall_len = 35
path_width = 30
#Setup turtle
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.speed(0)



#create maze from inside out
def draw_barrier():
    barrier = rand.randint(path_width * 2, (wall_len - path_width))
    maze_painter.forward(barrier - path_width)
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)


for wall in range(21):
    door = rand.randint(path_width * 2, (wall_len + path_width * 2))
    maze_painter.forward(door)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if wall > 5:
        draw_barrier()
    maze_painter.forward(path_width)
    maze_painter.left(90)
    wall_len += 15



wn.listen()
wn.mainloop()