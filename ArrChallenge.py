"""
Read the array stored in strArr which will represent a list of comma-separated numbers sorted in ascending order.
the second list of comma-separated numbers represent a second list of ascending order numbers (also with no duplicates).
your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
if there is no intersection, return the string false.
"""
def FindIntersection(strArr):
    strArr = strArr.split(', ')
    strArr1 = strArr[0].split(',')
    strArr2 = strArr[1].split(',')
    
    # Handle both integers and floating point numbers
    strArr1 = [float(i) if '.' in i else int(i) for i in strArr1]
    strArr2 = [float(i) if '.' in i else int(i) for i in strArr2]
    
    strArr1 = set(strArr1)
    strArr2 = set(strArr2)
    strArr = strArr1.intersection(strArr2)
    
    if len(strArr) == 0:
        return 'false'
    else:
        strArr = sorted(strArr)
        strArr = [str(i) for i in strArr]
        return ','.join(strArr)
if __name__ == '__main__':
    # keep this function call here
    print(FindIntersection(input()))