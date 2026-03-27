from turtle import Turtle
#####################
#remember the screen setup was [[ (1000,500) ]]
#####################

class ScreenUI(Turtle):
    def __init__(self):
        super().__init__()
        #
        self.shape("square")
        self.color("white")
        self.pensize(10)
        self.speed(10000)
        self.hideturtle()
        #---------------------
        self.penup()
        self.goto(0,250)
        #
        self.pendown()
        self.goto(490, 250)
        self.goto(490, -245)
        #
        self.goto(-500, -245)
        self.goto(-500, 250)
        self.goto(500, 250)
        self.penup()
        #---------------------
        self.goto(0, 250)
        #---------------------

#__________________________________
    def draw_midline(self):
        self.penup()
        self.goto(0, 245)
        #
        drawing_midline = True
        reached_end = False
        self.shape("square")

        while drawing_midline:
            #
            self.setheading(270)
            self.pensize(5)

            # -------------#
            if self.ycor() % 2 == 0:
                self.penup()
                self.forward(21)
            else:
                self.pendown()
                self.forward(21)


            #-------------#stop<!>
            if self.ycor() <= -230:
                reached_end = True
            if reached_end:
                drawing_midline = False
