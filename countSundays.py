"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month between two dates(both inclusive)?

Input Format

The first line contains an integer T, i.e., number of test cases.
Each testcase will contain two lines
$Y_1 M_1 D_1$ on first line denoting starting date.
$Y_2 M_2 D_2$ on second line denoting ending date.

Constraints
1 <= T <= 100
1900 <= Y_1 <= 10^16
Y_1 <= Y_2 <= (Y_1 + 1000)
1 <= M_1, M_2 <= 12
1 <= D_1, D_2 <= 31
"""
import datetime

def count_sundays(start_date, end_date):
    # Convert start and end dates to datetime objects
    start = datetime.datetime.strptime(start_date, '%Y %m %d')
    end = datetime.datetime.strptime(end_date, '%Y %m %d')

    # Initialize count to 0
    count = 0

    # Iterate over all months and years between start and end dates
    while start <= end:
        # Check if the first day of the month is a Sunday
        if start.day == 1 and start.weekday() == 6:
            count += 1

        # Move to the next month
        if start.month == 12:
            start = start.replace(year=start.year+1, month=1)
        else:
            start = start.replace(month=start.month+1)

    return count

if __name__ == '__main__':
    # Get the number of test cases
    T = int(input())

    # Iterate over the test cases
    for _ in range(T):
        # Get the start and end dates
        start_date = input()
        end_date = input()

        # Print the number of Sundays
        print(count_sundays(start_date, end_date))
