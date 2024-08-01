from random import *
from time import *
Main_room = 0
balance = int(input("input a starter balance:$"))
Quit = False
headbackstr = "0"
def headback():
    headbackstr = input("Would you like to head back to the lobby? (Y/N)")
    if headbackstr == "Y":
        global Main_room
        Main_room = 0
        print("Okay! Heading back...")
        sleep(1.3)
    elif headbackstr == "N":
        print("Okay! Restarting the game..")
        sleep(1.3)
    else:
        headbackstr = input("Please enter a valid option.")
while Quit == False:
    while Main_room == 0:
        Main_room = int(input("You are in the lobby of the Javaleti Casino! What would you like to do? 1.Head Over to the Baccarat room | 2.Head Over to the Craps room | 3.Head over to the slot machine room. | 4.Check your balance | 5.Exit the casino:"))
    if Main_room == 1:
                Baccarat_bet = int(input("Make a Bet: $"))
                balance -= Baccarat_bet
                Baccarat_choice = str(input("Choose a hand: Banker or Player? (in lowercase)"))
                sleep(1.2)
                player = randint(1,9)
                banker = randint(1,9)
                print("Banker:", banker)
                sleep(0.5)
                print("player:", player)
                sleep(1.1)
                if banker == player:
                    print("Draw! You keep your money.")
                elif banker > player:
                    Baccarat_winner = "banker"
                else:
                    Baccarat_winner = "player"
                
                if Baccarat_winner == Baccarat_choice:
                    print("Well done! You win! your bet was multiplied by 1.5x and added to your balance! GGs")
                    balance += Baccarat_bet * 1.5
                else:
                    print("You lose! You lost your bet money.")
                    balance -= Baccarat_bet
                
                headback()
        
        
    elif Main_room == 2:
            Craps_points = 0
            Craps_opp_points = 0
            Craps_bet = int(input("Make a Bet: $"))
            balance -= Craps_bet
            Craps_choice1 = int(input("Guess what the outcome of the first dice roll will be (1 to 6):"))
            Craps_choice2 = int(input("Guess what the outcome of the second dice roll will be (1 to 6):"))
            print("Rolling the first dice...")
            sleep(2)
            Craps_roll1 = randint(1,6)
            print("Rolling the second dice...")
            sleep(2)
            Craps_roll2 = randint(1,6)
            Craps_opponent1 = randint(1, 6)
            Craps_opponent2 = randint(1, 6)
            print(f"Your opponent guessed: {Craps_opponent1} for the first dice roll and {Craps_opponent2} for the 2nd one.")
            sleep(1)
            print("Time for the results...")
            sleep(1)
            print(f"FIRST ROLL:{Craps_roll1} SECOND ROLL: {Craps_roll2}.")
            sleep(0.5)
            print("Results from the first dice roll:")
            sleep(1)
            if Craps_opponent1 == Craps_roll1:
                print("OPPONENT WINS! +1 PT. FOR OPPONENT!")
                Craps_opp_points += 1
            elif Craps_choice1 == Craps_roll1:
                print("YOU WIN! +1 PT. FOR YOU!")
                Craps_points += 1
            else:
                 print("Draw!")
            print("Results from the second dice roll:")
            sleep(1)
            if Craps_opponent2 == Craps_roll2:
                print("OPPONENT WINS! +1 PT. FOR OPPONENT!")
                Craps_opp_points += 1
            elif Craps_choice2 == Craps_roll2:
                print("YOU WIN! +1 PT. FOR YOU!")
                Craps_points += 1
            else:
                 print("Draw!")
            sleep(0.5)
            if Craps_points > Craps_opp_points:
                 print("CONGRATS! YOU WIN! YOU WIN 1.7X YOUR BET!")
                 balance += Craps_bet * 1.7
            elif Craps_points < Craps_opp_points:
                 print("YOU LOST! YOU LOST ALL OF YOUR BET MONEY. BETTER LUCK NEXT TIME!")
            else:
                 print("DRAW! YOU BOTH LOST YOUR BET MONEY")
            sleep(1)
            headback()
    
    elif Main_room == 3:
        Slotmachine_bet = input("Make a Bet!")
        balance -= Slotmachine_bet
        Slotmachine_rolling1 = randint(1,7)
        Slotmachine_rolling2 = randint(1,7)
        Slotmachine_rolling3 = randint(1,7)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⠛⠛⠀⠀")
        print(f"⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿{Slotmachine_rolling1}⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⣷⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀")
        print("⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀")
        print("⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀")
        print("⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀")
        sleep(1)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⠛⠛⠀⠀")
        print(f"⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿{Slotmachine_rolling1}⡇⢸{Slotmachine_rolling2}⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⣷⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀")
        print("⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀")
        print("⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀")
        print("⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀")
        sleep(2)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⠛⠛⠀⠀")
        print(f"⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿{Slotmachine_rolling1}⡇⢸{Slotmachine_rolling2}⣿⡇⢸⣿{Slotmachine_rolling3}⡇⠀⣿⡇⠀⠀⣷⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀")
        print("⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀")
        print("⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀")
        print("⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀")
        sleep(2)
        if Slotmachine_rolling2 == Slotmachine_rolling1 == Slotmachine_rolling3:
             print(f"YOU WON!!!!! YOU MULTIPLIED YOUR MONEY BY {Slotmachine_rolling1}")
             balance = Slotmachine_bet * Slotmachine_rolling1
        elif Slotmachine_rolling2 == Slotmachine_rolling1 == Slotmachine_rolling3 == 1:
             print("You rolled three 1's you keep your money.")
        else:
             print("YOU LOSE! YOU LOST YOUR BET MONEY!")
        headback()
    elif Main_room == 4:
        if balance < 0:
            print(f"${balance}, you are in debt of the casino.")
            Main_room = 0
        else:
            print(f"${balance}")
            Main_room = 0
    elif Main_room == 5:
        Quit = True
    else:
        print("Enter a valid option.")

print("Thanks for visiting the Javaleti Casino! Come back later and win some more cash!")