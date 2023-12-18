from turtle import Turtle as T
from turtle import Screen
import colorgram

timmy = T()
screen = Screen()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray","SeaGreen"]
def square(a):
    for _ in range(4):
        a.forward(100)
        a.right(90)

def triangle(a):
    for _ in range(3):
        a.forward(100)
        a.right(120)


triangle(timmy)
square(timmy)
screen.exitonclick()