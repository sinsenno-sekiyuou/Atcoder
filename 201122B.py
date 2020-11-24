N, X = map(int, input().split()) #Xで改行なのでN,Xで止めてSを入れないでもN,S間に空白があるので.split()で区切る
S = input()
for s in S:
    if s == 'o':
        X += 1
    elif X:
        X -= 1
print(X)
