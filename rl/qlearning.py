import random
import numpy
import pylab
import environment
import pprint

images = (pylab.imread('step1.png'),
          pylab.imread('step2.png'),
          pylab.imread('step3.png'),
          pylab.imread('step4.png'),
          pylab.imread('step5.png'),
          pylab.imread('step6.png'),
          pylab.imread('step7.png'),
          pylab.imread('step8.png'),
          pylab.imread('step9.png'),
          pylab.imread('step10.png'),
          pylab.imread('step11.png'),
          pylab.imread('step12.png'),
          pylab.imread('step13.png'),
          pylab.imread('step14.png'),
          pylab.imread('step15.png'),
          pylab.imread('step16.png'))

def egreedy(e, f, args):
	if random.random() < e:
		return args[random.randint(0, len(args)-1)]
	else:
		return argmax(f, args)


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
# Constants for Q-learning
learningRate = 0.9 # 0 < n < 1
discountFactor = 0.9 # 0 < g < 1
chooseBestFactor = 0.1 # 0 < e < 1

# Variables for current experiment
states = range(16)
actions = range(4)

# Initialize Q(s, a) arbitrarily for all s and a
Q = [[random.normalvariate(0, 2) for a in range(len(actions))] for s in range(len(states))]

# Initialize s
state = random.randrange(0, len(states))

environment = environment.Environment(state)

# Repeat for each step: (Until T steps)
T = 1000
for t in range(T):
	# * Choose a from s using e-greedy policy based on Q(s, a)
	action = egreedy(chooseBestFactor, lambda(a): Q[state][a], actions)
	# * Take action a, observe r, and next state s'
	(newState, reward) = environment.go(action)
	# * Update Q(s, a) <- Q(s, a) + n[r + gamma * max_(a') Q(s', a') - Q(s, a)]
	maxFutureValue = Q[newState][argmax(lambda(newAction): Q[newState][newAction], actions)]
	Q[state][action] += learningRate*(reward + discountFactor*maxFutureValue - Q[state][action])
	# * Replace s with s'
	state = newState

pprint.pprint(Q)

# Patch together all walking animations from all states
comicbook = []
for state in range(0, 16) :
	test = []
	test.append(state)
	# Find 8 following states
	for f in range(0, 8) :
		action = egreedy(0, lambda(a): Q[state][a], actions)
		(state, reward) = environment.go(action)
		test.append(state)
	# Show comic
	comic = numpy.concatenate([images[i] for i in test], axis=1)
	if len(comicbook) == 0:
		comicbook = comic
	else:
		comicbook = numpy.concatenate((comicbook, comic), axis=0)
	
# Show comics for all states
pylab.imshow(comicbook)
pylab.show()
