import heapq
from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = defaultdict(int)
        self.heap = []

    def get(self, key):
        if key in self.cache:
            # Update the frequency and heap when accessing a key
            self.frequency[key] += 1
            heapq.heappush(self.heap, (self.frequency[key], key))
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if len(self.cache) >= self.capacity:
            # Evict the least frequently used item
            while self.heap:
                freq, k = heapq.heappop(self.heap)
                if self.frequency[k] == freq:
                    del self.cache[k]
                    break

        # Add the new key-value pair
        self.cache[key] = value
        self.frequency[key] += 1
        heapq.heappush(self.heap, (self.frequency[key], key))
