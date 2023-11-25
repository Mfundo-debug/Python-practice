"""
There is a strange counter. At the first second, it displays the number 3.
Each second, the number displayed by decrements by 1 until it reaches 1.
In next second, the timer resets to 2 x the initial number for the prior cylce and continues counting down.
Find and print the value displayed by the counter at time t.

Function Description

Complete the strangeCounter function in the editor below.

strangeCounter has the following parameter(s):

int t: an integer
Returns

int: the value displayed at time t.
Constraints
1 <= t <= 10^12
Subtask
1 <= t <= 10^5 for 60% of the maximum score.
"""
def strangeCounter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    return rem-t+1
if __name__ == '__main__':
    t = int(input().strip())
    result = strangeCounter(t)
    print(result)