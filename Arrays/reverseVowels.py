def reverseVowels(s):
  '''
  Understand: 
  - Do I have to lowercase the vowels? 
  - What are the time and space complexities?
  
  Match: Use two pointers to reverse values.
  Store vowels in an array.

  For example:
     l   r
  1) hello
      l  r
  2) hello
       lr
  3) holle
  '''
  vowels = 'aeiouAEIOU'
  left = 0
  right = len(s) - 1
  s = list(s)
  while left < right:
      if s[left] not in vowels:
          left += 1
      elif s[right] not in vowels:
          right -= 1
      elif s[left] in vowels and s[right] in vowels:
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
  return ''.join(s)

# Time: O(n)
# Space: O(n)