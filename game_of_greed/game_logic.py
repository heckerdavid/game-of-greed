from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        score = 0
        tally = Counter(dice)
        print(tally)
        if tally[5] < 3 or tally[1] < 3:
            score += (tally[5] * 50) + (tally[1] * 100)
        
        return score