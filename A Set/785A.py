polyhedrons = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20,
}

n = int(input())
t = 0 
for i in range(n):
    t += polyhedrons[input()]
print(t)

# https://codeforces.com/problemset/problem/785/A