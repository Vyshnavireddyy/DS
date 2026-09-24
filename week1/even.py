"""a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")"""
def odd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")

n=100
while n>=0:
    if n%2==0:
        print(n,end=" ")
    n-=1
