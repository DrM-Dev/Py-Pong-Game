from turtle import Turtle
#########################
player_1_paddle = []
player_2_paddle = []

class PlayerPaddle(Turtle):
    def __init__(self, paddle_size):
        super().__init__()
        #
        self.penup()
        self.hideturtle()
        #
        self.shape("square")
        self.color("white")
        self.shapesize(paddle_size)
        #
        self.p1_direction = ""
        self.p2_direction = ""

#___________________________________________________
    def spawn_players(self):
        global player_1_paddle
        global player_2_paddle
        # ___________________PLAYERS:
        # PLAYER1
        # player_1_paddle = []
        for p1_segments in range(0, 5):
            p1_segments = PlayerPaddle(2)
            player_1_paddle.append(p1_segments)
        # ---#
        p1_seg_spacer = 20
        for segments in player_1_paddle:
            segments.speed(1000)
            #
            segments.goto(-500, p1_seg_spacer)
            p1_seg_spacer -= 10
            segments.showturtle()
            #
            segments.speed(1)
            # to make it 20, 10, 0, -10, -20 segments


        #==========================================================
        # PLAYER2
        # player_2_paddle = []
        for p2_segments in range(0, 5):
            p2_segments = PlayerPaddle(2)
            player_2_paddle.append(p2_segments)
        # ---#
        p2_seg_spacer = 20
        for segments in player_2_paddle:
            segments.speed(1000)
            #
            segments.goto(490, p2_seg_spacer)
            p2_seg_spacer -= 10
            segments.showturtle()
            #
            segments.speed(1)
            # to make it 20, 10, 0, -10, -20 segments



#=======================================================================P1 MOVEMENT:
    #___________________________#re-directors / changing movement
    def p1_move_up(self):
        self.p1_direction = "UP"
        # print("command_UP") #DEBUG

    def p1_move_down(self):
        self.p1_direction = "DOWN"
        # print("command_DOWN") #DEBUG

    def p1_hault(self):
        self.p1_direction = "HAULLLTTTT"
        # print("command_DOWN") #DEBUG

    ####################################################
    #note: boarders are from y=210 to -200   -    the screen setup was [[ (1000,500) ]]
    ####################################################
    def move_p1(self):         #engine / drives
        global player_1_paddle
        #___________________________Boarders for P1_paddle
        p1_middle = player_1_paddle[2]  # 2 is middle seg :)
        # ----------
        # Boarders for P1_paddle
        p1_y = p1_middle.ycor()  # boarders are 210 to -210

        #___________________________
        # print("RECEIVED COMMAND")  # DEBUG
        if self.p1_direction == "UP" and p1_y < 210:
            for segments in player_1_paddle:
                segments.setheading(90)
                segments.forward(20)
                #
                # print("^^^^^") #DEBUG
        #___________________________
        if self.p1_direction == "DOWN" and p1_y > -200:
            for segments in player_1_paddle:
                segments.setheading(270)
                segments.forward(20)
                #
                # print("vvvvvv") #DEBUG



#=======================================================================P2 MOVEMENT:
    #___________________________#re-directors / changing movement
    def p2_move_up(self):
        self.p2_direction = "UP"
        # print("command_UP") #DEBUG

    def p2_move_down(self):
        self.p2_direction = "DOWN"
        # print("command_DOWN") #DEBUG

    def p2_hault(self):
        self.p2_direction = "HAULLLTTTT"
        # print("command_DOWN") #DEBUG

    ####################################################
    #note: boarders are from y=250 to -250   -    the screen setup was [[ (1000,500) ]]
    ####################################################
    def move_p2(self):         #engine / drives
        global player_2_paddle
        #___________________________Boarders for P2_paddle
        p2_middle = player_2_paddle[2]  # 2 is middle seg :)
        # ----------
        # Boarders for P2_paddle
        p2_y = p2_middle.ycor()  # boarders are 210 to -210

        #___________________________
        # print("RECEIVED COMMAND")  # DEBUG
        if self.p2_direction == "UP" and p2_y < 210:
            for segments in player_2_paddle:
                segments.setheading(90)
                segments.forward(30)
                #
                # print("^^^^^") #DEBUG
        #___________________________
        if self.p2_direction == "DOWN" and p2_y > -200:
            for segments in player_2_paddle:
                segments.setheading(270)
                segments.forward(30)
                #
                # print("vvvvvv") #DEBUG
