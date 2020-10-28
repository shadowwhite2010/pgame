li=[1, 2, 0, 0,  5, 0, 9, 6]
def ll(li):
    for i in range(len(li)):
        if li[i]==2:
            print(li[i])
            li[i]=0
while 0 in li:
    li.remove(0)
ll(li)


print(li)