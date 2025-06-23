#rock, paper, scissor

import random

print("Welcome to Rock 🪨, Paper 📃, Scissor ✂️!")

options1 = ["rock", "paper", "scissor"] 
options2 = ["r", "p", "s"]
options3 = ["rock 🪨", "paper 📃", "scissor ✂️"]


while True:
    rounds = input("if you want to play a match ▶️  enter 'match' or if you want to play in infinite mode ♾️  enter 'infinite': ").lower()
    if rounds == 'infinite':
        print ("\nlet's begin infinite ♾️  mode\n")
        while True:
            user = input("Choose rock🪨  (r), paper📃 (p), scissor✂️  (s)\nor 'quit😞 (q)' to stop\n\nYOUR CHOICE: ").lower() 
            if user == "quit" or user == "q":
                print("\nThanks for playing!")
                print("-" * 100)
                print("\n")
                break

            if user not in options1 and user not in options2 and user not in options3:
                print("\nInvalid choice. Try again.")
                continue

            computer = random.choice(options3)
            print("\nCOMPUTER'S CHOICE: ", computer)

            if  (user == computer) or\
                (user == "r" and computer == "rock 🪨") or \
                (user == "s" and computer == "scissor ✂️") or \
                (user == "p" and computer == "paper 📃"):
                print("\nIT'S A TIE! 🤝  " )

            elif(user == "rock" and computer == "scissor ✂️") or \
                (user == "r" and computer == "scissor ✂️") or \
                (user == "scissor" and computer == "paper 📃") or \
                (user == "s" and computer == "paper 📃") or \
                (user == "paper" and computer == "rock 🪨") or \
                (user == "p" and computer == "rock 🪨"):
                print("\nYOU WIN! 🎉  ")

            else:
                print("\nCOMPUTER WINS! 💻")

            print("-" * 100)
            print("\n" * 2)

    elif rounds != 'match' and rounds != 'infinite':
        print ("invlid response, try again 🙂")
        continue

    elif rounds == 'match':
        print ("\nlet's begin the match ▶️")
        try:
            total_rounds = int(input("\nenter the number of rounds you want to play 💭 : ")) 
            if total_rounds <= 0:
                print("\nPlease enter a number greater than 0️⃣.")
            else:
                break
        except ValueError:
            print("\nPlease enter a valid number. 🙂")

user_score = 0
computer_score = 0
rounds_played = 0

while rounds_played < total_rounds:
    print("\nROUND", rounds_played + 1)
    user = input("\nChoose rock🪨  (r), paper📃 (p), scissor✂️  (s)\nor 'quit😞 (q)' to stop\n\nYOUR CHOICE: ").lower()

    if user == "quit" or user == "q":
        print("\nThanks for playing!")
        print("goodbye 👋")
        print("-" * 30)
        break

    if user not in options1 and user not in options2:
        print("Invalid choice. Try again. 🙂")
        print("-" * 30)
        continue

    computer = random.choice(options3)
    print("COMPUTER'S CHOICE: ", computer) 

    if  (user == computer) or \
        (user == "r" and computer == "rock 🪨") or \
        (user == "s" and computer == "scissor ✂️") or \
        (user == "p" and computer == "paper 📃"):
        print("\nIT'S A TIE! 🤝  " )

    elif(user == "rock" and computer == "scissor ✂️") or \
        (user == "r" and computer == "scissor ✂️") or \
        (user == "scissor" and computer == "paper 📃") or \
        (user == "s" and computer == "paper 📃") or \
        (user == "paper" and computer == "rock 🪨") or \
        (user == "p" and computer == "rock 🪨"):
        print("\nYOU WIN! 🎉  ")
        user_score += 1

    else:
        print("\nCOMPUTER WINS! 💻")
        computer_score += 1

    print("-" * 30)
    rounds_played += 1

if rounds_played == total_rounds:
    print("\nFinal Result 🎯")

    if user_score > computer_score:
        print("You: 😱", user_score)
        print("Computer: 🥲", computer_score) 
        print("🎉 You won the game!")

    elif user_score < computer_score:
        print("You: 🥲", user_score)
        print("Computer: 😱", computer_score)
        print("💻 Computer won the game!")
    else:
        print("You: ", user_score)
        print("Computer: ", computer_score)
        print("🤝 It's a tie!")
    print("-" * 100)
