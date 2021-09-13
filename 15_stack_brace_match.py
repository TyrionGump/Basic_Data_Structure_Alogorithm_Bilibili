class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()
    
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for ch in s:
        if ch in ['(', '[', '{']:
            stack.push(ch)
        else:
            if stack.is_empty():  # 说明右括号没有和它匹配的左括号
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                 return False
    
    if stack.is_empty():
        return True
    else:
        return False

[print(brace_match('{}({)'))]
            

