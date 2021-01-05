N,X = map(int,input().split())
S = input()

for s in S:
    if s == "○":
        X += 1
    elif X:
        X -= 1

print(x)