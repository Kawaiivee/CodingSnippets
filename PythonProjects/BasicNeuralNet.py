#!/usr/bin/env python3

import numpy as np

#took code from here
#https://iamtrask.github.io/2015/07/12/basic-python-network/
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1], [0,1,1], [1,0,1], [1,1,1]  ])

# output dataset
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic to analyze easier set of results
#np.random.seed(2)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1
print("Synapse 0 is:\n")
print(syn0)

generations = 100
for iter in range(generations):
# forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
# how much did we miss by?
    l1_error = y - l1
# multiply how much w  e missed by the
# slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)
# update weights
    syn0 += np.dot(l0.T,l1_delta)
    #print(l1)

print("Output After Training with", generations, "generations:")
print(l1)
