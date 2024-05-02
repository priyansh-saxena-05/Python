"""
In this code, DynamicArray is a class that represents a dynamic array. It has an array self.array to store the elements, a self.capacity to store the capacity of the array, and a self.size to store the number of elements in the array.
The get method returns the element at a given index. The set method sets the element at a given index to a given value. The pushback method adds an element to the end of the array, resizing the array if necessary. The popback method removes and returns the last element of the array.
The resize method doubles the capacity of the array and copies the elements from the old array to the new array. The getSize method returns the number of elements in the array. The getCapacity method returns the capacity of the array.
"""
class DynamicArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i):
        return self.array[i]

    def set(self, i, n):
        self.array[i] = n

    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self):
        self.size -= 1
        return self.array[self.size]

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity
