# Initialization of turtles and images
import turtle as trtl
import random as rand

apple_image = "apple.gif"
basket_image = "basket.gif"
xcor = 0
ycor = 50
ground_height = -200
basket_height = -180

wn = trtl.Screen()
wn.setup(width=2, height=2)
#make screen aware of new files
wn.addshape(apple_image)
wn.addshape(basket_image)
wn.bgpic("background.gif")

# set score up to left corner a screen
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(220, 250)
score_writer.pendown()

font_setup = ("Arial", 20, "normal")
score = 0
direction_list = "a" "d"
apple = trtl.Turtle()
apple.penup()

basket = trtl.Turtle()
basket.penup()

def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.showturtle()
    wn.update()

def draw_basket(active_basket):
    active_basket.shape(basket_image)
    basket.showturtle()
    wn.update()
    basket.speed(0)
    basket.goto(0, basket_height)

def drop_apple():
    apple.speed(2)
    apple.goto(xcor, ground_height)
    apple.clear()
    apple.hideturtle()

def basket_left():
    basket.left(90)
    basket.forward(10)
    basket.right(90)

def basket_right():
    basket.right(90)
    basket.forward(10)
    basket.left(90)

def basket_move_left():
    if ("a" in direction_list):
        basket_left()
def basket_move_right():
    if ("d" in direction_list):
        basket_right()





wn.onkeypress(basket_move_left, "a")
wn.onkeypress(basket_move_right, "d")

draw_apple(apple)
draw_basket(basket)
drop_apple()

wn.listen()
wn.mainloop()