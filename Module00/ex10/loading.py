import time

braille = [u"\u258E", u"\u258C", u"\u258A", u"\u2588"]

def ft_progress(listy):
	current = 0
	size = len(listy)
	base_time = time.time()

	print(base_time)

	for x in listy:
		time_passed = int(time.time() - base_time)
		percent = current * 100 // size
		block_number = (percent // 4)
		print("\033[1F\033[2K", end='')
		print("\x1b[32;44m", end='')
		print('█' * block_number, end='')
		print(braille[percent % 4], end='')
		print(' ' * (24 - block_number), end='')
		print("\033[0m", end='')
		print(percent, " ", end='')
		print("time:%3d seconds" % time_passed, end='')
		print()
		current += 1
		yield x

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem * 3) % 5
	time.sleep(0.01)
print(ret)