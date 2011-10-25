import random

import environment

states = range(16)
actions = range(4)

# Initialize Q(s, a) arbitrarily for all s and a
Q = [[random.normalvariate(0, 2) for a in range(len(actions))] for s in range(len(states))]

# Initialize s
s = random.randrange(0, len(state))

# Repeat for each step: (Until T steps)
for t in range(T):
	# * Choose a from s using e-greedy policy based on Q(s, a)
	a = argmaxEgreedy(Q, s)
	# * Take action a, observe r, and next state s'

	# * Update Q(s, a) <- Q(s, a) + n[r + gamma * max_(a') Q(s', a') - Q(s, a)]

	# * Replace s with s'