import random

class Stack:
    def __init__(self):
        self.items = []
    def push(self, e):
        self.items.append(e)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return True if len(self.items) < 1 else False
    def peek(self):
        return -1 if self.isEmpty() else self.items[0]
    def reverse(self):
        self.items.reverse()
    def __repr__(self):
        return str([str(item) for item  in self.items])
    def __eq__(self, other):
        return self.items == other.items
        
class Queue(Stack):
    def __init__(self):
        super().__init__()
    def enqueue(self, e):
        super().push(e)
    def dequeue(self):
        self.items.pop(random.randint(0, len(self.items)-1))
    
def isPalindrome(str):
    stack = Stack()
    queue = Queue()
    for letters in str:
        stack.push(letters)
        queue.push(letters)
    stack.reverse()
    return True if (stack == queue) else False
    
print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))