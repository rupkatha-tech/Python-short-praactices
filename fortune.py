import random #import random module
import time   #import time module

print("\n" + "'Welcome to the Magic 8 Ball!'".center(90) + "\n") #welcome message centered
print("\n" + "------------------------------".center(90) + "\n") #separator line
print("The Magic 8 Ball takes only 'Yes' or 'No' questions.") #instructions
print("You can ask the Magic 8 Ball up to 10 questions, then you have to restart.") #instructions
while True: #loop to ask or quit
    choice = input("Do you want to:\n1. Ask\n2. Quit\nEnter 1 or 2: ") #user input to ask or quit
    if choice == "2": #if user chooses to quit
        print("Have a nice day. Goodbye!") #goodbye message
        break
    elif choice == "1": #if user chooses to ask
        question_count = 0 #initialize question counter
        while True: #loop to keep asking questions
            if question_count >= 10:
                print("\nYou have reached the question limit (10). Please restart the game to ask more questions.\n") #limit message
                break
            question = input(f"Ask the Magic 8 Ball a question ({question_count + 1}/10): ") #takes user input
            answer = random.randint(0, 9) #random number between 0 and 9
            print("Thinking...") #thinking message
            time.sleep(1) #pause for 1 second
            if answer == 0: 
                print("Yes - definitely.") 
            elif answer == 1:
                print("It is decidedly so.") 
            elif answer == 2:
                print("Without a doubt.")
            elif answer == 3:
                print("Reply hazy, try again.")
            elif answer == 4:
                print("Ask again later.")
            elif answer == 5:
                print("Better not tell you now.")
            elif answer == 6:
                print("My sources say no.")
            elif answer == 7:
                print("Outlook not so good.")
            elif answer == 8:
                print("Very doubtful.")
            else:
                print("No- not at all.")
            question_count += 1 #increment question counter
            # Show warning only when 3 or fewer questions left
            if question_count >= 7 and question_count < 10:
                print(f"Reminder: You have asked {question_count} questions, only {10 - question_count} more left!") #reminder message when 3 or fewer questions left
            if question_count < 10: 
                another = input("Want to ask another question? (Y/N)") #user input to ask again or return to main menu
                if another.lower() in ["no","n"]: #if user chooses no or n
                    print("Returning to main menu...") #returning message
                    time.sleep(1) #pause for 1 second
                    break
                elif another.lower() not in ["yes","y"]: #if user wants to ask again, accepts yes or y (case-insensitive)
                    break
        
    else:
        print("Invalid input. Please enter 1 to 'Ask' or 2 to 'Quit'.") #if user inputs anything other than 1 or 2