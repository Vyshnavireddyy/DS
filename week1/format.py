#t="my name is {fname}, I'm {age} years old".format(fname="John",age=23)
#print(t)
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
if b>c and b>c:
    print(b)
else:
    print(c)
