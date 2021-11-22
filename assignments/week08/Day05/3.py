class MyQueue:

    def __init__(self):
        
        self.myque = list()
        print(self.myque)
        

    def push(self, x: int) -> None:
        
        self.myque.append(x)
        print(self.myque,self.myque)
        
        

    def pop(self) -> int:
        
        return  self.myque.pop(0)
  
        

    def peek(self) -> int:
        
        
        return self.myque[0]
    
        

    def empty(self) -> bool:
        
        return len(self.myque) == 0
        
    
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()