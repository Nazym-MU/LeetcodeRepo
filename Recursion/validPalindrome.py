# A helper function to check if substring s[i:j+1] is a palindrome
# Your function isPalindrome is called as such:
# s = "people"
# isPalindrome(s)


def isPalindrome(s):
  def is_palindrome_range(i: int, j: int) -> bool:
    return all(s[k] == s[j - k + 1] for k in range(i, j))

  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return is_palindrome_range(left + 1, right) or is_palindrome_range(
          left, right - 1)
    left += 1
    right -= 1

  return True  

print(isPalindrome('aba'))
print(isPalindrome('abca'))
print(isPalindrome('abc'))
print(isPalindrome('abcca'))

