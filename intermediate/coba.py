def filter(l,fc):
    n=[]
    for i in l:
        if fc(i):
            n.append(i)
    return n
def map(l,fc):
    for i in range(len(l)):
        l[i]=fc(l[i])
    return l

a=[2,4,7,5,1,8,5, 3]
b=list(map(a, lambda x:x*6+9-3/2*10))
print(a, b)


# b=filter(a,
#     lambda x:x>3
# )

# print(b)

