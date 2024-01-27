"""
Array pull is a program that pulls data from an array and prints it to the screen.
"""
def arrayPull(array):
    for i in range(len(array)):
        print(array[i])
    
if __name__ == '__main__':
    array = ["Hello", "World", "I", "am", "a", "programmer"]
    arrayPull(array)