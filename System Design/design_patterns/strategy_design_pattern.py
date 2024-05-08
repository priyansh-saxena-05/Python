"""
The Strategy Design Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one of them, and make them interchangeable. This pattern lets the algorithm vary independently from clients that use it.
Here's how you can implement the Strategy Design Pattern in Python:

Define the Strategy Interface: Define an interface (or base class) that declares a method for the algorithm.
Implement Concrete Strategies: Implement concrete classes that conform to the strategy interface. Each class represents a specific algorithm.
Use Context Class: Create a context class that maintains a reference to a strategy object and provides a method for clients to execute the algorithm.
Let's see an example of how to implement the Strategy Design Pattern in Python. Suppose we have a context class representing a sorting algorithm, and we want to implement different sorting strategies (e.g., bubble sort, quicksort, mergesort).
"""

from abc import ABC, abstractmethod
from typing import List

# Step 1: Define the Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

# Step 2: Implement Concrete Strategies
class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        sorted_data = data.copy()
        n = len(sorted_data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_data[j] > sorted_data[j + 1]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        return sorted_data

class QuickSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return QuickSortStrategy().sort(left) + middle + QuickSortStrategy().sort(right)

# Step 3: Use Context Class
class SortingAlgorithm:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def execute_sort(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)

# Example usage:
data = [3, 1, 4, 1, 5, 9, 2, 6]
sorting_algorithm = SortingAlgorithm(BubbleSortStrategy())
sorted_data = sorting_algorithm.execute_sort(data)
print("Sorted using Bubble Sort:", sorted_data)

sorting_algorithm.set_strategy(QuickSortStrategy())
sorted_data = sorting_algorithm.execute_sort(data)
print("Sorted using Quick Sort:", sorted_data)
