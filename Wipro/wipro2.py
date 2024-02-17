'''
The online math course provider 'MathAtTip' has designed a course for children called Learning Number Recognition and Counting. 
The assessment part of the course has a question where the student is given a number and a digit. The student needs to find out 
the total count of the digits present in the number excluding the given digit Write an algorithm to help the student find out the 
count of the total number of digits present in the number excluding the given digit


Input
The input consists of two integers number and digit where the first line integer represents the number and the second line 
integer represents the digit given to the student. 

Output
Print an integer representing the count of the total number of digits present in the number excluding

the given digit Constraints
0< number 10"
0<digit ≤9

Example

Input
5644456
5

Output
5

Explanation
Excluding 5; the digits in the number are 4 and 6 their total count is 5. Hence the output is 5.
'''

def countno(n,k):
    count = 0
    while(n!=0):
        if(n%10)!=k:
            count =count+1
        n = int(n/10)
    return(count)
n= int(input())
k=int(input())
print(countno(n,k))
