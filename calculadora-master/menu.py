N1 = 5555

au1 = len(str(N1))

res = 0
while au1 > 0:
    au2 = str(N1)[-au1]
    au1 = au1 - 1
    res = int(au2) * 8 ** au1 + res
print(res)
