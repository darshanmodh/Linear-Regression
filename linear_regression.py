import numpy as np 
import random

def generatePoints(n):
	X = []
	Y = []
	for i in xrange(n):
		x1 = random.uniform(-100, 100)
		x2 = random.uniform(-100, 100)
		output = classify(x1, x2)
		vector = np.array([x1, x2])
		X.append(vector)
		Y.append(output)
		print "%s = %s" % (str(vector), str(output))
	return np.array(X), np.array(Y)


def train(X, Y):
	pseudo_inv = np.linalg.pinv(X)
	return pseudo_inv.dot(Y)

def classify(x1, x2):
		x1_line = (x2 - intercept) / float(slope)
		if x1 > x1_line:
		    return 1
		elif x1 < x1_line:
		    return -1
		else:
		    return 0

def generateLine():
	x_1, y_1 = random.uniform(-100, 100) , random.uniform(-100, 100)
	x_2, y_2 = random.uniform(-100, 100) , random.uniform(-100, 100)
	a = np.array([[x_1, 1], [x_2, 1]])
	b = np.array([y_1, y_2])
	soln = np.linalg.solve(a, b)
	return soln

line = generateLine()
slope, intercept = line[0], line[1]

X, Y = generatePoints(20)
print "Weight : ", train(X, Y)