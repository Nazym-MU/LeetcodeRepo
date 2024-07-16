from collections import deque
def minOperations(logs):
  stack = deque()
  for log in logs:
      if log == "../":
          if stack:
              stack.pop()
      elif log != "./":
          stack.append(log)
  return len(stack)