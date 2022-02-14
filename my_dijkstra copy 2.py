# https://yxudong.github.io/Dijkstra-%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E7%AE%97%E6%B3%95-Python-%E5%AE%9E%E7%8E%B0/
def Dijkstra(G, start,end):
    start=start
    n = len(G)
    u = 0
    mark = [0] * n
    # visited = [0] * n
    dis = [float('inf')] * n
    # parents = [-1] * n 
    for i in range(n):
        dis[i] = G[start][i]
    mark[start]=1; 

    for K in range(n):
        min = inf

        for i in range(n):
            if mark[i]==0 and min<dis[i]:
                min = dis[i]
                u = i

        mark[u]=1

        for i in range(n):
            if mark[i] == 0 and dis[i] > dis[u] + G[u][i]:
                dis[i] = dis[i] + G[u][i]
    print("dis y is :",dis[end])
    return dis[end]

if __name__ == '__main__':
    inf = float('inf')
    # G = [[0, 1, 12, inf, inf, inf],
    #      [inf, 0, 9, 3, inf, inf],
    #      [inf, inf, 0, inf, 5, inf],
    #      [inf, inf, 4, 0, 13, 15],
    #      [inf, inf, inf, inf, 0, 4],
    #      [inf, inf, inf, inf, inf, 0]]

    G = [
        [0, 1, inf, inf, 1, inf, inf, 1, inf, inf, inf, inf, inf, inf, inf], 
        [1, 0, 1, inf, inf, inf, inf, 1, 1, inf, inf, inf, inf,inf, inf], 
        [inf, 1, 0, 1, inf, inf, inf, inf, 1, 1, inf, inf, inf, inf, inf], 
        [inf, inf, 1, 0, inf, inf, inf, inf, inf, 1, 1,inf, inf, inf, inf], 
        [1, inf, inf, inf, 0, 1, inf, 1, inf, inf, inf, inf, inf, inf, inf], 
        [inf, inf, inf, inf, 1, 0, 1, 1, inf, inf, inf, inf, inf, inf, inf], 
        [inf, inf, inf, inf, inf, 1, 0, inf, inf, inf, inf, inf, inf, inf, inf], 
        [1, 1, inf, inf, 1,1, inf, 0, 1, inf, inf, inf, inf, inf, inf], 
        [inf, 1, 1, inf, inf, inf, inf, 1, 0, 1, inf, inf, inf, inf, inf], 
        [inf, inf, 1,1, inf, inf, inf, inf, 1, 0, 1, inf, inf, inf, inf], 
        [inf, inf, inf, 1, inf, inf, inf, inf, inf, 1, 0, inf, inf, inf, inf], 
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 1, inf, inf], 
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1, 0, 1, inf], 
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1, 0, 1], 
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1, 0]
        ]
    distance = Dijkstra(G,0,5)
    print("dis: ", distance)
    # print("parents: ", parents)


