"""
Jane loves strings more than anything. She has a string t with her, and value of a string s over function f can be calculated as given below:
f(s) = |s| * (number of occurrences of s in t)
Jane wants to know the maximum value of f(s) among all the substrings (s) of string t. can you help her?
Input Format
A single contains a string t (1 <= |t| <= 10^5)
Output Format
Print the maximum value of f(s) among all the substrings (s) of string t.
Constraints
1 <= |t| <= 10^5
The string consists lowercase English alphabets
1 test failed
"""
def max_value_of_f_s(t):
    n = len(t)
    max_value = 0
    for i in range(n):
        for j in range(i+1, n+1):
            s = t[i:j]
            count_s = sum(1 for k in range(n-len(s)+1) if t[k:k+len(s)] == s)
            max_value = max(max_value, len(s) * count_s)
    return max_value

if __name__ == '__main__':
    t = input()
    result = max_value_of_f_s(t)
    print(result)