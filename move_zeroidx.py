"""
Given an array list [0,1,2,0,4,0]
move all the zeros into the middle like this [1,2,0,0,0,4]
"""
def move_zeros(arr):
    # iterate through the array
    # if the element is 0
    # remove it from the array
    # append it to the end of the array
    # return the array
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr

if __name__ == '__main__':
    arr = [0,1,2,0,4,0]
    print(move_zeros(arr))