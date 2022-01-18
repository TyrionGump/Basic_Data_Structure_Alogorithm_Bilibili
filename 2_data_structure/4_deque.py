"""
双向队列的两端都支持进队和出队操作.
如果只想要一个队列容器，用deque；如果想线程间同步，生产者消费者什么的，用Queue.
"""

from collections import deque

q = deque()
q.append(1)  # 队尾进队
q.popleft()  # 队首出队
q.appendleft(1)  # 队首进队
q.pop()  # 队尾出队