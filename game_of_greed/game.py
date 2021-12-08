from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from tests.flo import _extract_rolls

class Game:
    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')

        response = input('> ')

        if response == 'y':
            self.start_game(roller)
        elif response == 'n':
            print('OK. Maybe another time')
            return

    def quit_game(self, user):
        print(f'Thanks for playing. You earned {user.balance} points')

    def start_game(self, roller):
        flag = True
        round = 1
        number_of_dice = 6
        user_bank = Banker()
        print(f'Starting round {round}')

        while flag:

            print(f'Rolling {number_of_dice} dice...')
            dice_rolls = roller(number_of_dice)
            str_rolls = [str(die) for die in dice_rolls]
            print("*** " + " ".join(str_rolls) + " ***")
            print('Enter dice to keep, or (q)uit:')

            response = input('> ')

            if response == 'q':
                self.quit_game(user_bank)
                flag = False
            else:
                score = GameLogic.calculate_score([int(num) for num in response])
                number_of_dice -= len([int(num) for num in response])
                user_bank.shelf(score)
                print(f'You have {user_bank.shelved} unbanked points and {number_of_dice} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')

            
            response = input('> ')
            
            if response == 'b':
                print(f'You banked {user_bank.bank()} points in round {round}')
                print(f'Total score is {user_bank.balance} points')
                number_of_dice = 6
                round += 1
                print(f'Starting round {round}')
            elif response == 'q':
                self.quit_game(user_bank)
                flag = False

            
if __name__ == "__main__":
    #Game.play()
    game = Game()
    game.play()