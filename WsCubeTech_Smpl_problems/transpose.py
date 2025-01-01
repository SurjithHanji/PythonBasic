#using for looop

a=[[1],[3],[5],
   [3],[4],[3]]

T=[[0],[0],
   [0],[0],
   [0],[0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        T[j][i]=a[i][j]

for i in T:
    print(i)

# using list comprehension

a=[[1],[3],[5],
   [3],[4],[3]]

T=[[a[j][i] for j in range(len(a[0]))]]
print(T)
