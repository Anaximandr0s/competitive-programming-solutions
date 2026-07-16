class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            current_min= min(value, self.minstack[-1])
            self.minstack.append(current_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() if self.minstack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None