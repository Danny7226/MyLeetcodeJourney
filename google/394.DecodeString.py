'''
41.7%	Medium

394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

'''

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef"
s = "2[abc]3[cd]ef"
class Solution:
	def decodeString(s: str) -> str:
		buffer1 = ['']
		buffer2 = ['']
		layer = 0
		duplicators = [1]
		out = ''
		for i in range(len(s)):

			if(s[i] in '['):
				layer += 1
				if(layer > (len(buffer2) - 1)):
					buffer2.append('')
				continue

			if(s[i] in ']'):
				
				if(len(duplicators) == 0 ):
					duplicators = [0]

				layer -=1
				buffer2[layer] = buffer2[layer] + duplicators[layer+1] * buffer2[layer+1]
				buffer2[layer + 1] = ''
				duplicators[layer + 1] = 0
				# print(buffer2)
				continue

			if (s[i].isdigit()):
				if(layer <= len(duplicators) - 1 ):
					duplicators.append(0)				
				duplicators[layer+1] = duplicators[layer+1] * 10 + int(s[i])
				continue

			buffer2[layer] += s[i]
			

		return buffer2[0]

print(Solution.decodeString(s))





