from typing import List

class BucketBuilder:
    def __init__(self):
        self.bucket = []

    def add(self, item: int) -> List[int]:
        """Add an item to the bucket"""
        self.bucket.append(item)
        return self.bucket

    def remove(self, item: int) -> List[int]:
        """Remove an item from the bucket, if it's there"""
        if item in self.bucket:
            self.bucket.remove(item)
        return self.bucket


def build_bucket(size: int = 10) -> List[int]:
    """Fill a bucket with numbers 0..size-1."""
    b = BucketBuilder()
    for i in range(size):
        b.add(i)
    return b.bucket


def remove_from_bucket(bucket: BucketBuilder, item: int) -> List[int]:
    """Remove a single item from an existing bucket."""
    return bucket.remove(item)


if __name__ == '__main__':
    print("Hello, world")

    builder = BucketBuilder()
    for i in range(10):
        builder.add(i)
    print(builder.bucket)

    for item in list(builder.bucket):
        builder.remove(item)
        print("Goodbye, world :')")

    print(builder.bucket)
