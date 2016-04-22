
namespaces = {'global': 'None'}
variables = {}
variables['global'] = []
command=[]

def read():
    n = int(input())
    global command
    for i in range(n):
        command.append(input().split())

def processed():
    global command
    for c in command:
        if c[0] == 'create': 
            create_namespace(c[1], c[2])
        if c[0] == 'add': 
            add_var(c[1], c[2])
        if c[0] == 'get': 
            print(get(c[1], c[2]))


def create_namespace(name, parent):
    namespaces[name]=parent
    variables[name]=[]

def add_var(namespace, name):
    variables[namespace].append(name)

def get (space, var):
    current_space = space
    if var in variables[current_space]: 
        return current_space
    else:
        current_space = namespaces[current_space]
        if current_space is 'None':
            return 'None'
        else:
            return get(current_space,var)


read()
processed()


# namespaces = {'global': 'None', 'foo': 'global', 'bar': 'foo'}
# variables = {'global': ['a'], 'foo': ['b'], 'bar': ['a', 'c', 'd']}