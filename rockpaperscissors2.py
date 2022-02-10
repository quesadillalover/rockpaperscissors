#Kaitlyn
#January 13, 2022
#Rockpaperscissors2
from random import randint #importing one specific function from library
import random #importing whole library 
from time import sleep 

win= 'You won!'
lose= 'You lost!'

def rock():
    rock= 'rock'
    return rock
def paper():
    paper= 'paper'
    return paper
def scissors():
    scissors= 'scissors'
    return scissors
    

def decide_winner():
    u_score = 0
    c_score = 0
    
    
    while u_score <3 and c_score <3:
        user_choice= input('Choose between Rock, Paper, or Scissors: ')
        options= ['Rock', 'Paper', 'Scissors']
        computer_choice= options[randint(0,2)]
        print('Computer choosing...')
        sleep(3)
        print('Computer chose: ' + computer_choice)
        sleep(1)
        
        if user_choice == computer_choice:
            print(' It is a tie!')
            
        elif user_choice == 'Paper' and computer_choice =='Rock':
            print(win)
            sleep(1)
            u_score = u_score+1
            
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            print(win)
            sleep(1)
            u_score = u_score +1
            
        elif user_choice == 'Rock' and computer_choice == 'Scissors':
            print(win)
            sleep(1)
            u_score = u_score +1
            
        else:
            print(lose)
            c_score = c_score +1
        print('User Score: ' + str(u_score) + " " + "Computer Score: " +str(c_score) + '')
        
        if c_score == 3:
            print("Game Over! Computer Wins!")
        if u_score == 3:
            print('Game Over! User Wins!')
        
decide_winner()


