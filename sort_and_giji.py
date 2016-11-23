#擬似乱数を発生
import random

a = []
for i in range(100):
	a = a + [i+1]

for i in range(50):
	ran = int(random.randint(0,99))
	b = a[i]
	a[i] = a[ran]
	a[ran] = b

print(a)
#出来上がったはいれつ

#数列をソートする
leng = len(a)

for j in range(leng-1):
	chen = 0
	for i in range(leng-1-j):
		if a[leng-i-1] < a[leng-i-2]:
			b = a[leng-i-1]
			a[leng-1-i] = a[leng-i-2]
			a[leng-2-i] = b
			chen = chen + 1
	#もし変更を一回も行わなかった場合。終了
	if chen == 0:
		break

#並び替えが完了した配列
print(a)
