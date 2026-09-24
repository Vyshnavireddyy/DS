import numpy as np
from scipy.spatial import distance
pointA=np.array([2,4,6])
pointB=np.array([3,1,7])
md=distance.cityblock(pointA,pointB)
print("Manhattan distance : ",md)
sm=1/(1+md)
print("Euclidean similarity : ",sm)