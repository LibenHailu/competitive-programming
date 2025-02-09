# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10**4
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) == 2 ** 31 - 1 or reader.get(mid) > target:
                right = right -1
            else:
                left = left + 1
        return -1