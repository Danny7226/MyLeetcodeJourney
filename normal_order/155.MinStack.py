'''

155. Min Stack

Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         Min = float('inf')
#         for i in self.stack:
#             if i < Min:
#                 Min = i
#         return Min

class MinStack:
    # getMin in constant runtime
    # Using a tuple to store the min element of the list behind

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

class MinStack:
    # fastest

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.Min or self.Min[-1] >= x:
            self.Min.append(x)
    def pop(self) -> None:
        if self.stack:
            tmp = self.stack.pop()
            if tmp == self.Min[-1]:
                self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()