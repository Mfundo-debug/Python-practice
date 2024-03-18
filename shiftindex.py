"""
Given an array [1,2,-3,0,0,5,4], shift zeros to the initial part of the array and shift non-zeros to the end of the array. 
The result should be [0,0,1,2,-3,5,4].

"""
def shiftindex(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] == 0:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr

if __name__ == '__main__':
    arr = [1,2,-3,0,0,5,4]
    print(shiftindex(arr))