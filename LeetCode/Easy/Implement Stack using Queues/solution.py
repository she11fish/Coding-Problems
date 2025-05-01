class MyStack:

    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)
        while self.stack:
            self.queue.insert(0, self.stack.pop())
        while self.queue:
            self.stack.insert(0, self.queue.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
