class MyQueue:

    def __init__(self):
        #remember stacks are lifo by default
        #create 2 stacks here
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        #while there are values present in the first stack
        while self.stack1:
            #pop values off stack1 and append them to stack2
            self.stack2.append(self.stack1.pop())
            
        #when stack1 is empty, we can add x to it
        self.stack1.append(x)
        
        #while there are values present in stack2
        while self.stack2:
            #do the same thing the other way
            #append the popped values back onto stack1
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        #we've already done the shuffle, so now we can just straight pop
        return self.stack1.pop()
        

    def peek(self) -> int:
        #classic index to return last element (element at front of queue)
        return self.stack1[-1]
        

    def empty(self) -> bool:
        #return true if queue is empty
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


