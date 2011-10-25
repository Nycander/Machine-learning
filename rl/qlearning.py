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


def egreedy(e, f, args):
	if random() < e
		return args[random.randint(0, len[args]-1)]
	else
		return argmax f, args


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
# Policy iteration
policy = [None for s in trans]
value = [0 for s in trans]
for p in range(100):
	for s in range(len(policy)):
		policy[s] = argmax(
			lambda(a): 
				rew[s][a] + gamma*value[trans[s][a]], 
			range(4))
	
	for s in range(len(value)):
		a = policy[s]
		value[s] = rew[s][a] + gamma*value[trans[s][a]]


