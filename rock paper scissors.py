import random
print('''hello lets play rock, paper,scissors. This game has 3 key outcomes
- Rock Beats Scissors
- Paper Beats Rock
- Scissors Beats Paper''')
player_name = input("what is your name")
print("Welcome", str(player_name.strip()), "lets begin")
attempts = 0
wins = 0
losses = 0
choices = ["rock", "paper", "scissors"]
while True:
    player_choice = input("what do you play rock, paper, or scissors. You may also say 'quit' to abort")
    if player_choice.strip().lower() == "quit":
      print("you have quit successfully. Thank You For Playing Kemji's Rock Paper Scissors")
      break
    bot_choice = random.choice(choices)
    attempts += 1
    if player_choice.strip() == bot_choice.strip():
      print(f"I played {bot_choice}, its a draw you have played {attempts} times, {wins} wins, {losses} losses")   
    if(player_choice.strip() == "rock" and bot_choice == "scissors") or\
      (player_choice.strip() == "paper" and bot_choice == "rock") or\
      (player_choice.strip() == "scissors" and bot_choice == "paper"):
      wins += 1 
      print(f"I played {bot_choice} you won, you have played {attempts} times and have won {wins} times and have lossed {losses} times")
    if(player_choice.strip() == "rock" and bot_choice == "paper") or\
      (player_choice.strip() == "paper" and bot_choice == "scissors") or\
      (player_choice.strip() == "scissors" and bot_choice == "rock"):
      losses += 1
      print(f"I played {bot_choice} I won you have played {attempts} times, won {wins} times and lost {losses} times")
    elif player_choice.strip().lower not in choices:
        print("invalid, please try again")
       
    
