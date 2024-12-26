"""
ABC School has allotted unique token IDs from (1 to
600) to all the parents for facilitating a lucky draw
on the day of their Annual day function. The winner
would receive a special prize. Write a program using
Python that helps to automate the task.(Hint: use
random module)
"""
import random
def lucky_draw():
    winner_id = random.randint(1,600)
    return winner_id

winner = lucky_draw()
print(f"The winner of the lucky draw is {winner}")