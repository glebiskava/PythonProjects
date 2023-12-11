
import turtle

s = turtle.getscreen()

t =  turtle.Turtle()

#shortened versions
# t.rt() instead of t.right()
# t.fd() instead of t.forward()
# t.lt() instead of t.left()
# t.bk() instead of t.backward()

t.penup()
t.setpos(0, -350)
t.shape("turtle")
t.speed(5)
t.pendown()
t.pencolor("green")
t.fillcolor("green")
t.pensize(3)


i = True
n = 10

while i == True:
    t.circle(n)
    n = n+7.5
    
