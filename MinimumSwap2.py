def minimumSwaps(arr):
    idx = 0
    num_swap = 0
    while((len(arr) - idx) > 0):
        print(arr[idx])
        if(arr[idx] != idx+1):
            temp = arr[arr[idx]-1]
            arr[arr[idx]-1] = arr[idx]
            arr[idx] = temp
            num_swap += 1
        else:
            idx += 1   
    return num_swap



# input = "5 1 2 3 7 8 6 4"
input = "4 3 1 2"

# input = "2 1 5 3 4"
# input = "2 5 1 3 4"

a = list(map(int, input.rstrip().split()))

minimumSwaps2(a)