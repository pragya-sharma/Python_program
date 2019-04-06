#Dividing rational numbers
import math
n = int(input())
n1,d1 = map(int,input().split(" "))
n2,d2 = map(int,input().split(" "))
n3,d3 = map(int,input().split(" "))
multi_numerator = n1*n2*n3
multi_denomrator = d1*d2*d3
gcd = math.gcd(multi_numerator,multi_denomrator)
new_numrator = multi_numerator//gcd
new_denomrator = multi_denomrator//gcd
print(new_numrator)
print(new_denomrator)
