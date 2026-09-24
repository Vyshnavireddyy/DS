import numpy as np
from scipy.spatial import distance
pointA=np.array([2,4,6])
pointB=np.array([3,1,7])
md3=distance.minkowski(pointA,pointB,p=2)
print("Minkowski distance (p=3) : ",md3)
m=1/(1+md3)
print("Minkowski similarity : ",m)
