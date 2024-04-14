# Write a program for implementing a MINSTACK which should support operations like push,
# pop, overflow, underflow, display
# a. Construct a stack of N-capacity
# b. Push elements
# c. Pop elements
# d. Top element
# e. Retrieve the min element from the stack

class MinStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.minstack = []
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def push(self,item):
        if self.is_full():
            print("Stack is OverFlow")
        else:
            self.stack.append(item)
            if len(self.minstack) == 0 or self.minstack[-1]>=item:
                self.minstack.append(item)  

    def pop(self):
        if self.is_empty():
            print("Stack is UnderFlow")
        else:
            if self.minstack[-1] == self.stack[-1]:
                self.minstack.pop()
            return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            print("No top element")
        else:
            return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("No element present")
        else:
            print(self.stack)
            print(self.minstack)
    
    def get_min(self):
        if len(self.minstack) == 0:
            print("no min element")
        else:
            return self.minstack[-1]

a = MinStack(10)
a.push(1)
a.push(2)
a.push(2)
a.push(3)
a.push(1)

a.display()
print("Pop element is : ",a.pop())
a.display()
print("Pop element is : ",a.pop())
print("TOP element is : ",a.top())
print("Pop element is : ",a.pop())
a.display()
print("min element is : ",a.get_min())



    
