m=[0,1,2,3,4,5]
print(len(m)-1)
for i in range(0,len(m)-1,2):
    print(m[i])

n=[0,1,1,0,1,0]
print(''.join(str(n[l]) for l in range(2)))

# print(int(''.join(n[0:2])),2)