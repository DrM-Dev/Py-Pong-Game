#Py-PongGame V2  by  Dr.M-Dev:
#====================================================================================
#====================================================================================
# Imports__________________________
from turtle import Screen
import time
#X--X#X--X#X--X#X--X#X--X#X--X#X--X#
from screen_ui import ScreenUI
from player import PlayerPaddle
from player import player_1_paddle, player_2_paddle
#X--X#X--X#X--X#X--X#X--X#X--X#X--X#
from ball_mechanic import Ball
#X--X#X--X#X--X#X--X#X--X#X--X#X--X#
from score_screen import PongScoreScreen


#====================================================================================
print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


print("******** WELCOME TO Py-PongGame V2   -   By: Dr.m DEV *********")
#==========================================================================================================
#______________________________________________________________


#====================================================================
#====================================================================
#====================================================================SET-UP:
#_____________________________________________________SCREEN
my_screen = Screen()
my_screen.setup(1000,500) #the middle is gonna be 0, 500 for each X and -X cor.
my_screen.bgcolor("black")
#__________Tracer
my_screen.tracer(0)
#
my_screen_ui = ScreenUI()
my_screen_ui.draw_midline()
##################
my_screen.title("Py-PongGame  -  Dr.M-Dev")

#___________________________________________________OBJs:
players = PlayerPaddle(2)
players.spawn_players()
#
the_ball = Ball()
#
p1_score_tracker = PongScoreScreen()
p2_score_tracker = PongScoreScreen()

#___________________________________________________SCORE-SCREEN SETUP
p1_score_tracker.go_to_place((-80,190))
p2_score_tracker.go_to_place((80,190))
#
#DEBUG=========================
p1_score_tracker.checking_loc()
p2_score_tracker.checking_loc()

#=====================================================================CONTROLS
# +++++++++++++++++++++++++++++++CONTROLS:
my_screen.listen()
my_screen.onkeypress(key="w", fun=players.p1_move_up)
my_screen.onkeypress(key="s", fun=players.p1_move_down)
#
my_screen.onkeyrelease(key="w", fun=players.p1_hault)
my_screen.onkeyrelease(key="s", fun=players.p1_hault)
##########
my_screen.onkeypress(key="Up", fun=players.p2_move_up)
my_screen.onkeypress(key="Down", fun=players.p2_move_down)
#
my_screen.onkeyrelease(key="Up", fun=players.p2_hault)
my_screen.onkeyrelease(key="Down", fun=players.p2_hault)


#=====================================================================MAIN CODE
game_is_on = True

while game_is_on:
    # Updating the tracer:
    my_screen.update()
    time.sleep(0.05)
    #__________________________Player Movement:
    ##########P1
    players.move_p1()
    players.move_p2()
    #__________________________Ball Movement:
    the_ball.move()
    #--------------------------Calculating Ball to Player Collisions!
    for seg in player_1_paddle:
        if the_ball.distance(seg) < 25:
            the_ball.bounce_player1_left()

    for seg in player_2_paddle:
        if the_ball.distance(seg) < 25:
            the_ball.bounce_player2_right()

    #___________________________Score_checker:
    p1_score_tracker.p1_scored()
    p2_score_tracker.p2_scored()

#=====================================================================END OF CODE
my_screen.mainloop()
