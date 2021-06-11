def avg(a, b, c):
	return (a + b + c) / 3
avg(1, 2, 3)


def avg1(a):
	total = 0
	for v in a:
		total += v
	return total / len(a)
avg1(1, 2, 3, 4, 5)
