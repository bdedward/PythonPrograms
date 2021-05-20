#This program will take in a string and determine how many characters
#need to be removed in order to form a palindrome with the existing 
#characters

FLAG = 0
NumberChars = 256
length = 0


def palindrome(s):
    count = [0] * NumberChars
    for i in range(0, len(s)):
        count[ord(s[i])] = count[ord(s[i])] + 1
    odd = 0
    for i in range(0, NumberChars):
        if count[i] & 1:
            odd = odd + 1
        if odd > 1:
            return False
    return True


def recursion(s):
    global FLAG, length
    p = palindrome(s)
    if p and (len(s) > 1):
        FLAG = 1
        length = len(s)
    if not p and FLAG == 0 and len(s) > 1:
        for i in range(len(s)):
            substring = s[:i] + s[i+1:]
            recursion(substring)


def solution(s):
    before = len(s)
    recursion(s)
    return before - length

#Driver code to test "solution", solution takes a string
print(solution("america"))
