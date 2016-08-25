word = 'HannaH'

#recursive approach
def isPalindrome(x):
    if len(x) < 2: return True
    if x[0] != x[-1]: return False
    return isPalindrome(x[1:-1])

print isPalindrome(word)


#non-recursive approach
isPalindrome = word == word[::-1]
print isPalindrome


print -2%2