from game_of_greed.game_logic import GameLogic

class Game:
    def play(self, roller):
        print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')

        response = input('> ')

        if response == 'y':
            self.start_round()
        elif response == 'n':
            print('OK. Maybe another time')
            return


    def start_round(self):
        flag = True
        rounds = 0

        while flag:
            rounds += 1
            print(f'Starting round {rounds}')
            print('Rolling 6 dice...')
            print("*** " + "4 4 5 2 3 1 "+"***")
            print('Enter dice to keep, or (q)uit:')
            response = input('> ')
            if response == 'q':

                print('Thanks for playing. You earned 0 points')

            flag = False

