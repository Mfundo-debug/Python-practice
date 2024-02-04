"""
find the minimum number of operations required to convert a given string into a palindrome under certain conditions.
Example
s = "abc"
The following operations are performed:
Append a character to the end of the string: "abc".
Constraints:
1 <= |s| <= 10^3
s[i] is a lowercase English letter.
"""
def theLoveLetterMystery(s):
    count = 0
    for i in range(len(s)//2):
        count += abs(ord(s[i]) - ord(s[-i-1]))
    return count

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        print(result)