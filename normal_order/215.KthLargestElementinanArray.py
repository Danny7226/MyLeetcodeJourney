'''

215. Kth Largest Element in an Array

Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''
'''
# min heap
function heapify(arr, root, max) {
	let toSwapIdx;
	let leftChildIdx;
	let rightChildIdx;

	while(root < max) {
		toSwapIdx = root;
		leftChildIdx = 2 * root + 1;
		rightChildIdx = 2 * root + 2;
		if(leftChildIdx < max && arr[root] > arr[leftChildIdx]) {
			toSwapIdx = leftChildIdx;
		}

		if(rightChildIdx < max && arr[toSwapIdx] > arr[rightChildIdx]) {
			toSwapIdx = rightChildIdx;
		}

		if(root == toSwapIdx) return;

		swap(arr, toSwapIdx, root);
		root = toSwapIdx;
	}
} 
'''
## HEAP RUN TIME O(N + klgN)
# min - heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = nums[:k]
        heapq.heapify(ans) # run time O(n)
        for i in range(k, len(nums)):
            heapq.heappushpop(ans, nums[i]) # if nums[i] > ans[0] => heapq.push, run time O(klgn)
        # print(ans)
        return ans[0]   

# max - heap - #1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = heapq.nlargest(k, nums) # run time O(n+klgn)
        return ans[-1]

# max - heap - #2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums) # run time O(k)
        for _ in range(k):
            ans = heapq.heappop(nums) # run time O(nlgk)
        return -ans    

## QUICK SELECT RUN TIME O(N) ON AVERAGE
class Solution:
    # quick select, based on quick sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        # print(nums, k, pivot)
        l, r, m = [], [], []
        for i in nums:
            if i == pivot:
                m.append(i)
            elif i < pivot:
                l.append(i)
            else:
                r.append(i)
        # print(l, m, r)
        ll, lm, lr = len(l), len(m), len(r)
        if lr < k <= lr+lm:
            return m[0]
        elif k <= lr:
            return self.findKthLargest(r, k)
        else:
            return self.findKthLargest(l, k-lr-lm)
               