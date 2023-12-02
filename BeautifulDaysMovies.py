"""
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. 
For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.
She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.
Given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day.
Print the number of beautiful days in the range.
Function Description

Complete the beautifulDays function in the editor below.

beautifulDays has the following parameter(s):

int i: the starting day number
int j: the ending day number
int k: the divisor
Returns

int: the number of beautiful days in the range
Constraints
1 <= i <= j <= 2 X 10^6
1 <= k <= 2 X 10^9
"""
def beautifulDays(i,j,k):
    count = 0
    for day in range(i,j+1):
        if abs(day - int(str(day)[::-1])) % k == 0:
            count += 1
    return count
if __name__ == '__main__':
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautifulDays(i,j,k)
    print(result)