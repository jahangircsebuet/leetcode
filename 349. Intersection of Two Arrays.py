class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        list1 = []
        list2 = []
        if len(nums1) > len(nums2):
            list1 = nums1
            list2 = nums2
        else:
            list1 = nums2
            list2 = nums1
        for x in list2:
            if x in list1:
                while x in list1: list1.remove(x)
                #while x in list2: list2.remove(x)
                #if x not in result:
                result.append(x)
        return result
