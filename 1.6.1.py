
rules={}

def read():
    n = int(input())
    global rules
    for i in range(n):
        r = input().split(':')
        if len(r) > 1:
            rules[str.rstrip(r[0])] = r[1].split()
        else:
            rules[r[0]] = []


