# names = ['Arthur','Vahag','Ani']
# for name in names:
# 	print(name)
# names = 'Aramayis'
# for a in names:
# 	print(a)

# name = 'Xachatur'
# for i in name:
# 	print(i)
# 	if i == 'u':
# 		break

# name = 'Xachatur'
# for i in name:
# 	if i == 'c' or i == 'h':
# 		continue
# 	print(i) 

# for i in range(3):
	# num = int(input('Gushakir tivy '))
	# if num == 3:
	# 	print('you win ')
	# 	break
	# else:
	# 	print('wrong answer ')


# for i in range(0,100,2):
# 		print(i)

# name = 'haykush'
# name = iter(name)
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# try:
# 	print(next(name))
# except:
# 	print('end')


# for i in '♥♦♣♠':
# 	for j in 'JQKT':
# 		print(i,j)

# while True:
# 	x = 6
# 	num = int(input('number'))
# 	if num == x:
# 		print('win')
# 		break
# 		else:
# 		print('Losser')




# while True:
# print('hi')


# i = 1	
# while i  < 6:
# 	print(i)
# 	i += 1


# import time 

# while True:
# 	localtime = time.localtime()
# 	result = time.strftime('%I:%M:%S %p',localtime)
# 	print(result)
# 	time.sleep(1)


# name = 'odanavakayan'
# x = 0
# for i in name:
# 	if i == 'a':
# 		x += 1
# print(x)


# import time 
# import os

# res = 0
# while True:
# 	os.system('cls')
# 	res += 1
# 	print('\n'*14,' '*43,res)
# 	time.sleep(1)


import random 
es = 0
pc = 0
while True:
	i = int(input('number '))
	p = random.randint(1,3)
	
	if i == p:
		print(i,p)
		es += 1
	else:
		print(i,p)
		pc += 1
		if es == 3:
			print('you win')
			break
		elif pc == 3:
			print('pc',pc,es)
			break