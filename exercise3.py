import numpy as np

known_points = [(1,2),(4,5),(10,8),(2,1),(7,3)]
new_point = (3,3)

def euclidean_distance(point,new_point):

    return((point[0]-new_point[0])**2+(point[1]-new_point[1])**2)**.5

def closest(known_points,new_point):
    
    min_distance = np.inf
    
    for point in known_points:
    
        distance = euclidean_distance(point,new_point)
    
        if(distance<min_distance):
    
            min_distance = distance
            index = known_points.index(point)
    
    return(min_distance,index)

ans = closest(known_points,new_point)

print('point: '+str(known_points[ans[1]])+', distance: '+str(ans[0]))