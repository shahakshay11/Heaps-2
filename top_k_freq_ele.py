"""
// Time Complexity : O(nlogk)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        Heap approach
        - Create a min heap out of the frequency of the elements
        - If the heap size > k, pop the elements 
        - fetch the most frequent elements in the result array
        """
        heap = []
        freq_map = Counter(nums)
        for ele,freq in freq_map.items():
            heapq.heappush(heap,(freq,ele))
            if len(heap) > k:
                heappop(heap)
        
        result = []
        while heap:
            result.append(heappop(heap)[1])
        
        return result