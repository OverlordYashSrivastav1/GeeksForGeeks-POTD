class Solution:   
    def peakElement(self,arr, n):
        # Code here
        
        left = 0
        right = n-1
        while left<right:
            mid = (left+right) // 2
            
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left