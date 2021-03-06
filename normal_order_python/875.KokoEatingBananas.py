'''

875. Koko Eating Bananas

Medium

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
'''

piles, H = [312884470], 968709470
class Solution:   
    def minEatingSpeed(self, piles: list, H: int) -> int:
        left, right = 0, max(piles)
        while left < right: # O(lgn) for binary search, totally O(NlgN)
            mid = (left + right) / 2
            # print(left, right, mid)
            if self.whether(piles, H, mid): # this will take O(n)
                right = mid
            else:
                left = mid + 1
        return left
        
    def whether(self, piles, H, K):
        # print(K)
        total = [ (bananas+K-1)//K for bananas in piles]
        return sum(total) <= H

s = Solution()
print(s.minEatingSpeed(piles,H))