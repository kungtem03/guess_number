#產生一個隨機整數start~end (不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "恭喜猜對了"
#猜錯的話 要告訴他 比答案大或小

import random

start = int(input('請決定隨機數字範圍的開始值'))
end = int(input('請決定隨機數字範圍的結束值'))
num = 0

while num <= 15:
	answer = random.randint(start, end)
	num = num + 1
	guess = int(input('請猜一個數字: '))

	if guess < answer:
		print('你猜的數字太小了!','  你已經猜了{0}次'.format(num))
	elif guess > answer:
		print('你猜的數字太大了!','  你已經猜了{0}次'.format(num))
	else:
		print('恭喜猜對了!!!', '你總共猜了{0}次'.format(num))
		break