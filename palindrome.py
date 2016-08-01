def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq)> 1:
        if dq.popleft() != dq.pop():
            return False
    return True
    
def another_palindrome(word):
    return word == word[::-1]