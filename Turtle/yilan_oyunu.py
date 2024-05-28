from turtle import Turtle, Screen
import time
from yilan import Yilan

sc = Screen()
sc.setup = (800, 800)
sc.bgcolor("lightblue")
sc.title("YILAN OYUNU")
sc.tracer(0)  # body ler arasındaki aralıları kapatır

yilan = Yilan()

sc.listen()
sc.onkey(yilan.yukari, "Up")
sc.onkey(yilan.asagi, "Down")
sc.onkey(yilan.saga, "Right")
sc.onkey(yilan.sola, "Left")

oyun = True
while oyun:
    sc.update()  # ekranda guncelleme ve birlikte hareket etmeyi saglar
    time.sleep(0.1)
    yilan.hareket_et()

sc.exitonclick()