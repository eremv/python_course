objects = [1,1,1,1,1]

for i in range(len(objects)):
    for j in range(i+1, len(objects)-1):
        if objects[i] is objects[j]:
            del objects[j];

print(len(objects))