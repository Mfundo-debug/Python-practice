"""
Taum is planning to celebrate the birthday of his friend, Diksha.
There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
To make her happy, Taum has to buy b black gifts and w white gifts.

The cost of each black gift is bc units.
The cost of every white gift is wc units.
The cost to convert a black gift into white gift or vice versa is z units.
Determine the minimum cost of Diksha's gifts
Example
b =3
w =5
bc =3
wc =4
z =1
He can buy a black gift for 3 and convert it to a white gift for 1, 
making the total cost of each white gift 4. 
That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. 
Either way, the overall cost is  3*3+5*4 = 29.
Function Description

Complete the function taumBday in the editor below. It should return the minimal cost of obtaining the desired gifts.

taumBday has the following parameter(s):

int b: the number of black gifts
int w: the number of white gifts
int bc: the cost of a black gift
int wc: the cost of a white gift
int z: the cost to convert one color gift to the other color
Returns

int: the minimum cost to purchase the gifts
Constraints
1 <= t <= 10
0 <= b,w,bc,wc,z <= 10^9
"""
def taumBday(b,w,bc,wc,z):
    if bc > wc + z:
        return (b+w)*wc + b*z
    elif wc > bc + z:
        return (b+w)*bc + w*z
    else:
        return b*bc + w*wc
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b,w = map(int,input().split())
        bc,wc,z = map(int,input().split())
        print(taumBday(b,w,bc,wc,z))