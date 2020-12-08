
string = "isa"
string[0] + string[::-1][1:-1] + string[-1]


n = 4
for j in range(n):
    print(" "*j, end=" ")
    for i in range(n):
        print('*', end=" ")
    print()



n = 4
for j in range(n):
    for i in range(n):
        if (j in [0, n-1]):
            print('*', end=" ")
        else:
            if (i in [0, n-1]):
                print('*', end=" ")
            else:
                print(' ', end=" ")
    print()
        