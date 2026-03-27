from turtle import Turtle
import random

#########################
import score_screen
#==========================================================================Ball Class

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        #
        self.penup()
        self.color("white")
        self.shape("square")
        #
        self.goto(0,0)
        #
        self.x_bounce_modifier = 1
        self.y_bounce_modifier = -1

    # ==========================================================================BOUNCE-Mechanic
    # ----------------------------BOUNCE OFF WALLS\\
    def bounce_upper_wall(self):
        self.y_bounce_modifier = -1

    def bounce_lower_wall(self):
        self.y_bounce_modifier = 1

    #-----------------------------BOUNCE OFF PLAYERS\\
    def bounce_player1_left(self):
        self.x_bounce_modifier = 1

    def bounce_player2_right(self):
        self.x_bounce_modifier = -1

    # ----------------------------re-set:
    def reset_to_p1(self):
        self.goto(0,0)
        #------------------------------
        random_chances = [-1,1]
        #------------------------------
        self.x_bounce_modifier = 1
        #
        self.y_bounce_modifier = random.choice(random_chances)
    # ----------------------------re-set:
    def reset_to_p2(self):
        self.goto(0,0)
        #------------------------------
        random_chances = [-1,1]
        #------------------------------
        self.x_bounce_modifier = -1
        #
        self.y_bounce_modifier = random.choice(random_chances)



    # ==========================================================================Ball Movement
    def move(self):
        direction_x = self.xcor() + 10 * self.x_bounce_modifier # starts + (going to the upper-r
        direction_y = self.ycor() + 10 * self.y_bounce_modifier # starts -
        #--------------
        self.goto(direction_x,direction_y)

        # ==========================================================================
        if direction_y > 230:
            self.bounce_upper_wall()

        if direction_y < -225:
            self.bounce_lower_wall()

        #--------------------------
        if direction_x > 470: #THIS GOAL IS PROTECTED BY PLAYER2
            score_screen.p1_score += 1
            #
            self.reset_to_p2()
            # print("PLAYER-1 GOAL!") #DEBUG


        if direction_x < -480: #THIS GOAL IS PROTECTED BY PLAYER1
            score_screen.p2_score += 1
            #
            self.reset_to_p1()
            # print("PLAYER-2 GOAL!") #DEBUG

    # ==========================================================================
