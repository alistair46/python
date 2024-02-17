'''
Rajiv wants to write a program to calculate the intersectional area between two circles. The following are the input parameters for him -

Input
first line accepts number of test cases
The following lines accept the x, y coordinates and radius for both circles

Sample Input
1
333442

Sample Output 
11.527246

'''
import math
t=int(input())
x1, y1, r1, x2, y2, r2 = map(int, input().split())
#print(x1,x2,y1,y2,r1,r2)

d=math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))
#print(d)

if r2< r1:
    temp=r1
    r1=r2
    r2=temp
part1 = r1 * r1 * math.acos((d * d +r1 * r1 -r2 * r2)/(2 * d * r1))
part2 = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1)/(2 * d * r2))
part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))

intersection=part1 + part2 - part3
print(intersection)