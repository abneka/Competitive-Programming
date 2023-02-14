class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        pointerA, pointerB = len(a)-1, len(b)-1
        
        while pointerA >= 0 or pointerB >= 0 or carry:
            total = carry
            
            if pointerA >= 0:
                total += int(a[pointerA])
                pointerA -= 1
            
            if pointerB >= 0:
                total += int(b[pointerB])
                pointerB -= 1
            
            result.append(str(total % 2))
            
            carry = total // 2
            
        return ''.join(reversed(result))