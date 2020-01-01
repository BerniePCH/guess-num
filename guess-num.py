import random

start = input('請輸入隨機數字開始值： ')
end = input('請輸入隨機數字結束值： ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
count = int(count)

while True:
	count = count + 1 #count += 1
	count <= 5
	num = input('請輸入您猜的數字答案： ')
	num = int(num)
	if num == r:
		print('您猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('您猜的數字太大囉！')
	elif num < r:
		print('您猜的數字太小囉！')
	print('這是你猜的第', count, '次')
	
	
