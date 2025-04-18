# queue_manager.py
from collections import deque

# Dictionary to track inactivity tasks per guild
inactivity_tasks = {}

def get_inactivity_queue():
    return inactivity_tasks

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add(self, song):
        self.queue.append(song)

    def next(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

song_queue = QueueManager()