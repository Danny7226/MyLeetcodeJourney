'''

Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

'''

text = "we will we will rock you"
first = "we"
second = "will"
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        if not text:
            return []
        words = text.split(' ')
        ans = []
        leng = len(words)
        for i in range(leng-1):
            if words[i] == first:
                if i+1<leng and words[i+1] == second:
                    if i+2<leng:
                        ans.append(words[i+2])
        return ans

s = Solution()
print(s.findOcurrences(text,first,second))       