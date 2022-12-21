class Solution:
    def interpret(self, command: str) -> str:
        command = [i for i in command]
        print(command)
        
        string = ''
        
        while command:
            temp = command.pop()
            print(temp)
            if temp.isupper():
                string = temp + string
                continue
            
            temp = command.pop()
            if temp.islower():
                command.pop()
                command.pop()
                string = 'al' + string
                
            else:
                string = 'o' + string
                
        
        return string
            