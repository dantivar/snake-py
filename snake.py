from turtle import Turtle
import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20

class Snake:
  def __init__(self) -> None:
    self.segments = []
    self.__create_snake()
  
  def __create_snake(self):
    for position in STARTING_POSITIONS:
      new_segment = Turtle('square')
      new_segment.color('purple')
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)
  
  def move(self):
    for seg in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg - 1].xcor()
      new_y = self.segments[seg - 1].ycor()
      self.segments[seg].goto(new_x, new_y)

    self.segments[0].forward(20)

  def up(self):
    if self.segments[0].heading() == 270:
      self.segments[0].setheading(270)
    else:
      self.segments[0].setheading(90)
  
  def down(self):
    if self.segments[0].heading() == 90:
      self.segments[0].setheading(90)
    else:
      self.segments[0].setheading(270)
  
  def left(self):
    if self.segments[0].heading() == 0:
      self.segments[0].setheading(0)
    else:
      self.segments[0].setheading(180)
  
  def right(self):
    if self.segments[0].heading() == 180:
      self.segments[0].setheading(180)
    else:
      self.segments[0].setheading(0)
