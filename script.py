m=[0,1,2,3,4,5]
print(len(m)-1)
for i in range(0,len(m)-1,2):
    print(m[i])


print("---")
n=[0,1,0,0,1,0,1]
ge=[2,4,7]
c = []
for k in range(len(ge)):
    c.append(''.join(str(n[l]) for l in range(ge[k-1],ge[k])))
c[0]=''.join(str(n[l]) for l in range(ge[0]))
print(c)


