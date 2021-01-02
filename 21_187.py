def digitSum():
    s = str()
    array = list(map(int,s))
    return sum(array)
a = 0
b = 0
l = list(map(int, input().split()))
a = digitSum()
b = digitSum()

if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print(a)
