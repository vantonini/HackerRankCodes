
# better solution
def rotLeft(a, d):
b = []
newIdx = 0
for idx in range(len(a)):
    newIdx = (idx + d + len(a)) % len(a)
    # print(idx, newIdx)
    b.append(a[newIdx])
return b

# def rotLeft(a, d):
#     b = a[:]
#     newInd = 0
#     for idx, num in enumerate(a):
#         if (idx + d > len(a)-1):
#             newInd = (idx + d) - (len(a))
#         else:
#             newInd = idx + d
#         # print(idx, newInd)
#         b[idx] = a[newInd]
#     return b

nd = "15 13"
input = "33 47 70 37 8 53 13 93 71 72 51 100 60 87 97"

nd = nd.split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input.rstrip().split()))

rotLeft(a, d)