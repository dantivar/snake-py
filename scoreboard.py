from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("purple")
    self.penup()
    self.goto(0, 260)    
    self.hideturtle()
    self.refresh()
  
  def refresh(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.refresh()
