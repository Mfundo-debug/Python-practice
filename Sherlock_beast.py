"""
Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus. He also gives him a clue: an integer. Sherlock determines the key to removing the virus is to find the largest Decent Number having that number of digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
It is the largest such number for its length.
Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

For example, the numbers 55533333 and 555555 are both decent numbers because there are 3 5's and 5 3's in the first, and 6 5's in the second. They are the largest values for those length numbers that have proper divisibility of digit occurrences.
Function Description

Complete the decentNumber function in the editor below.

decentNumber has the following parameter(s):
int n: the length of the decent number to create
Prints

Print the decent number for the given length, or -1 if a decent number of that length cannot be formed. No return value is expected.
Constraints
1 ≤ t ≤ 20
1 ≤ n ≤ 100000
"""
def decentNumber(n):
    if n < 3:
        print(-1)
    elif n % 3 == 0:
        print("5" * n)
    elif n % 5 == 0:
        print("3" * n)
    else:
        fives = 0
        while n % 3 != 0:
            n -= 5
            fives += 5
        if n < 0:
            print(-1)
        else:
            print("5" * n + "3" * fives)
    return None

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        decentNumber(n)