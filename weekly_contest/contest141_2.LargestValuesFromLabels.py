'''

1090. Largest Values From Labels

Medium

We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

 

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.
Example 4:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.

'''

values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 1

class Solution:
    def largestValsFromLabels(self, values: list, labels: list, num_wanted: int, use_limit: int) -> int:
        stack = []
        output = 0
        for i in range(len(values)):
            stack.append((values[i],labels[i]))
        stack.sort(key = lambda x:x[0])
        # print(stack)
        num, use = 0, {}
        while num < num_wanted and stack:
            value, label = stack.pop()
            # print(value,label)
            if label not in use:
                use[label] = 1
                output += value
                num += 1
            elif use[label] < use_limit:
                use[label] += 1
                output += value
                num += 1                
            else:
                continue
            
        return output
s = Solution()
print(s.largestValsFromLabels(values,labels,num_wanted,use_limit))    