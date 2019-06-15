'''

Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make. 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 
'''

tiles = "AAABBC"
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        tile = list(tiles)
        def bt(comb, tile):
            if comb and comb not in ans:
                ans.add(comb)
            
            for i in range(len(tile)):
                if i>0 and tile[i] == tile[i-1]:
                    continue
                bt(comb+tile[i], tile[:i]+tile[i+1:])
        bt('', tile)
        print(ans)
        return len(ans)

s = Solution()
print(s.numTilePossibilities(tiles))        