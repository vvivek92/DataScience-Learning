# simple demo for CLT

import random
from math import sqrt

import seaborn as sns
sns.set(color_codes=True)

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))

def sample(N):
    return


def flip(N):
    return [ 0 if random.random() < 0.5 else 1   for i in range(0,1000)      ]

# the sample size is set to the number of samples
def sampleDistribution(N):
    return [ mean(flip(N)) for i in range(N)]

N=1000
f=flip(N)

print mean(f)
print stddev(f)

sns.distplot(sampleDistribution(N))