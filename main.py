from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.window_width()
screen.window_height()

def move_fd():
    tim.fd(10)

def move_bck():
    tim.bk(10)

def move_lt():
    tim.left(10)

def move_rt():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkeyrelease(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bck)
screen.onkey(key="a", fun=move_lt)
screen.onkey(key="d", fun=move_rt)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
