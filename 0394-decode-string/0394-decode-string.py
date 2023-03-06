class Solution:
    def decodeString(self, s: str) -> str:
        
        def decoder(string,start):
            output = []
            i = start
            k = ''
            while i < len(string):
                if string[i] == ']':
                    return (''.join(output),i)
                else:
                    if string[i].isdigit():
                        k += string[i]
                        i += 1
                    elif string[i] == '[':
                        letters, index = decoder(string,i+1)
                        output.append(letters*int(k))
                        k = ''
                        i = index+1
                    else:
                        output.append(string[i])
                        i += 1
                
            return (''.join(output),i)
        string , idx = decoder(s,0)
        return string