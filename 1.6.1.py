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

def is_parent(parent, child):
    print('Looking for ', parent,' is parent of ',child)
    print('Strict parents of ',child,' are : ', rules[child])
    if rules[child]==[]: 
        print('empty array for rules[child] = ', rules[child])
        return 'No'
    if parent == child: 
        print('parent is child')
        return 'Yes'
    elif parent in rules[child]:
        print('parent', parent, ' is in ', rules[child])
        return 'Yes'
    else:
        print('enter the recursia')
        for p in rules[child]:
            print(' check is parent for child = ', p , ' ,parent = ', parent)
            is_parent(parent, p)

def process():
    read()
    for r in requests:
        print( is_parent(r[0], r[1]) )

process()
3
A
B : A
C : B
1
A C