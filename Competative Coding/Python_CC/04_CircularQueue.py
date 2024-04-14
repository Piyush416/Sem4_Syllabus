# Implementation of circular Queue
class MyCircular:
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.front = self.rear = -1
    
    def enqueue(self,data):
        if ((self.rear+1)%self.k) == self.front:
            print("Queue is Full")
        
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.k
            self.queue[self.rear] = data
        
    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.rear = self.front = -1
            return temp
    
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1)%self.k
            return temp
        
    def display(self):
        if (self.front == -1):
            print("Queue is Empty")
        
        elif (self.rear >= self.front):
            print("Elements in the circular queue are: ",end = " ")

            for i in range(self.front , self.rear+1):
                print(self.queue[i],end=" ")
                
        else:
            print("Elements in the circular queue are: ", end = " ")

            for i in range(self.front,self.k):
                print(self.queue[i],end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i],end=" ")
            print ()
        
        

ob = MyCircular(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("Deleted value = ",ob.dequeue())
print("Deleted value = ",ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
