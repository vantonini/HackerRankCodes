def minimumBribes(q):
    total_bribes = 0
    for idx, num in enumerate(q):
        if (num - (idx + 1) > 2):
            print("Too chaotic")
            return
        # if there is a greater value between 2 positions before the original one (num-2) and its actual position (idx),
        # it means that this number has been swapped
        # print(num, q[max(0,num-2):idx], sum(i > num for i in q[max(0,num-2):idx]))
        total_bribes += sum(i > num for i in q[max(0,num-2):idx])
    print(total_bribes)


    
# input = "5 1 2 3 7 8 6 4"
input = "1 2 5 3 7 8 6 4"

# input = "2 1 5 3 4"
# input = "2 5 1 3 4"

a = list(map(int, input.rstrip().split()))

minimumBribes(a)