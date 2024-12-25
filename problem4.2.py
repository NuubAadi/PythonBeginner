"""
Two friends decide who gets the last slice of a cake
by flipping a coin five times. The first person to
win three flips wins the cake. An input of 1 means
player 1 wins a flip, and a 2 means player 2 wins
a flip. Design an algorithm to determine who takes
the cake?
"""
player1_win = 0
player2_win = 0
for i in range(5):
    flip = int(input(f"Enter the result{i+1}: (1 for player1 win, 2 for player2 win):"))

    if flip==1:
      player1_win += 1
    elif flip==2:
      player2_win += 1
    else:
      print("Invalid input, please enter 1 or 2.")
    
    if player1_win == 3:
      print("Player 1 takes the cake!")
      break
    elif player2_win == 3:
      print("Player 2 takes the cake!")
      break
