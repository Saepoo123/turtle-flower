import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("white")
for x in range(25):
    for n in range(25):
        tur.color(cs.hsv_to_rgb(n/15,x/25,1))
        tur.right(90)
        tur.circle(200-x*4, 90)
        tur.left(90)
        tur.circle(200-x*4, 90)
        tur.right(180)
        tur.circle(50,24)
t.hiderturtle()        
t.done
