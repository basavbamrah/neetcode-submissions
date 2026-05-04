class MinStack:

    def __init__(self):
        self.stack=list()


    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) <1:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) <1:
            return None
        return min(self.stack)
        
