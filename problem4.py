a=[1,1,2,3,4,64,35,93,35,87,4,3]
b=set()
unique=[]
for i in a:
  if i not in b:
    unique.append(i)
    b.add(i)
print(unique)