class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        current_min= min(value, self.minstack[-1] if self.minstack else value)
        self.minstack.append(current_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]