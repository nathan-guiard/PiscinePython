import time

blocks = [u"\u258F", u"\u258E", u"\u258D", u"\u258C", u"\u258B", u"\u258A", u"\u2589", u"\u2588"]

def ft_progress(listy):
	current = 0
	size = len(listy)
	base_time = time.time()

	print(base_time)

	for x in listy:
		time_passed = int(time.time() - base_time)
		percent = current * 200 // size
		block_number = (percent // 8)

		if current + 1 == size:
			print("\033[1F\033[2K", end='')
			print("Progress: 100%% | %5d " % size, end='')
			print("\x1b[32;44m", end='')
			print('█' * 25, end='')
			print("\033[0m", end='')
			print("", size, end='')

		else:
			print("\033[1F\033[2K", end='')
			print("Progress: %3d%% | %5d " % (int(percent / 2), current), end='')
			print("\x1b[32;44m", end='')
			print('█' * block_number, end='')
			print(blocks[percent % 8], end='')
			print(' ' * (24 - block_number), end='')
			print("\033[0m", end='')
			print("", size, end='')

		if time_passed >= 60:
			print(" | time: %2dm %2ds" % (time_passed // 60, time_passed % 60), end='')
		else:
			print(" | time: %2ds" % time_passed, end='')

		print()
		current += 1
		yield x

listy = range(333333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
print(ret)