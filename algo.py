def getAdjMatrix(path):
    edge = []
    pointNum = 0
    with open(path, 'r') as fp:
        for line in fp.readlines():
            if line.startswith('p'):
                pointNum = int(line.split()[2])
                for i in range(pointNum):
                    edge.append([0 for i in range(pointNum)])
            if line.startswith('e') and pointNum > 0:
                edge[int(line.split()[1]) - 1][int(line.split()[2]) - 1] = 1
                edge[int(line.split()[2]) - 1][int(line.split()[1]) - 1] = 1
    return edge, pointNum

def main():
    edge, pointNum = getAdjMatrix(r'test.txt')
    colorNum = 0
    disabled = []
    color = []
    for i in range(pointNum):
        color.append(0)
    edgeNum = [sum(e) for e in edge]
    for k in range(pointNum):
        maxEdgePoint = [i for i in range(pointNum) if edgeNum[i] == max(edgeNum) and edgeNum[i] != 0]
        for p in maxEdgePoint:
            if p not in disabled:
                color[p] = colorNum + 1
                disabled.append(p)
                edgeNum[p] = 0
                temp = edge[p]
                for i in range(pointNum):
                    if i not in disabled:
                      if temp[i] == 0:
                            color[i] = colorNum + 1
                            disabled.append(i)
                            edgeNum[i] = 0
                            temp = [x + y for (x, y) in zip(edge[i], temp)]
                colorNum = colorNum + 1
        if 0 not in color:
            break
    print(str(colorNum))

main()
