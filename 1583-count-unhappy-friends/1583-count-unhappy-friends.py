class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rating=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                rating[i][preferences[i][j]]=j+1
        
        def check(friend, pref):
            for friend1, friend2 in pairs:
                if friend != friend1 and rating[friend][friend1] < pref and rating[friend1][friend] < rating[friend1][friend2]:
                    return 1
                if friend != friend2 and rating[friend][friend2] < pref and rating[friend2][friend] < rating[friend2][friend1]:
                    return 1
            return 0
        
        ans = 0
        for friend1, friend2 in pairs:
            ans += check(friend1, rating[friend1][friend2])
            ans += check(friend2, rating[friend2][friend1])
        
        return ans