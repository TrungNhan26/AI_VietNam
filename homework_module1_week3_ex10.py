class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            print("Stack is full! Cannot push the value.")
        else:
            self.__stack.append(value)
            print(f"Pushed {value} to stack.")

    def top(self):
        if self.is_full():
            print("Stack is empty! No top element.")
            return None  # Hoặc có thể trả về một giá trị đặc biệt để biểu thị ngăn xếp trống
        else:
            return self.__stack[-1]
        
stack1 = MyStack ( capacity =5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print (stack1.top())
