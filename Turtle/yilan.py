from turtle import Turtle, Screen

pozisyonlar = [(0, 0), (-20, 0), (-40, 0)]


class Yilan:
    def __init__(self):
        self.parcalar = []
        self.body_olustur()
        self.bas = self.parcalar[0]

    def body_olustur(self):
        for pozisyon in pozisyonlar:
            body = Turtle(shape="square")
            body.color("white")
            body.penup()
            body.goto(pozisyon)
            self.parcalar.append(body)

    def hareket_et(self):
        for i in range(len(self.parcalar) - 1, 0, -1):
            x = self.parcalar[i - 1].xcor()
            y = self.parcalar[i - 1].ycor()
            self.parcalar[i].goto(x, y)
        self.parcalar[0].forward(20)

    def yukari(self):
        if self.bas.heading() != 270:
            self.bas.setheading(90)

    def asagi(self):
        if self.bas.heading() != 90:
            self.bas.setheading(270)

    def sola(self):
        if self.bas.heading() != 0:
            self.bas.setheading(180)

    def saga(self):
        if self.bas.heading() != 180:
            self.bas.setheading(0)