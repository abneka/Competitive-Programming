class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)
        ans = []
        
        left = 0
        right = sum(i for i in range(length) if boxes[i]=='1')
        
        one_left = 0
        one_right = boxes.count('1')
        
        for i in range(length):
            ans.append(left+right)
            
            if boxes[i]=='1':
                one_left = one_left+1
                one_right = one_right-1
                
            left = left+one_left
            right = right-one_right
            
        return ans