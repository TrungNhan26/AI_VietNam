class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        if len(self.__queue) == self.__capacity:
            return True
        else:
            return False

    def is_empty(self):
        return len(self.__queue) == 0

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full! Cannot enqueue the value.")
        else:
            self.__queue.append(value)
            print(f"Enqueued {value} to queue.")
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue the value.")
            return None
        else:
            return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        else:
            return self.__queue[0]


# Khởi tạo đối tượng MyQueue với dung lượng 5
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())