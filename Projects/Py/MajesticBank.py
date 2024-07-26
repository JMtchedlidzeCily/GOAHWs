# Pin input
pin = input("To proceed, you're going to need to make a 4-character pin for your bank account: ")

# Pin checking
while len(pin) != 4:
    print("Pin creation unsuccessful. Please make sure it has 4 characters.")
    pin = input("Create a new one, make sure it has 4 characters: ")

print("Pin creation successful.")

# Declaring the balance variable
balance = 0

# Declaring the Quit variable which will act as a killswitch
Quit = False

# Making the bank functionality
while not Quit:
    main_menu = input("Main menu: 1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Quit | Please select an option: ")

    if main_menu == '1':
        print(f"You have ${balance}.")
    
    elif main_menu == '2':
        entered_pin = input("Please enter your pin: ")
        if entered_pin == pin:
            amount = input("How much money do you want to deposit into your bank account? ")
            balance += int(amount)
            print(f"${amount} has been deposited into your account.")
        else:
            print("Incorrect pin. Deposit unsuccessful.")
    
    elif main_menu == '3':
        entered_pin = input("Please enter your pin: ")
        if entered_pin == pin:
            wamount = input("How much do you wish to withdraw from your bank account? ")
            if balance - int(wamount) >= 0:
                balance -= int(wamount)
                print(f"${wamount} has been withdrawn from your account.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect pin. Withdrawal unsuccessful.")
    
    elif main_menu == '4':
        Quit = True
        print("Thank you for using the Majestic banking system. Goodbye!")
    
    else:
        print("Invalid option. Please select a valid option from the menu.")