"""
Task
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i2.

Example
n = 3
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
0
1
4
Input Format
The first and only line contains the integer,n .

Output Format
Print n lines, one corresponding to each i.

Sample Input 0
5
Sample Output 0
0
1
4
9
16
"""
if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i**2)
        i+=1
