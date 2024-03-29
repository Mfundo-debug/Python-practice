"""
Task
Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints
0 < Total number of students in college < 1000
"""

def difference(set1, set2):
    # return the difference of set1 and set2
    return set1.difference(set2)

if __name__ == '__main__':
    # Get the number of students subscribed to English newspaper
    n = int(input())

    # Get the roll numbers of students subscribed to English newspaper
    english = set(map(int, input().split()))

    # Get the number of students subscribed to French newspaper
    b = int(input())

    # Get the roll numbers of students subscribed to French newspaper
    french = set(map(int, input().split()))

    # Get the number of students who have subscribed to only English newspapers
    print(len(difference(english, french)))