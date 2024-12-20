# untuk oop

# def stack():
#     return []
# def push(s, data):
#     return s.append(data)
# def pop(s):
#     return s.pop()
# def peek(s):
#     return s[-1]
# def size(s):
#     return len(s)
# def isEmpty(s):
#     return len(s)==0

# jika dengan class

class Stack:
    def __init__(self):
        self.items=[]
        # return self.items
    # for printing the stack content
    def __str__(self):
        return " ".join([str(i) for i in self.items])
    
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
