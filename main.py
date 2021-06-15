from typing import runtime_checkable
from snake import Snake
from turtle import Screen

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0.81, 0.78, 0.77)
screen.title("Py Snake Game")
screen.tracer(0)

snake = Snake()
  
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.listen()

def run_game():
  snake.move()
  screen.update()
  screen.ontimer(run_game, 250)

run_game()
screen.mainloop()
