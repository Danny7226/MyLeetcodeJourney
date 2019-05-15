'''

tags: 2 ptrs

38. Count and Say

Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"


'''

n = 7
class Solution:
    def countAndSay(self, n: int) -> str:
        def count(n, s):
            if n == 1:
                return s
            else:
                ptr1 = 0
                ptr2 = 0
                temp = ''
                while(ptr2<len(s)):
                    while (ptr2 != len(s)) and (s[ptr2] == s[ptr1]):
                        ptr2 += 1
                    temp += str(ptr2-ptr1) + s[ptr1]
                    
                    ptr1 = ptr2
                print(temp)
                n -= 1
                return count(n, temp)

        output = ''         
        output = count(n,'1')
        return output 

s = Solution()
print(s.countAndSay(n))       