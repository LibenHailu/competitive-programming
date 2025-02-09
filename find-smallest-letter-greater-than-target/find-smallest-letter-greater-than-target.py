class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        best = 0
        left,right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return letters[best]