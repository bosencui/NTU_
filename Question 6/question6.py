def isRayIntersectsSegment(poi,s_poi,e_poi): #[x,y] [lng,lat]
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1]==e_poi[1]: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #线段在射线上边
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #线段在射线下边
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #交点为下端点，对应spoint
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #交点为下端点，对应epoint
        return False
    if s_poi[0]<poi[0] and e_poi[1]<poi[1]: #线段在射线左边
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #求交
    if xseg<poi[0]: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后

def isPoiWithinPoly(poi,poly):
    #输入：点，多边形三维数组
    #poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

    #可以先判断点是否在外包矩形内 
    #if not isPoiWithinBox(poi,mbr=[[0,0],[180,90]]): return False
    #但算最小外包矩形本身需要循环边，会造成开销，本处略去
    sinsc=0 #交点个数
    #for epoly in poly: #循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
    for i in range(len(poly)-1): #[0,len-1]
        s_poi=poly[i]
        e_poi=poly[i+1]
        if isRayIntersectsSegment(poi,s_poi,e_poi):
            sinsc+=1 #有交点就加1

    return True if sinsc%2==1 else  False

points = []
with open('input_question_6_points', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.strip().split()
        if len(temp) < 1:
            continue
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        points.append(temp)
    
polygon = []
with open('input_question_6_polygon', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.strip().split()
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        polygon.append(temp)

with open('output_question_6', 'w', encoding = 'utf-8') as f:
    string = ''
    for point in points:
        result = isPoiWithinPoly(point, polygon)
        #string += str(point[0]) + ' ' + str(point[1]) + ' ' + str(result) + '\n'
        string += '{} {} {}\n'.format(point[0], point[1], result)
    f.write(string)

