# GVE
# G-> Graphs
# V->vertices
# E-set of Edges

# g =(v,e)

# v = ['A','B','C','D']

# E = [(A,B),(B,C),(C,D),(A,C),(A,D),()]


# Edge List -> Krushkal Algorithm

# A->B
# C->D
# 4

# E = n(n-1)/2
#   4(4-1)/2->6


graph = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["A"],
    "D":["B"]
}

print(graph)

graph["E"] = []

graph["C"].append("E")
graph["E"].append("C")
print(graph)

graph["A"].remove("B")
print(graph)


for i in graph:
    if 'E' in graph[i]:
        graph[i].remove("E")

print(graph)

del graph["E"]
print(graph)

print("A" in graph)


# Adjacent Matrix
    # A   B    C    D   E
# A  0    1    0    1   1
# B   1    0    1   0   1
# C
# D
# E


arr = ["A","B","C","D","E"]

matrix = [
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,1,0,0,0],
    [1,0,0,0,1],
    [1,1,0,1,0]
]

for row in matrix:
    print(row)


# Network
