import time

# part 1
start = time.time()
doubles = 0
triples = 0
with open('./input.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		d = False
		t = False
		for letter in line:
			if line.count(letter) == 2:
				d = True
			elif line.count(letter) == 3:
				t = True
		if d: doubles += 1
		if t: triples += 1
	print('Part 1:', doubles*triples)
	end = time.time()
	print(end - start)
	
	# part 2
	start = time.time()
	lines = sorted(lines)
	diff = False
	for x in range(len(lines)):
		for y in range(x+1, len(lines)):
			for i in range(len(lines[x])):
				if diff and lines[x][i] != lines[y][i]:
					diff = False
					break
				elif lines[x][i] != lines[y][i]:
					diff = True
			if diff:
				break
		if diff:
				break
	r = ''
	for i in range(len(lines[x])):
		if lines[x][i] == lines[y][i]:
			r += lines[x][i]
	print('Part 2:', r)
	end = time.time()
	print(end - start)