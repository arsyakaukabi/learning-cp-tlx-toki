import math; 
i = lambda:map(int, input().split())

a, b = i(); c, d = i()
num = d*a+b*c
dem = b*d
div = math.gcd(num,dem)
print('{} {}'.format(num//div,dem//div))