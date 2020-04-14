from stack_new import Stack

def intToB(n):
    s = Stack()
    while n > 0:
        remainder = n%2
        s.push(remainder)
        n = int(n/2)
    res = ''
    while not s.is_empty():
        res += str(s.pop())       
    return res

print(intToB(242))
        
    
