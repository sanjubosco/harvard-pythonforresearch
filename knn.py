import numpy as np
import time
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

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
    return (random.choice(winners),max_vote)

def majority_vote_scipy(votes):
    """ picks the most common element from the array using scipy module"""
    winner,count = ss.mstats.mode(votes)
    return(winner,count)

def find_k_nearest_neighbour(test_point,points,k=3):    
    distances = np.array([euclidean_distance(test_point,p) for p in points])
    sorted_indices = np.argsort(distances)
    return(sorted_indices[:k])

def knn_predict(test_point,points,outcomes,k):
    k_n_n = find_k_nearest_neighbour(test_point,points,k)
    print (k_n_n,type(k_n_n))
    return(majority_vote(outcomes[k_n_n]))

p1 = np.random.randn(2,3)
p2 = np.random.randn(2,3)

start = time.perf_counter_ns()
for a,b in zip(p1,p2):
    print (euclidean_distance(a,b))

end = time.perf_counter_ns()
print ("Time taken First = ", end-start)
outcomes = np.array([1,2,3,1,2,3,3,2,1])
points = np.random.randn(9,2)
p = [.023,0.572]
print (points)
plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1],"bo")
#plt.show()

print (knn_predict(p,points,outcomes,3))




