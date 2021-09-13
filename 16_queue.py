class Queue:
    """
    这里我们创建一个长度固定的环形 queue.
    """
    def __init__(self, size=100) -> None:
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针
    
    def push(self, element):
        """
        把新进来的值放到队尾指针的位置
        """
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is full!")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty!")
    
    def is_empty(self):
        return self.rear == self.front
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
# 长度为 5 的队列只能存 4 个数字
for i in range(4):
    q.push(i)
print(q.pop())


