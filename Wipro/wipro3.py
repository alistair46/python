'''
The e-commerce company "TodaysApparel" has a list of sales values of N days. Some days the company made a profit, represented as a 
positive sales value. Other days the company incurred a loss, represented as a negative sales value. The company wishes to know 
the number of profitable days in the list. Write an algorithm to help the company know the number of profitable days in the list.

Input
The first line of input consists of an integer- numDays representing the number of days (N). The second line of input consists of N space- separated integers-sales[0]. sales[1] sales[N-1] representing the sales value of N days respectively.

Output
Print an integer representing the number of days the company made a profit.

Example

Input
7
23-7 13 -34 56 43 -12  

Output
4

Explanation
The number of positive sales values in the list is 4. Hence the output is 4.
'''

T=int(input())
arr=[int(i) for i in input().split()]
#print(arr)
count=0
for i in arr:
    if i>0:
        count=count + 1
print(count)
