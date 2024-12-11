# Initialization of turtles and images
import turtle as trtl
import random as rand

apple_image = "apple.gif"
basket_image = "basket.gif"
xcor = 0
ycor = 50
ground_height = -200

wn = trtl.Screen()
wn.setup(width=2, height=2)
#make screen aware of new files
wn.addshape(apple_image)
wn.addshape(basket_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

basket = trtl.Turtle()
basket.penup()
wn.tracer(False)

def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.showturtle()
    wn.update()

def draw_basket(active_basket):
    active_basket.shape(basket_image)
    basket.showturtle()
    wn.update()

def drop_apple():
    wn.tracer(True)
    apple.goto(xcor, ground_height)
    apple.clear()
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)

def reset_apple(apple):
    if apple < ground_height:
        newx = rand.randint(-200, 200)
        newy = 0
        apple.goto(newx, newy)


draw_apple(apple)
draw_basket(basket)
drop_apple()
wn.mainloop()