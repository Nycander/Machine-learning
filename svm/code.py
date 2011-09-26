from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math

# A suitable kernel function
def linearKernel(x, y):
	return x[0] * y[0] + x[1] * y[1] +1

def polynomialKernel(x, y):
	#print (x[0] * y[0] + x[1] * y[1] +1)**4
	return (x[0] * y[0] + x[1] * y[1] +1)**4

def RadKernel(x, y):
	sigma = 7
	#print math.exp((-((x[0] * y[0] + x[1] * y[1])**2))/2*sigma**(2))
	z = (x[0] -y[0], x[1] - y[1])
	return math.exp(-(z[0] * z[0] + z[1] * z[1])/2*sigma**(2))

def kernel(x, y):
	return linearKernel(x, y)
	return polynomialKernel(x, y)
	return RadKernel(x, y)
	
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

def calculateAlphas(trainingData):

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


# Generate data
#classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5,1),     1.0) for i in range(5) ] + \
#		 [(random.normalvariate( 1.5, 1), random.normalvariate(0.5,1),     1.0) for i in range(5) ]

#classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5,0.5), -1.0) for i in range(10)]

classA = [(random.normalvariate(0,3), random.normalvariate(0,0),  1.0) for i in range(10) ]
classB = [(random.normalvariate(0,3), random.normalvariate(0,0), -1.0) for i in range(10) ]


data = classA + classB
random.shuffle(data)

# Find contour
xRange = numpy.arange(-3, 3, 0.05)
yRange = numpy.arange(-3, 3, 0.05)

alphas = calculateAlphas(data)
grid = matrix([[indicator([x, y], data, alphas) for y in yRange] for x in xRange])

# Plot the data
pylab.hold(True)


# Plot contour between classifications
pylab.contour(xRange, yRange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths=(1, 2, 1))

# Plot all points
pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')

# Print alpha points
for alpha in alphas:
	pylab.plot(data[alpha[0]][0], data[alpha[0]][1], 'w+')
	
pylab.show()
