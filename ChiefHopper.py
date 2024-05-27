"""
Chief's bot is playing an old DOS based game. There is a row of buildings of different heights arranged at each index along a number line.
The bot starts at building 0 and at a height of 0. You must determine the minimum energy his bot needs at the start so that he can jump to the top of each building without his energy going below zero.

Units of height relate directly to units of energy. The bot's energy level is calculated as follows:
if the bots' botEnergy is less than the height of the building, his 
newEnergy = botEnergy + (height - botEnergy)
if the bot's botEnergy is greater than the height of the building, his
newEnergy = botEnergy - (botEnergy - height)
Example:
arr = [2,3,4,3,2]
The bot starts at building 0 with 0 energy and jumps to building 1 with cost 2 energy. His newEnergy = 2 - (2-3) = 3
Function Description

Complete the chiefHopper function in the editor below.

chiefHopper has the following parameter(s):

int arr[n]: building heights
Returns

int: the minimum starting botEnergy
Constraints
1 ≤ n ≤ 10^5

1 ≤ arr[i] ≤ 10^5 where 1 ≤ i ≤ n
"""
def chiefHopper(arr):
    n = len(arr)
    energy = 0
    for i in range(n-1, -1, -1):
        energy = (energy + arr[i] + 1) // 2
    return energy

if __name__ =='__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = chiefHopper(arr)
    print(result)