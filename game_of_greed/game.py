from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from tests.flo import _extract_rolls

class Game:
    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')

        response = input('> ')

        if response == 'y':
            self.start_round(roller)
        elif response == 'n':
            print('OK. Maybe another time')
            return


    def start_round(self, roller):
        flag = True
        round = 0
        number_of_dice = 6
        user_bank = Banker()

        while flag:
            round += 1
            print(f'Starting round {round}')
            print(f'Rolling {number_of_dice} dice...')
            dice_rolls = roller(number_of_dice)
            print(f"*** {str([die for die in dice_rolls]).replace(']', '').replace('[','').replace(',', '')} ***")
            print('Enter dice to keep, or (q)uit:')

            response = input('> ')

            if response == 'q':
                print(f'Thanks for playing. You earned {user_bank.balance} points')
                flag = False
            else:
                score = GameLogic.calculate_score([5])
                number_of_dice -= len(response)
                user_bank.shelf(score)
                print(f'You have {user_bank.shelved} unbanked points and {number_of_dice} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')
                # flag = False
            
            response = input('> ')
            
            if response == 'b':
                print(f'You banked {user_bank.bank()} points in round {round}')
                print(f'Total score is {user_bank.balance} points')
                number_of_dice = 6
            elif response == 'q':
                print(f'Thanks for playing. You earned {user_bank.balance} points')

                
