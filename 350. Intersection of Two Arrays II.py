class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) > len(nums2):
            for x in nums2:
                if x in nums1:
                    nums1.remove(x)
                    result.append(x)
            return result
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                result.append(x)
        return result
