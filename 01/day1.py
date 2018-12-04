import time

# part 1
start = time.time()
r = 0
with open('./input.txt', 'r') as f:
	lines = f.readlines()
	for l in lines:
		r += int(l)
	print('Part 1:', r)
	end = time.time()
	print(end - start)
	
	# part 2 - fast
	start = time.time()
	r = 0
	a = {}
	i = 0
	while r not in a:
		a[r] = True
		r += int(lines[i%len(lines)])
		i += 1
	print('Part 2:', r, 'in', i,'steps')
	end = time.time()
	print(end - start)
	
	# part 2 - slow
	start = time.time()
	r = 0
	a = []
	i = 0
	while r not in a:
		a.append(r)
		r += int(lines[i%len(lines)])
		i += 1
	print('Part 2:', r, 'in', i,'steps')
	end = time.time()
	print(end - start)