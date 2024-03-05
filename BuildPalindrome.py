"""
s = can be expressed as s = s_a + s_b where s_a is a non-empty substring of a and s_b is the non-empty of b.
s is a palindrome string. the length of s is as long as possible.
for each of q pairs of strings(a_i and b_i) received as input, find and print string s_i on a new line.
if you're able to form more than one valid string s_i, print whichever one comes first alphabeticallt. if there is no valid string s_i, print -1.
Constraints
1 <= q <= 10
1 <= |a|, |b| <= 10^5
a and b contain only lowercase English letters.
sum of |a| over all queries does not exceed 2*10^5
sum of |b| over all queries does not exceed 2*10^5
"""
def build_palindrome(a, b):
    def is_palindrome(s):
        return s == s[::-1]

    a = a.lower()
    b = b.lower()
    b = b[::-1]  # Reverse b to find the longest common suffix of a and prefix of b
    max_length = 0
    palindrome = ''

    for i in range(1, min(len(a), len(b)) + 1):
        if a[-i:] == b[:i] and is_palindrome(a + b[i:]):
            if i > max_length:
                max_length = i
                palindrome = a + b[i:]

    if max_length == 0:
        return -1
    else:
        return palindrome

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        result = build_palindrome(a, b)
        print(result)