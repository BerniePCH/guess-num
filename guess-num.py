import random

r = random.randint(1, 100)

while True:
	num = input('請輸入您猜的數字答案： ')
	num = int(num)
	if num == r:
		print('您猜對了！')
		break
	else:
		if num > r:
			print('您猜的數字太大囉！')
		elif num < r:
			print('您猜的數字太小囉！')
	
