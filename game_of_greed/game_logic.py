import random 

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1,6) for _ in range (0, num_dice))