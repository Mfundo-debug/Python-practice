"""
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Example
scores = [12,24,10,24]
Scores are in the same order as the games played.
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

int scores[n]: points scored per game
Returns

int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
Input Format

The first line contains an integer , the number of games.
The second line contains  space-separated integers describing the respective values of score0,score1,...,scoren-1.

Constraints
1<=n<=1000
0<=scores[i]<=10^8
"""

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for i in range(1, len(scores)):
        if scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
        if scores[i] > max_score:
            max_score = scores[i]
            max_count += 1
    return max_count, min_count

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
    print('\n')