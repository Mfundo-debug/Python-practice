"""
Debug the given function print_from_stream using the default value of one of its arguments.

The function has the following signature:

def print_from_stream(n, stream)

This function should print the first n values returned by get_next() method of stream object provided as an argument. 
Each of these values should be printed in a separate line.

Whenever the function is called without the stream argument, 
it should use an instance of EvenStream class defined in the code stubs below as the value of stream.

Your function will be tested on several cases by the locked template code.
Input Format

The input is read by the provided locked code template. In the first line, there is a single integer q denoting the number of queries.
Each of the following q lines contains a stream_name followed by integer n, and it corresponds to a single test for your function.

Constraints
1 <= q <= 100
1 <= n <= 10
"""

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        value = stream.get_next()
        print(value)

if __name__ == '__main__':
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == 'even':
            stream = EvenStream()
        else:
            stream = OddStream()
        print_from_stream(n, stream)
