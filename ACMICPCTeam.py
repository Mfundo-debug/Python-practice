"""
There are a number of people who will be attending ACM-ICPC World Finals.
Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, presented as binary strings,
determine the maximum number of topics a 2-person team can know. Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. 
Also determine the number of teams that know the maximum number of topics. Return an integer array with two elements. The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.
Example
n = 3
topics = ['10101', '11110', '00010']
Function Description

Complete the acmTeam function in the editor below.
acmTeam has the following parameter(s):

string topic: a string of binary digits
Returns

int[2]: the maximum topics and the number of teams that know that many topics
Constraints
2 ≤ n ≤ 500
1 ≤ m ≤ 500
"""
import math
import os
def acmTeam(topic):
    # Write your code here
    max_topics = 0
    max_teams = 0
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            topics = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    topics += 1
            if topics > max_topics:
                max_topics = topics
                max_teams = 1
            elif topics == max_topics:
                max_teams += 1
    return [max_topics, max_teams]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()