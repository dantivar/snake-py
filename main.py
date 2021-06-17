from food import Food
from snake import Snake
from turtle import Screen

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0.81, 0.78, 0.77)
screen.title("Py Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
  
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.listen()

def run_game():
  # Snake movement
  snake.move()
  screen.update()

  # Detect collition with food
  if snake.segments[0].distance(food) < 15:
    food.refresh()
  screen.ontimer(run_game, 100)

run_game()
screen.mainloop()
