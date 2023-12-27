class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        dict_nums1=Counter(nums1)
        dict_nums2 = Counter(nums2)
        for key,values in dict_nums1.items():
            if key in dict_nums2:
                if dict_nums1[key] <  dict_nums2[key]:
                    res.extend([key]*dict_nums1[key])
                else:
                    res.extend([key]*dict_nums2[key])
        return res

