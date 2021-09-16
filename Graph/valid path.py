from astroid import List


def validPath(n: int, edges: List[List[int]], start: int, end: int) -> bool:
    flag = False
    for i in edges:
        if edges[i][0] == start:
            start = edges[i][1]
            if edges[i][1] == end:
                flag = True
            break
    return flag

n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2

validPath(n,edges,start,end)