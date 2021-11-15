#-----------screan-----------
import turtle
import time
win = turtle.Screen()
win.bgcolor ("black")
win.setup(width=600, height=600)
win.title("Arvins clock")
#---------clock face-------
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen._tracer(0)

pen.pensize(3)
def draw_clock(h,m,s ,pen):
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(210)
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    #------------clock hour-------
    for x in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    #--------the clock hand------
    pen.penup()
    pen.pensize(6)
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(130)


    pen.penup()
    pen.pensize(4)
    pen.goto(0,0)
    pen.color("brown")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)



    pen.penup()
    pen.pensize(1)
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(200)

while True:
    h = int (time.strftime("%I"))
    m = int (time.strftime("%M"))
    s = int (time.strftime("%S"))
    
    
    




    draw_clock(h,m,s,pen)


    win.update()

    time.sleep(1)

    pen.clear()



win.mainloop()

