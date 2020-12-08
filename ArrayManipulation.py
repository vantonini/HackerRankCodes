def arrayManipulation(n, queries):
    # arr = [0] * n
    arr = []
    for query in queries:
        array1 = [0] * (query[0]-1)
        array2 = [query[2]] * (query[1]-(query[0]-1))
        array3 = [0] * (n-(query[1]))
        array_sum = array1 + array2 + array3
        arr.append(array_sum)
        if (len(arr) > 1):
            arr = [[sum([row[i] for row in arr]) for i in range(n)]]
    print(max(arr[0]))
        # print([sum([row[i] for row in arr]) for i in range(n)])

    # return max([sum([row[i] for row in arr]) for i in range(n)])


## better score
def arrayManipulation2(n, queries):
    arr = [0] * n
    for query in queries:
        for idx in range(query[0]-1, query[1]):
            arr[idx] += query[2]
    return max(arr)



input = "1 5 3, 4 8 7, 6 9 1, 10 10 11"
n = 10

# input = "778 3330 152792, 442 1282 529876, 1653 3109 21175, 3116 3834 105877, 146 3595 406523, 379 561 938920, 243 1318 865056, 1991 3725 342448, 1301 3248 554541, 2465 3994 288890, 1295 2146 630019"
# n = 30000
# input = "2 1 5 3 4"
# input = "2 5 1 3 4"

queries = []
for _ in input.split(","):
    queries.append(list(map(int,_.split())))

arrayManipulation(n, queries)