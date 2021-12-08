import random
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        score = 0
        tally = Counter(dice)

        #check for straight; one of each dice
        if len(tally) == 6:
            return 1500

        #calculate score for 3 pairs
        filtered_tally = list(filter(lambda n : n == 2, tally.values()))
        # print("filter:", filtered_tally)
        if len(filtered_tally) == 3:
            return 1500
            
        #calculate 3 of a kind and up
        for dice_value in tally:
            if tally[dice_value] > 2:
                if dice_value == 1:
                    score += (tally[dice_value] - 2) * dice_value * 1000
                else: 
                    score += (tally[dice_value] - 2) * dice_value * 100

        #calculate individual 1's and 5's
        if tally[5] < 3:
            score += (tally[5] * 50)
        if tally[1] < 3:
            score += (tally[1] * 100)

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1,6) for _ in range (0, num_dice))

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_as_list = [x for x in roll]
        for die in keepers:
            try:
                roll_as_list.remove(die)
            except:
                return False
        return True


    @staticmethod
    def get_scorers(dice_set):
        dice_count = Counter(dice_set)
        scorers = []
        for dice_value in dice_count:
            if dice_value == 1 or dice_value == 5:
                for _ in range(dice_count[dice_value]):
                    scorers.append(dice_value)
            else:
                if dice_count[dice_value] > 2:
                    for _ in range(dice_count[dice_value]):
                        scorers.append(dice_value)
        
        return tuple(scorers)

