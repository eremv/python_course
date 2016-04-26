rules={}
requests=[]

def read():
    n = int(input())
    global rules
    for i in range(n):
        r = input().split(':')
        if len(r) > 1:
            rules[str.rstrip(r[0])] = r[1].split()
        else:
            rules[r[0]] = []
    n = int(input())
    global requests
    for i in range(n):
        st = input().split()
        requests.append(st)


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def process():
    read()
    for r in requests:
        res = find_path(rules, r[1], r[0])
        if find_path(rules, r[1], r[0]) == None :
            print('No')
        else:
            print('Yes')

process()
10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
38
classK classD
classD classA
classG classD
classH classA
classE classE
classH classG
classE classL
classB classD
classD classL
classD classG
classD classE
classA classF
classA classC
classK classA
classA classH
classK classD
classH classB
classK classB
classD classL
classG classG
classA classH
classK classL
classG classE
classB classA
classC classK
classK classL
classC classL
classG classC
classD classD
classC classG
classE classA
classF classK
classB classG
classH classL
classL classF
classH classG
classD classA
classH classL