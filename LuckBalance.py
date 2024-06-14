"""
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests.
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i]:
- L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].
- T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
If lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.
Example:
k =2
L = [5, 1, 4]
T = [1, 1, 0]
If Lena loses all of the contests, her will be 5 + 1 + 4 = 10. Since she is allowed to lose 2 important contests, and there are only 2 important contests. 
She can lose all three contests to maximize her luck at 10. If k = 1, she has to win at least 1 of the 2 important contests. She would choose to win the lowest value important contest worth 1. 
Her final luck will be 5 + 4 - 1 = 8.
Function Description

Complete the luckBalance function in the editor below.

luckBalance has the following parameter(s):

int k: the number of important contests Lena can lose
int contests[n][2]: a 2D array of integers where each contests[i] contains two integers that represent the luck balance and importance of the i^th contest
Returns
- int: the maximum luck balance achievable
Constraints
1 <= n <= 100
0 <= k <= N
1 <= L[i] <= 10^4
0 <= T[i] <= 1
"""

def luckBalance(k, contests):
    # Sort the contests in descending order
    contests.sort(reverse=True)
    luck = 0
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]
    return luck

if __name__ == '__main__':
    # Read the input
    n, k = map(int, input().split())
    contests = [list(map(int, input().split())) for _ in range(n)]
    # Call the luckBalance function
    result = luckBalance(k, contests)
    print(result)