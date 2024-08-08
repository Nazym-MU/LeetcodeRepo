def canPlaceFlowers(flowerbed, n):
  '''
  - check both left and right
  - left and right are boolean values
  - if both are true and they are 0s and the current item is 0, then n-=1
  - change to 1
  - at the end, return n <= 0

  for example:
  [0, 0, 1, 0, 1]
  1. check first index, can plant because it's the first item, right == 0, so n-=1
  2. check second index, cannot plant because left == 1 (updated) and right == 1
  3. check third index, cannot plant because it's not 0
  etc.
  '''
  for i in range(len(flowerbed)):
      left = i == 0 or flowerbed[i-1] == 0
      right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
      if left and right and flowerbed[i] == 0:
          n -= 1
          flowerbed[i] = 1
  return n <= 0

# Time: O(n)
# Space: O(1)