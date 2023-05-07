m={
    "Tetrahedron":4,
    "Cube":6,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20
}
t=int(input())
ans=0
while(t!=0):
    ans+=m[input()]
    t-=1

print(ans)