"""
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories.
If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least 2^j * c miles to maintain his weight.
Example
caloric = [5,10,7]
If he eats the cupcakes in the order 5,10,7, the miles he will need to walk are (2^0 * 5) + (2^1 * 10) + (2^2 * 7) = 5 + 20 + 28 = 53.
This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles is calculated as (2^1 * 7) + (2^0 * 10) + (2^2 * 5) = 14 + 10 + 20 = 44.
Given the individual calori counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.
Function Description

Complete the marcsCakewalk function in the editor below.

marcsCakewalk has the following parameter(s):

int calorie[n]: the calorie counts for each cupcake
Returns

long: the minimum miles necessary

Constraints
1 <= n <= 40
1 <= c[i] <= 1000
"""
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for i in range(len(calorie)):
        miles += (2**i) * calorie[i]
    return miles

if __name__ == '__main__':
    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)