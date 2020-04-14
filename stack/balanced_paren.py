from stack import Stack

def match(p, q):
    if p == '(' and q==')':
        return True
    if p=='{' and q=='}':
        return True
    if p=='[' and q==']':
        return True
    return False

def paren(st):
    s = Stack()
    for i in st:
        if i in '[{(':
            s.push(i)
        if i in ']})':
            popped = s.pop()
            if match(i, popped):
                continue
            else:
                return "Not Balanced"
    return "Balanced"


print(paren('{{[]}'))
            
    
