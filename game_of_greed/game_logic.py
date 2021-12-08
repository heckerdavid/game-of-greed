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




