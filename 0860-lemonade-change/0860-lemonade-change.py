class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            
            elif bill == 10:
                if fives:
                    tens += 1
                    fives -= 1
                else:
                    return False
            
            else:
                if fives and tens:
                    tens -= 1
                    fives -= 1
                elif fives:
                    if fives >= 3:
                        fives -= 3
                    else:
                        return False
                else:
                    return False
        return True