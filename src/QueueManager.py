# queue_manager.py
from collections import deque

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add(self, song):
        self.queue.append(song)

    def next(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0
