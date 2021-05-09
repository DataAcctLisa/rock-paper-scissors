
# The idea is simple: while a certain condition is True, keep doing something. For example:

a = 5
while (a > 0):
    print(a)
    a -= 1
# The output of this code segment is:

#   5
#   4
#   3
#   2
#   1

# A particularly useful way to use while loops is checking user input for correctness. For example:

quit = input('Type "enter" to quit:' )
while quit != "enter":
    quit = input('Type "enter" to quit:' )
# The uses for this are infinite, and can (and should!) be combined with conditionals to yield the most efficient results.



# An infinite loop is a loop that never stops. 
# This means that the condition in the beginning of the while loop will always be true.

# there is an 
# example of this in https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


# meanwhile

# A break statement stops the execution of a loop before the original condition is met. 
# While the use of a break statement will often start an argument about good coding practices, sometimes it is useful.

# For example:

while True: 
    usr_command = input("Enter your command: ")
    if usr_command == "quit": break
    else: 
        print("You typed " + usr_command)
# In this case, the break statement is used to break off the “infinite while loop” 
# that we have constructed with the while True statement.


user1 = input("name of player one: ")
print("name of player one is :", user1)
user2 = input("name of player two: ")
print("name of player two is:", user2)
user1_answer = input("%s,Do you choose rock, paper or scissors?" % user1)
user2_answer = input("%s,Do you choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

# print(compare(user1_answer, user2_answer))

# def ppt():
a= [ 'paper', 'rock', 'scissors']

n = input('Enter rock, paper or scissors : ')

import random

pc= random.choice(a)

print (pc)

if n == 'paper' :

    if pc == 'paper':

        print('Draw')

elif (pc == 'rock'):

    print ('You win!')

else:

    print ('You lose')

if (n == 'rock') :

    if (pc == 'paper'):

        print ('You lose')

elif (pc == 'rock'):

    print ('Draw')

else:

    print ('You win!')

if (n == 'scissors'):

    if (pc== 'rock'):

        print ('You lose')

elif (pc == 'paper'):

    print ('You win')

else:

    print ('Draw')

# else:

    # print ('Invalid input! You have not entered rock, paper or scissors, try again')

