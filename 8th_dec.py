import turtle
import time
import random

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

    #Paddle Moves Up    
    def go_up(self):
        new_y = self.paddle.ycor() + 30
        self.paddle.goto(self.paddle.xcor(), new_y)
    
    #Paddle Moves down
    def go_down(self):
        new_y = self.paddle.ycor() - 30
        self.paddle.goto(self.paddle.xcor(), new_y)  

    def check_collision_with_paddle(self, paddle):
        # Check if the ball is near the paddle and within paddle's y-range
        if self.ball.xcor() > 340 and paddle.paddle.xcor() > 340:  # Right paddle
            if paddle.paddle.ycor() - 50 < self.ball.ycor() < paddle.paddle.ycor() + 50:
                self.ball.xspeed *= -1  # Reverse horizontal direction
        
        if self.ball.xcor() < -340 and paddle.paddle.xcor() < -340:  # Left paddle
            if paddle.paddle.ycor() - 50 < self.ball.ycor() < paddle.paddle.ycor() + 50:
                self.ball.xspeed *= -1  # Reverse horizontal direction
    

#create the ball
class Ball():
    def __init__(self, screen):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x=0, y=0)
        self.screen = screen
        self.randomize_speed()
        
        # Randomizes the direction in which the ball moves 
        self.ball.xspeed = random.choice([0.2, -0.2])
        self.ball.yspeed = random.choice([0.2, -0.2])
        self.count_left = 0
        self.count_right = 0
    
    #changes the speed after each paddle hit
    def randomize_speed(self):
        self.ball.xspeed = random.choice([0.15, 0.2, -0.15, -0.2])
        self.ball.yspeed = random.choice([0.15, 0.2, -0.15, -0.2])

    #ball moving logix
    def move(self):
        new_x = self.ball.xcor() + self.ball.xspeed
        if self.ball.ycor() > 300 or self.ball.ycor() < -300:
            self.ball.yspeed *= -1  # Will bounce the balls off the top and bottom walls
        new_y = self.ball.ycor() + self.ball.yspeed
        self.ball.goto(new_x, new_y)

    #checks collision with the paddle
    def check_collision_with_paddle(self, paddle):
        # Check if the ball is near the paddle and within paddle's y-range
        if 340 < self.ball.xcor() < 350 and paddle.paddle.xcor() > 340:  # Right paddle
            if paddle.paddle.ycor() - 50 < self.ball.ycor() < paddle.paddle.ycor() + 50:
                self.ball.xspeed *= -1  # Reverse the horizontal direction of the ball so it goes in the opposite direction
                self.ball.goto(340, self.ball.ycor())  # Move the ball away far enough so that there is no double dounce
        
        if -350 < self.ball.xcor() < -340 and paddle.paddle.xcor() < -340:  # same thing but for the left paddle
            if paddle.paddle.ycor() - 50 < self.ball.ycor() < paddle.paddle.ycor() + 50:
                self.ball.xspeed *= -1  # Reverse the horizontal direction
                self.ball.goto(-340, self.ball.ycor())  # Move the ball away far enough so that there is no double dounce
    
    def reset_position_right(self, scoreboard):
        if self.ball.xcor() > 360:
            scoreboard.leftpoint()  # Award point to the left player
            scoreboard.updatescore()  # Update the scoreboard
            self.count_right += 1
            self.ball.goto(x=0, y=0)
            time.sleep(1)
            self.randomize_speed()
            self.ball.xspeed *= -1

        

    def reset_position_left(self, scoreboard):
        if self.ball.xcor() < -360:
            scoreboard.rightpoint()  # Award point to the right player
            scoreboard.updatescore()  # Update the scoreboard
            self.count_left += 1
            self.ball.goto(x=0, y=0)
            time.sleep(1)
            self.randomize_speed()
            self.ball.xspeed *= -1


class Scoreboard():
    def __init__(self,screen):
        self.scoreboard = turtle.Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.leftscore = 0
        self.scoreboard.rightscore = 0
        self.scoreboard.hideturtle()
        self.updatescore()
        self.screen = screen
       
    def updatescore(self):
        self.scoreboard.clear()
        self.scoreboard.goto(-110, 210)
        self.scoreboard.write(self.scoreboard.leftscore, align = "center", font = ("Arial", 70,"normal"))
        self.scoreboard.goto(110,210)
        self.scoreboard.write(self.scoreboard.rightscore, align = "center", font = ("Arial", 70,"normal"))


    def leftpoint(self):
        self.scoreboard.leftscore += 1

    def rightpoint(self):
        self.scoreboard.rightscore += 1

class win_board():
    def __init__(self, screen):
        self.win_board = turtle.Turtle()
        self.win_board.color("white")
        self.win_board.penup()
        self.win_board.hideturtle()
        self.screen = screen

    def leftwin(self):
        self.win_board.goto(100,0)
        self.win_board.write("Player WASD wins", align = "center", font = ("Arial", 50,"normal"))
        

    def rightwin(self):
        self.win_board.goto(100,0)
        self.win_board.write("Player ARROW wins", align = "center", font = ("Arial", 50,"normal"))



# The actual game
def main():
    # Create screen and paddle and ball
    game_screen = SetScreen()
    right_paddle = Paddle(game_screen.screen, 360)
    left_paddle = Paddle(game_screen.screen, -360)
    ball = Ball(game_screen.screen)
    scoreboard = Scoreboard(game_screen.screen)
    winboard = win_board(game_screen.screen)

    # Delay game start by 2 seconds
    time.sleep(2)

    # Event listeners
    game_screen.screen.listen()
    game_screen.screen.onkey(right_paddle.go_up, "Up")
    game_screen.screen.onkey(right_paddle.go_down, "Down")
    game_screen.screen.onkey(left_paddle.go_up, "w")
    game_screen.screen.onkey(left_paddle.go_down, "s")
    

    # Game loop
    game_is_on = True
    while game_is_on:
        game_screen.screen.update()
        ball.move()
        # Check for collisions with paddles
        ball.check_collision_with_paddle(right_paddle)
        ball.check_collision_with_paddle(left_paddle)
        ball.reset_position_right(scoreboard)
        ball.reset_position_left(scoreboard)


        if ball.count_left > 6:
            winboard.leftwin()
            turtle.update()
            time.sleep(3)
            exit()
        
        if ball.count_right > 6:
            winboard.rightwin()
            turtle.update()
            time.sleep(3)
            exit()
        
    game_screen.screen.exitonclick()
main()