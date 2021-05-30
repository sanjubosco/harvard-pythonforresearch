import numpy as np
import time
import random
import scipy.stats as ss

def euclidean_distance(p1,p2):
    """ to calculate euclidean distance using formula squareroot((x1-x2)^2 + (y1-y2)^2)"""
    return(np.linalg.norm(p1-p2))

def majority_vote(votes):
    """ picks the most common element from the array"""
    votes_count = dict()
    for vote in votes:
        if vote in votes_count:
            votes_count[vote] += 1
        else:
            votes_count[vote] = 1
    
    max_vote = max(votes_count.values())
    winners = [key for key,value in votes_count.items() if value == max_vote]
    print (votes_count)
    return (random.choice(winners))

def majority_vote_scipy(votes):
    """ picks the most common element from the array using scipy module"""
    winner,count = ss.mstats.mode(votes)
    return(winner,count)

p1 = np.random.randn(2,3)
p2 = np.random.randn(2,3)

start = time.perf_counter_ns()
for a,b in zip(p1,p2):
    print (euclidean_distance(a,b))

end = time.perf_counter_ns()
print ("Time taken First = ", end-start)
votes = [1,2,1,2,2,2,2,3,4,5,2,3,4,4,4,4,4,3,3,3,1,1,2,2,4,4]
print (majority_vote(votes))
print (majority_vote_scipy(votes))
