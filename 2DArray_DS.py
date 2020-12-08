def hourglassSum(arr):
    total_hour_glass_sum = []
    for y in range(len(arr[0]) - 2):
        for x in range(len(arr[0]) - 2):
            total_hour_glass_sum.append(sum(arr[x][y:y+3]) + arr[x+1][y + 1] + sum(arr[x+2][y:y+3]))
    
    return max(total_hour_glass_sum)
# helper
def printArray(arr):
    for x in range(6):
        for y in range(6):
            print(arr[x][y], end=" ")
        print()


input = "1 1 1 0 0 0, 0 1 0 0 0 0, 1 1 1 0 0 0, 0 0 2 4 4 0, 0 0 0 2 0 0, 0 0 1 2 4 0"
arr = []

for _ in range(6):
    arr.append(list(map(int,input.rstrip().split(",")[_].split())))

hourglassSum(arr)