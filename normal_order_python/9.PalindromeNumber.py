'''

9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

'''

i = 12421


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        x1 = x
        while (x>0):
            reminder = x%10
            reverse = reverse*10 + reminder
            x = x//10

        return reverse == x1
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False

print(Solution.isPalindrome(i))