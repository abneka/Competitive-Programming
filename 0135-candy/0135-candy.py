class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 1
        length = len(ratings)
        left = 0
        right = 0
        prev = 1
        temp = 0
        for index in range(1, length):
            if ratings[index] < ratings[index - 1]:
                if right > left:
                    left += 1
                    temp += 1
                    ans += temp
                    continue
                temp = 0 
                left += 1
                right = 0
            
            elif ratings[index] == ratings[index - 1]:
                left = 0
                right = 0
            else:
                if temp:
                    temp = 0
                    right = 0
                left = 0
                right += 1
            
            ans += left + 1 + right
        return ans