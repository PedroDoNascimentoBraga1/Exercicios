nums1 = [1,2,3,4,5]
nums2 = [9,8,7,6]
nums1.extend(nums2)
nums1.sort()
disel = len(nums1)

teset = 0 if disel == 0 else nums1[(len(nums1)) // 2] if len(nums1) % 2 != 0 else (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2 

print(teset)
