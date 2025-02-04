class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        ans = []
        for num in nums2:
            if num in count:
                ans.append(num)
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        return ans