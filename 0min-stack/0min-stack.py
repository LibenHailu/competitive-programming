class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
            return
        cur = []
        while self.minStack and val > self.minStack[-1]:
            cur.append(self.minStack.pop())
            # if not self.minStack:
            #     self.minStack.append(val)
        self.minStack.append(val)
        for num in reversed(cur):
            self.minStack.append(num)
            

    def pop(self) -> None:
        val = self.stack.pop()
        cur = []
        while self.minStack and self.minStack[-1] != val:
            cur.append(self.minStack.pop())
        self.minStack.pop()
        for num in reversed(cur):
            self.minStack.append(num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()