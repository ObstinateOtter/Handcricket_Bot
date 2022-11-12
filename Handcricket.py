import random
from tabulate import tabulate

h = ['Stats','Player','Computer']
lst = []

def start():
    print("\n \n \n \n Hand-cricket.py \n \n \n")
    over = int(input('How many overs would you like to play: '))
    global turns
    turns = over*6
    toss = str(input("Odd or Eve[odd/eve]: "))
    c_toss = random.randint(1,10)
    u_toss = int(input("Enter a number from 1-10: "))
    print("The computer rolled a ",c_toss)
    res = u_toss + c_toss
    print("Total =  ",res)
    comp_list = ['bat','bowl']
    c_choice = random.choice(comp_list)
    if toss.lower() == 'eve':
        if res % 2 == 0:
            lst.append(('Toss','Won','Lost'))
            print('You won the toss')
            choice = input("Would you like to Bat or Bowl first[bat/bowl]: ")
            if choice.lower() == 'bat':
                bat_first()
            else:
                bowl_first()
        else:
            lst.append(('Toss','Lost','Won'))
            if c_choice == 'bat':
                print("The computer chose to bat.\n")
                bowl_first()
            else:
                print("The Computer chose to bowl first.\n")
                bat_first()
    elif toss.lower() == 'odd':  #toss is odd
        if res%2 != 0:
            lst.append(('Toss','Won','Lost'))
            print('You won the toss')
            choice = input("Would you like to Bat or Bowl first[bat/bowl]: ")
            if choice.lower() == 'bat':
                bat_first()
            else:
                bowl_first()
        else:
            lst.append(('Toss','Lost','Won'))
            if c_choice == 'bat':
                print("The computer chose to bat.\n")
                bowl_first()
            else:
                print("The Computer chose to bowl first.\n")
                bat_first()
    else:
        print('Invalid Input!!! \n')
        start()




def bat_first():
    print("\n \n Batting \n")
    i = 0
    a = 0
    b = 0
    while i < turns : #bat
        user1 = int(input("Enter number from 1-10: "))
        comp1 = random.randint(1,10)
        if user1 > 10:
            print("Invalid Input")
        else:
            if user1 != comp1:
                print("The Computer rolled a ",comp1)
                a = user1 + a
                print("You are at ",a," runs")
                i += 1
                continue
            else:
                print("Out!")
                print("You scored ",a," runs")
                break
    print("\n \n Bowling \n")
    while b < a: #bowl
        user2 = int(input("Enter number from 1-10: "))
        comp2 = random.randint(1,10)
        if user2 > 10:
            print("Invalid Input")
        else:
            if user2 != comp2:
                print("The Computer hit ",user2," runs")
                b = user2 + b
                print("The Computer is at ",b," runs")
                i += 1
                continue
            else:
                print("Out!")
                print("The Computer scored ",b," runs")
                print("You scored ",a," runs")
                break
    if a >= b:
        print("\n \n You win!!! \n")
    else:
        print("\n \n You lost \n")
    lst.append(('Runs',a,b))
    print(tabulate(lst,headers=h,tablefmt='fancy_grid'))
    lst.clear()

def bowl_first():
    print("\n \n Bowling \n")
    i = 0
    c = 0
    d = 0
    while i < turns : #bowl
        user3 = int(input("Enter number from 1-10: "))
        comp3 = random.randint(1,10)
        if user3 > 10:
            print("Invalid Input")
        else:
            if user3 != comp3:
                print("The Computer hit ",comp3," runs")
                c = comp3 + c
                print("The Computer is at ",c," runs")
                i += 1
                continue
            else:
                print("Out!")
                print("The Computer scored ",c," runs")
                break
    print("\n \n Batting \n")
    while d < c: #bat
        user4 = int(input("Enter number from 1-10: "))
        comp4 = random.randint(1,10)
        if user4 > 10:
            print("Invalid Input")
        else:
            if user4 != comp4:
                d = user4 + d
                print("The Computer rolled a ",comp4)
                print("You are at ",d," runs")
                i += 1
                continue
            else:
                print("Out!")
                print("You scored ",d," runs")
                print("The Computer scored ",c," runs")
                break
    if d >= c:
        print("\n \n You win!!! \n")
    else:
        print(" \n \n You lost. Beter Luck next time. \n")
    lst.append(('Runs',d,c))
    print(tabulate(lst,headers=h,tablefmt='fancy_grid'))
    lst.clear()


start()


while True:
    ans = input("Would you like to play again?[y/n]: ")
    if ans == "y":
        start()
    else:
        print("Thank you for playing!!!")
        exit()