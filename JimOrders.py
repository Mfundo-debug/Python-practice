"""
Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them. 
Determine the order the customers receive their orders. Start by numbering each of the customers from 1 to n, front of the line to the back.
You will then be given an order number and a preparation time for each customer. The time of delivery is calculated as the sum of the order  number and the preparation time.
If two orders are delivered at the same time, assume they are delivered in ascending customer number order.
For example, there are n=5, customers in line. They each receive an order number order[i] and a preparation time prep[i].:
Customer	1	2	3	4	5
Order #		8	5	6	2	4
Prep time	3	6	2	3	3

FUnction Description:
Complete the jimOrders function in the editor below. It should return an array of integers that represent the order that customers' orders are delivered.

jimOrders has the following parameter(s):

orders: a 2D integer array where each orders[i] is in the form [order[i], prep[i]]

Constraints:
1 <= n <= 10^3
1 <= i <= n
1 <= order[i], prep[i] <= 10^6
"""
def jimOrders(orders):
    # Create a list of tuples where the first element is 
    # the order number and the second element is the delivery time
    # The delivery time is the sum of the order number and the preparation time
    # Sort the list of tuples based on the delivery time
    # Return a list of the order numbers in the sorted list of tuples
    return [i[0] for i in sorted(enumerate(orders, 1), key=lambda x: sum(x[1]))]

if __name__ == '__main__':
    n = int(input().strip())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    print(result)