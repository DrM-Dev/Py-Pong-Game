from turtle import Turtle
#___________________________________________________Players_Score:
p1_score = 0
p2_score = 0
#__________________________________________

class PongScoreScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def go_to_place(self,location):
        self.goto(location[0],location[1])

    #------------------------------------------------
    def checking_loc(self):
        self.write(f"0", align="Center", font=("Times New Roma", 38, "normal"))

    #------------------------------------------------
    def p1_scored(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x,y)
        #
        self.clear()
        self.write(f"{p1_score}", align="Center", font=("Times New Roma", 38, "normal"))

    def p2_scored(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x,y)
        #
        self.clear()
        self.write(f"{p2_score}", align="Center", font=("Times New Roma", 38, "normal"))
