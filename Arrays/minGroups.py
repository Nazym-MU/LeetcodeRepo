# 2406. Divide Intervals Into Minimum Number of Groups
"""
INTUITION:
Because the elements are sorted, we can keep track of the right element in each of the intervals. As we traverse the intervals, if we encounter an interval, the left element of which is less than the right element of the first interval in our heap, we pop from the heap.  

EXAMPLE: 
sorted array: [1,5],[1,10],[2,3],[5,10],[6,8]
pq = []
1. [5]
2. [5,10]
3. [5,10,3]
4. [5,10,3,10]
5. [5,10,3]
"""
class Solution(object):
  def minGroups(self, intervals):
      pq = []
      for left, right in sorted(intervals):
          if pq and pq[0] < left:
              heappop(pq)
          heappush(pq, right)
      return len(pq)
'''
Time Complexity: O(nlogn) because of sorting
Space Complexity: O(n) becuse of heap
'''