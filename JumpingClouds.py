def jumpingOnClouds(c):
    steps = 0
    i = 2
    while(i <= (len(c) -1)):
        if (c[i] == 1):
            steps += 2
            i +=1
        else:
            steps += 1
        i += 2
    if i == len(c):
        steps += 1
    return steps

# input = "0 0 0 1 0 0"
input = "0 0 1 0 0 1 0"
c = list(map(int, input.rstrip().split()))

jumpingOnClouds(c)
