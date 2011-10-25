# From cartoon.py
import numpy
import pylab

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

# Policy iteration variables

gamma = 0.9
goodbad =   ((0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (1, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, -1, 0,),
			 (0, 0, 1, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (-1, 0, 0, 0,),
			 (0, 0, 0, 0,),
			 (0, 0, 0, 0,))

imfalling =
		((0, 0, -1, 0,), 
		(-1, 0, -1, 0,),
		(0, 0, -1, 0,),
		(0, -1, 0, -1,),
		(-1, -1, -1, 0,),
		(-1, -1, 0, -1,),
		(0, -1, 0, -1,),
		(-1, -1, 0, -1,),
		(-1, -1, 0, -1,),
		(0, -1, 0, -1,),
		(-1, -1, 0, -1,),
		(-1, -1, -1, 0,),
		(0, -1, 0, -1,),
		(-1, 0, -1, 0,),
		(-1, 0, -1, 0,),
		(0, 0, -1, 0,))

rev = imfalling + goodbad

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

# Patch together all walking animations from all states
comicbook = []
for state in range(0, 16) :
	test = []
	test.append(state)
	# Find 8 following states
	for f in range(0, 8) :
		state = trans[state][policy[state]]
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

