"""
Priyanka works for an international toy company that ships by container. Her is to determine the lowest cost way to combine her orders for shipping.
She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. 
All items meeting that requirement will be shipped in one container.
What she wants to know is: what is the minimum number of containers she will need to ship all of her orders.

FOr example there are items weights w = [1, 2, 3, 4, 5, 10, 11, 12, 13]. This can be broken  into two containers: [1, 2, 3, 4, 5] and [10, 11, 12, 13]. Each container will contain items weighing within 4 units of the minimum weight item.

Function Description:
Complete the toys function in the editor below. It should return the minimum number of containers required to ship.

toys has the following parameter(s):

w: an array of integers that represent the weights of each order to ship

Constraints:
1 <= n <= 10^5
0 <= w[i] <= 10^4, where 0 <= i < n
"""

def toys(w):
    # Sort the list of item weights
    # Initialize a variable to keep track of the number of containers
    # Iterate through the sorted list of item weights
    # For each item weight, check if it can be added to the current container
    # If it cannot be added to the current container, increment the number of containers
    # Update the minimum weight for the current container
    # Return the number of containers
    w.sort()
    containers = 0
    min_weight = w[0]
    for weight in w:
        if weight > min_weight + 4:
            containers += 1
        min_weight = min(min_weight, weight)
    return containers + 1

if __name__ == '__main__':
    n = int(input().strip())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)