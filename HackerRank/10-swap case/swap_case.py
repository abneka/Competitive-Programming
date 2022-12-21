def swap_case(s):
    toggle = ''
    
    for i in s:
        if i.isupper():
            toggle+= i.lower()
        else:
            toggle+= i.upper()
            
    return toggle
 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
