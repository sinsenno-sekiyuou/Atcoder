N = int(input())
ans =  ""
for i in range(1,99):
    if N <= 26 ** i:
        N -= 1
        for j in range(i):
            ans += chr(ord("a") + N % 26)
            N //= 26
        break
    else:
        N -= 26 ** 1
print(ans[::-1])

#https://www.javadrive.jp/python/for/index5.html
#https://techacademy.jp/magazine/36090
#これからは公式解説みてネットで調べつつ動画でわからんかったら見てからユーザー解説のぞくー