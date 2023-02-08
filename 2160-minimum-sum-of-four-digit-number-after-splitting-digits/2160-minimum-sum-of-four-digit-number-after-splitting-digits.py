class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        num = sorted(list(num))
        num = str(num)
        
        list1 = list()
        list1.append((num[2]+num[17]))
        list1.append((num[7]+num[12]))
        return (int(list1[0])+int(list1[1]))