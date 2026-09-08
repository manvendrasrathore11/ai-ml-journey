import  turtle as t
import  random



tim = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b  = random.randint(0,255)

    random__colour = (r,g,b)
    return random__colour

def circle_shape(gap_bw):
    for _ in range(int(360/gap_bw)):
        tim.speed("fastest")
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_bw)

circle_shape(3)


scr =  t.Screen()
scr.exitonclick()