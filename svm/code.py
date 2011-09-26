from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math

# A suitable kernel function
def linearKernel(x, y):
	return x[0] * y[0] + x[1] * y[1] +1

def kernel(x, y):
	return linearKernel(x, y)

# Build P matrix from a given set of data points
def buildP(data):
	P = [None] * len(data) # Init NxN matrix.
	for i in range(0, len(data)):
		P[i] = [None] * len(data)
		for j in range(0, len(data)):
			P[i][j] = float(data[i][2]*data[j][2] * kernel(data[i][0:2], data[j][0:2]))
	return P

# Implement the indicator function
def indicator(x, data, alphas):
	ret = 0.0
	for (i, alpha) in alphas:
		ret += alpha*data[i][2]*kernel(x, data[i][0:2])
	return ret

def calculateAlphas(trainingData)

	# Build the q vector, G matrix and the h vector
	q = matrix(0.0, (len(data), 1))
	h = matrix(-1.0, (len(data), 1))
	G = numpy.identity(len(data)) * -1

	# Call qp
	r = qp(matrix(buildP(data)), q, matrix(G), matrix(h))
	alpha = list(r['x'])

	# Pick out the non-zero alpha values
	# We assume len(alpha) = len(data)!
	nonzeroAlpha = []
	for i in range(0, len(alpha)):
		if abs(alpha[i]) >= 0.00001:
			nonzeroAlpha.append((i, alpha[i]))
			
	return nonzeroAlpha

