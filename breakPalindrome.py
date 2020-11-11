def breakPalindrome(palindrome):
    n = len(palindrome)
    if n == 1:
        return ""
    first_half = list(palindrome[:n//2])
    second_half = list(palindrome[n//2:])
    for i in range(len(first_half)):
        char = first_half[i]
        if ord(char) - ord('a') > 0:
            first_half[i] = 'a'
            return ''.join(first_half) + ''.join(second_half)
    for i in range(len(second_half)-1, -1, -1):
        char = second_half[i]
        if ord(char) - ord('a') == 0:
            second_half[i] = 'b'
            return ''.join(first_half) + ''.join(second_half)
    return ''
