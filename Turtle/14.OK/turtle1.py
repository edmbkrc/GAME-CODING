"""
from turtle import Turtle, Screen

tosbaga = Turtle()

tosbaga.shape("turtle")
tosbaga.color("turquoise")
tosbaga.forward(200)

my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()

from turtle import Turtle, Screen

tosbaga = Turtle()
tosbaga.forward(100)
tosbaga.right(90)
tosbaga.forward(100)
tosbaga.right(90)
tosbaga.forward(100)
tosbaga.right(90)
tosbaga.forward(100)

my_screen = Screen()
my_screen.exitonclick()

from turtle import Turtle, Screen

tosbaga = Turtle()

for i in range(4):
    tosbaga.forward(100)
    tosbaga.right(90)


my_screen = Screen()
my_screen.exitonclick()
"""
from turtle import Turtle, Screen
import random

tosbaga = Turtle()

renkler = ["AliceBlue","blue4","DarkOrchid4","coral2","aquamarine4","BlueViolet","beige","black"]

def sekil_ciz(kenar_sayisi):
    aci = 360 / kenar_sayisi

    for i in range(kenar_sayisi):
        kenar_sayisi = 11
        tosbaga.forward(50)
        tosbaga.right(aci)

for x in range(3, 21):
    tosbaga.color(random.choice(renkler))
    sekil_ciz(x)


my_screen = Screen()
my_screen.exitonclick()