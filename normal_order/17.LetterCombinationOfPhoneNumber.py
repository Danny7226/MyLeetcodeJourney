'''

tag: backtracking

17. Letter Combinations of a Phone Number

Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

'''

digits = '23' 

# class Solution:
#     def letterCombinations(digits: str) -> list:
#         if digits == '':
#             return []

#         output = ['']
#         table = {'2':'abc', '3':'def', '4':'ghi',
#                 '5':'jkl', '6':'mno', '7':'pqrs',
#                 '8':'tuv', '9':'wxyz'}
#         for i in digits:
#             print('i:',i)
#             cur = []
#             for j in output:
#                 print('output1:',output, end = '  ')
#                 print('j:',j)
                
#                 for letter in table[i]:
#                     cur.append(j + letter)             
#             output = cur
#             print('output2:',output)
#         return output

class Solution:

    # Hashtable and recursion
    def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                print(combination)
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    # print(next_digits[1:])
                    # !important: no 'combination += letter' here
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output


print(Solution.letterCombinations(digits))
# print(digits[len(digits):]) # still output '' without raising an error