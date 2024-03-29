def solution(n, edge):
    answer = 0

    nearNodeList = [[] for i in range(n)]

    for pair in edge:
        a,b = pair[0]-1, pair[1]-1
        nearNodeList[a].append(b)
        nearNodeList[b].append(a)


    totalVisit = set()
    currentVisit = set()
    nextVisit = set()
    currentVisit.add(0)

    while (True):

        totalVisit = totalVisit | currentVisit

        for parent in currentVisit:
            for node in nearNodeList[parent]:

                if (node in totalVisit):
                    continue

                nextVisit.add(node)

        if (len(totalVisit) + len(nextVisit) == n):
            break

        currentVisit = nextVisit
        nextVisit = set()


    answer = len(nextVisit)

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)