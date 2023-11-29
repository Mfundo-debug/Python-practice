"""
You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars.
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price.
Specifically, the first game will cost p dollars, and every subsequent game will cost d dollars less than the previous one.
This continues until the cost becomes less than or equal to m dollars, after which every game will cost m dollars. 
How many games can you buy during the Halloween Sale?
Example
p =20
d =3
m =6
s =70
The following are the costs of the first 11 games in order:
20,17,14,11,8,6,6,6,6,6,6
Start at p=20 units cost, reduce by d=3 units until reaching a minimum possible price, m=6.
Starting with s = 70 units of currency in your Mist wallet, you can buy 5 games: 20+17+14+11+8=70.
Function Description

Complete the howManyGames function in the editor below.

howManyGames has the following parameters:

int p: the price of the first game
int d: the discount from the previous game price
int m: the minimum cost of a game
int s: the starting budget
Constraints
1 <= m <= p <= 100
1 <= d <= 100
1 <= s <= 10^4
"""
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p-d, m)
    return count
if __name__ == '__main__':
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = howManyGames(p, d, m, s)
    print(answer)