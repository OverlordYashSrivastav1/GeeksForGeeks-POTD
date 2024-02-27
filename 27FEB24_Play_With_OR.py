class Solution:
    def game_with_number (self, arr,  n) : 
        #Complete the function
        
        for i in range(len(arr)-1):
            arr[i] = arr[i] | arr[i+1]
            
        return arr

