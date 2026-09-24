import numpy as np
from scipy.spatial import distance
pointA=np.array([2,4,6])
pointB=np.array([3,1,7])
ed=distance.euclidean(pointA,pointB)
print("Euclidean distance : ",ed)
se=1/(1+ed)
print("Euclidean similarity : ",se)