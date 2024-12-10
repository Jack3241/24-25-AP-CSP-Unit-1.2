# Initialization of turtles and images
import turtle as trtl
import random as rand

apple_image = "apple.gif"
basket_image = "basket.jpg"

wn = trtl.Screen()
wn.setup(width=1, height=1)
#make screen aware of new files
wn.addshape(apple_image)
wn.addshape(basket_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.showturtle()
    wn.update()




wn.mainloop()