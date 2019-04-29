'''
32.9%	Easy

686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.


'''
A = "abcd"
B = "cdabcdab"
class Solution:

    def repeatedStringMatch(A: 'str', B: 'str') -> 'int':
        if len(set(B)) > len(set(A)):
            return -1
        
        if B in A:
            return 1
        if B in A+A:
            return 2
        
        len_div = len(B) // len(A)
        print(len_div)
        for i in range(len_div,len_div + 4):
            if B in A * i:
                return i 

        return -1

print(Solution.repeatedStringMatch(A,B))
# print(set(A),set(B))
# print(set(B) in set(A))