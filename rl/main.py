gamma = 0.9
rew = ( # CO SKRIVER DET HÄR
		)

trans = ((1, 3, 4, 12),
		 (0, 2, 5, 13),
		 (3, 1, 6, 14),
		 (2, 0, 7, 15),
		 (5, 7, 0, 8),
		 (4, 6, 1, 9),
		 (7, 5, 2, 10),
		 (6, 4, 3, 11),
		 (9, 11, 12, 4),
		 (8, 10, 13, 5),
		 (11, 9, 14, 6),
		 (10, 8, 15, 7),
		 (13, 15, 8, 0),
		 (12, 14, 9, 1),
		 (15, 13, 10, 2),
		 (14, 12, 11, 3))

# Policy iteration
policy = [None for s in trans]
value = [0 for in trans]
for p in range(100):
	for s in range(len(policy)):
		policy[s] = argmax(
			lambda(a): 
				rew[s][a] + gamma*value[trans[s][a]], 
			range(4))
	
	for s in range(len(value)):
		a = policy[s]
		value[s] = rew[s][a] + gamma*value[trans[s][a]]

# Utility function argmax
def argmax(f, args):
	mi = None
	m = -1e10
	for i in args:
		v = f(i)
		if v > m:
			m = v
			mi = i
	return mi
