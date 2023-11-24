import random
    


print("\x1bc\x1b[43;30m")


for q in range(3):
    l=list(range(50))
    for m in range(4):
        t=[]
        for n in range(10):
            t=t+[int(l.pop(random.randint(1,len(l)-1)))]
        t.sort()
        print(t)