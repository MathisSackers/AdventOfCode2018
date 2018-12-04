import time
import numpy as np

# part 1
start = time.time()
with open('./input.txt', 'r') as f:
	lines = f.readlines()
	lefts = [int(x[x.index('@') + 2:x.index(',')]) for x in lines]
	tops = [int(x[x.index(',') + 1:x.index(':')]) for x in lines]
	widths = [int(x[x.index(':') + 2:x.index('x')]) for x in lines]
	heigths = [int(x[x.index('x') + 1:]) for x in lines]
	inches = 0
	overlap = [] # part 2
	a = np.zeros(shape=(1000,1000))
	for claim in range(len(tops)):
		for x in range(lefts[claim], lefts[claim]+widths[claim]):
			for y in range(tops[claim], tops[claim]+heigths[claim]):
				if a[x][y] == 0:
					a[x][y] = claim + 1
				elif a[x][y] != -1:
					overlap.append(a[x][y]) # part 2
					overlap.append(claim + 1) # part 2
					a[x][y] = -1
					inches += 1
				else:
					overlap.append(claim + 1) # part 2
	print('Part 1:', inches)
	print('Part 2:', list(set(overlap).union(set(range(1, len(tops) + 1))) - set(overlap).intersection(set(range(1, len(tops) + 1))))[0])
	end = time.time()
	print(end - start)
