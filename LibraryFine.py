"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15 Hackos * (the number of days late).
f the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500 Hackos * (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 Hackos.
Example
d1,m1,y1=14,7,2018
d2,m2,y2=5,7,2018
The first values are the return date and the second are the due date. The years are the same and the months are the same. The book is 14-5=9 days late. Return 9*15=135.
Function Description

Complete the libraryFine function in the editor below.

libraryFine has the following parameter(s):

d1, m1, y1: returned date day, month and year, each an integer
d2, m2, y2: due date day, month and year, each an integer
Returns

int: the amount of the fine or 0 if there is none
Constraints
1<=d1,d2<=31
1<=m1,m2<=12
1<=y1,y2<=3000
It is guaranteed that the dates will be valid Gregorian calendar dates.
"""
def libraryFine(d1,m1,y1,d2,m2,y2):
    if y1>y2:
        return 10000
    elif m1>m2 and y1==y2:
        return (m1-m2)*500
    elif d1>d2 and m1==m2 and y1==y2:
        return (d1-d2)*15
    else:
        return 0
    
if __name__ == '__main__':
    d1,m1,y1=map(int,input().split())
    d2,m2,y2=map(int,input().split())
    print(libraryFine(d1,m1,y1,d2,m2,y2))