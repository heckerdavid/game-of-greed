from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from tests.flo import _extract_rolls

class Game:

    def __init__(self, num_rounds=1) -> None:
        self.number_of_dice = 6
        self.round = 1
        self.flag = True
        self.roller = None
        self.current_dice_roll = None
        self.num_rounds = num_rounds

    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller
        print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')

        response = input('> ')

        if response == 'y':
            self.start_game()
        elif response == 'n':
            print('OK. Maybe another time')
            return

    def quit_game(self, user):
        print(f'Thanks for playing. You earned {user.balance} points')
        self.flag = False
    
    def roll_users_dice(self):
        print(f'Rolling {self.number_of_dice} dice...')
        self.current_dice_roll = self.roller(self.number_of_dice)
        self.show_roll()
    
    def show_roll(self):
        str_rolls = [str(die) for die in self.current_dice_roll]
        print("*** " + " ".join(str_rolls) + " ***")
        if not self.check_zilch():
            print('Enter dice to keep, or (q)uit:')
        
    def check_zilch(self):
        if len(GameLogic.get_scorers(self.current_dice_roll)) == 0:
            self.zilch()
            return True
            
        return False
    
    def zilch(self):
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {self.round}')
        print(f'Total score is {self.user_bank.balance} points')
        self.round += 1
        print(f'Starting round {self.round}')
        self.number_of_dice = 6
        self.roll_users_dice()



    def start_game(self):
        self.user_bank = Banker()
        print(f'Starting round {self.round}')
        self.roll_users_dice()

        while self.flag:
            if self.num_rounds > self.round:
                self.quit_game(self.user_bank)

            response = input('> ')

            if response == 'q':
                self.quit_game(self.user_bank)
            elif response == 'b':
                print(f'You banked {self.user_bank.bank()} points in round {self.round}')
                print(f'Total score is {self.user_bank.balance} points')
                self.number_of_dice = 6
                self.round += 1
                if self.round > self.num_rounds:
                    self.quit_game(self.user_bank)
                    continue
                print(f'Starting round {self.round}')
                self.roll_users_dice()
                continue
            elif response == 'r':
                self.roll_users_dice()
                if self.check_zilch():
                    print(f'Starting round {self.round}')
                    continue
            else: # elif regex filter to ensure numbers?? (other else to continue with "junk" input)
                filtered_response = response.replace(' ', '')
                user_dice_to_keep = [int(num) for num in filtered_response]
                if GameLogic.validate_keepers(self.current_dice_roll, user_dice_to_keep):
                    score = GameLogic.calculate_score(user_dice_to_keep)
                    self.number_of_dice -= len(user_dice_to_keep)
                    self.user_bank.shelf(score)
                    print(f'You have {self.user_bank.shelved} unbanked points and {self.number_of_dice} dice remaining')
                    if self.number_of_dice == 0:
                        self.number_of_dice = 6
                    print('(r)oll again, (b)ank your points or (q)uit:')
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    self.show_roll()
                    continue


if __name__ == "__main__":
    #Game.play()
    game = Game()
    game.play()