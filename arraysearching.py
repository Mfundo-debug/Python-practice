"""
Array searching the value and the string and finding sum of the string
Example
list = ["word": 1, "word2": 2, "word3": 3]
output
sum = 6
"""
def arraySearch(list):
    sum = 0
    for i in list:
        sum += list[i]
    return sum
if __name__ == "__main__":
    list = {"word": 1, "word2": 2, "word3": 3}
    result = arraySearch(list)
    print(result)