import turtle

# Set up the screen
class SetScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("PONG")
        self.screen.tracer(0)

# Create a paddle
class Paddle:
    def __init__(self, screen, x_pos):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x=x_pos, y=0)
        self.screen = screen

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

# The actual game
def main():
    # Create screen and paddle
    game_screen = SetScreen()
    paddle = Paddle(game_screen.screen, 360)

    # Event listeners
    game_screen.screen.listen()
    game_screen.screen.onkey(paddle.go_up, "Up")
    game_screen.screen.onkey(paddle.go_down, "Down")

    # Game loop
    game_is_on = True
    while game_is_on:
        game_screen.screen.update()

    game_screen.screen.exitonclick()

main()




