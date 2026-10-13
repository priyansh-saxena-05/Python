from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):

            # 1. Remove indices outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller values from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Record maximum when window is complete
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans