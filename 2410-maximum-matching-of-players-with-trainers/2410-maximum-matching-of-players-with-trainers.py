class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        player = 0
        trainer = 0
        
        players.sort()
        trainers.sort()
        
        players_length = len(players)
        trainers_length = len(trainers)
        
        result = 0
        
        while player < players_length and trainer < trainers_length:
            
            if players[player] > trainers[trainer]:
                trainer += 1
                
            else:
                result += 1
                player += 1
                trainer += 1
                
        return result