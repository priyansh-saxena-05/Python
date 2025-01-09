import time

class RateLimiter:

    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = capacity
        self.last_login = time.time()

    def add_tokens(self):
        now = time.time()
        current_window = now - self.last_login
        self.last_login = now
        current_tokens = current_window * self.rate
        self.tokens = min(self.capacity, self.tokens + current_tokens)

    def allow_request(self):
        self.add_tokens()
        if self.tokens >= 1:
            self.tokens -=1
            return True
        return False


limiter = RateLimiter(capacity=3, rate=2)

for i in range(20):
    if i == 8:
        time.sleep(1)
    if i==18:
        time.sleep(4)
    print(limiter.allow_request())
