class Solution:
    def DivisibleByEight(self,s):
        #code here
        
        x=int(s[-3:])
        
        #if last 3 digits of the given number s is not divisible by 8
        
        if x%8 != 0 :
            return -1
        else:
            return 1