#  361. Гвоздики

N = int(input())
l = sorted(list(map(int, input().split())))

if N == 2 or N == 3:
    print(l[-1] - l[0])
elif N==4:
    print(l[1]-l[0] + l[-1] - l[-2])
elif N==5:
    print(l[1]-l[0] + l[-1] - l[-2] + min(l[3]-l[2], l[2]-l[1]))
else:
    base = l[1] - l[0]
    j = 2
    pair1 = (base + l[j]-l[j-1], base + l[j+1]-l[j])
    pair2 = (min(pair1[1], pair1[0]+l[j+1]-l[j]), min(l[j+2]-l[j+1] + pair1[0], l[j+2]-l[j+1] + pair1[1]))

    while j < N-4:
        j+=1
        pair1 = pair2
        pair2 = (min(pair1[1], pair1[0]+l[j+1]-l[j]), min(l[j+2]-l[j+1] + pair1[0], l[j+2]-l[j+1] + pair1[1]))



    print(min(pair2) + l[-1]-l[-2])