def dist(p1, p2):
    """Computes Eucledian distance between points p1 and p2.
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[0]
    
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def offices_to_merge(points):
    """
    Input : list of 2d coordinates of post offices,
            points=[(x1, y1), (x2, y2)...(xn, yn)]} with n>1
    Output: a pair of indices (l, k) such that...
            for all pairs of indices 0 <= i < j <=n it holds that
            dist(points[l], points[k]) <= dist(points[i], points[j])
    
    For example:
    >>> points = [(350, 150), (500, 250), (150, 150), (50, 400), (200,100)]
    >>> offices_to_merge(points)
    (2, 4)
    """
    distance = []
    
    for i in range(len(points)-1):
        
        for j in range(i+1, len(points)):
            
            distance.append( [ (i, j), dist(points[i], points[j]) ] )
    
 
           
    min_val = distance[0][1]

    
    min_position = 0
    
    for i in range(len(distance)):
        
        if distance[i][1] < min_val:
            min_val = distance[i][1]
            min_position = i
    
    
    res = distance[min_position][0]
    
    return res