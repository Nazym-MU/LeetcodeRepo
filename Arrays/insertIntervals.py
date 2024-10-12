class Solution(object):
  def insert(self, intervals, newInterval):
      """
      newInterval: [4,8]
      [1,2],[3,5],[6,7],[8,10],[12,16]
      Get the arrays before newInterval: [1,2]
      Get the arrays after newInterval: [12,16]
      Modify newInterval: [3,5],[4,8],[6,7],[8,10] => [3,10]
      Add all of these arrays together
      """
      s, e = newInterval[0], newInterval[1]
      left, right = [], []

      for i in intervals:
          if i[1] < s:
              left.append(i)
          elif i[0] > e:
              right.append(i)
          else:
              newInterval[0] = min(newInterval[0], i[0])
              newInterval[1] = max(newInterval[1], i[1])
      return left + [newInterval] + right

'''
Time complexity: O(n) because we are iterating through the intervals array once
Space complexity: O(n) because we are creating two new arrays
'''