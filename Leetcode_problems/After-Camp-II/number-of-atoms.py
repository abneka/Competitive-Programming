class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        ans = []
        start = 0
        while start < len(formula):
            # check if it upper
            if formula[start].isupper():
                end = start + 1
                count = ''
                #find substr
                while end < len(formula) and formula[end].islower():
                    end += 1
                name = formula[start:end]

                #find count
                if end == len(formula) or not formula[end].isdigit():
                    count = '1'
                while end < len(formula) and formula[end].isdigit():
                    count += formula[end]
                    end += 1
                
                #add to stack
                stack.append((name, int(count)))
                start = end
            
            # check if parenthesis
            elif formula[start] == '(':
                stack.append(('', 0))
                start += 1
            
            #check if parenthesis
            else:
                end = start + 1
                count = ''
                # find count
                if end == len(formula) or not formula[end].isdigit():
                    count = '1'
                while end < len(formula) and formula[end].isdigit():
                    count += formula[end]
                    end += 1
                
                # multiply families
                temp = []
                while stack[-1][1]:
                    name, val = stack.pop()
                    temp.append((name, val * int(count)))
                stack.pop()
                stack.extend(temp)
                start = end
        # sort according to name
        stack.sort()

        
        for name, count in stack:
            # merge similar names
            if ans and ans[-1] == name:
                ans.append(str(count + 1))
            elif len(ans) > 1 and ans[-2] == name:
                count += int(ans.pop())
                ans.append(str(count))
            #skip if count = 1
            elif count  == 1:
                ans.append(name)
            else:
                ans.append(name)
                ans.append(str(count))
        return ''.join(ans)