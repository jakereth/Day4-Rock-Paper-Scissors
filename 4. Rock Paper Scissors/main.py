import random

player1 = int(input("What do you choose?\n'0 for rock\n1 for paper\n2 for scissors"))
gameStatus = ''

bot = random.randint(0,2)


def rock(bot):
    if bot == 0:
        return 'tie'
    if bot == 1:
        return 'lose'
    if bot == 2:
        return 'win'

def paper(bot):
    if bot == 0:
        return 'win'
    if bot == 1:
        return 'tie'
    if bot == 2:
        return 'lose'

def scissors(bot):
    if bot == 0:
        return 'lose'
    if bot == 1:
        return 'win'
    if bot == 2:
        return 'tie'

match player1:
    case 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        gameStatus = rock(bot)
    
    case 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        gameStatus = paper(bot)

    case 2:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        gameStatus = scissors(bot)

choices = ['rock', 'paper', 'scissors']
botChoice = choices[bot]

if gameStatus == 'win':
    print("Congratulations you won!")
    print(f"The bot chose {botChoice}")
elif gameStatus == 'tie':
    print("Looks like you tied")
    print(f"The bot chose {botChoice}")
else:
    print("You lose this time!")
    print(f"The bot chose {botChoice}")