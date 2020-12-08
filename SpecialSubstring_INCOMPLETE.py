def substrCount(n, s):
    total_count = len(s)
    for i in range(2,len(s)):
        # if it's odd, check removing middle letter
        substring = s[0:i]
        # removing each letter from a substring and trying to find repeated letter in sequence
        for letter in set(substring): # something wrong here
            new_string = substring.replace(letter,"")
            print(new_string)
            # for l in range(len(new_string)-1): 
            #     if(new_string[l] == new_string[l+1]):
            #         print(new_string)
            #         total_count+=1
        # if it's even, check if there is repetition
        else:
            total_count += s.count(substring) - 1
            print(i, s, substring, s.count(substring) - 1)
    return total_count


# tests
input = "abcbaba"
count1 = 0

len_input = len(input)
print(input)
if ((len_input % 2) == 0):
    input[:len_input] == input[len_input:]
    print(input[:len_input],input[len_input:])
else:
    input[:len_input] == input[len_input+1:]
    print(input[:int(len_input/2)],input[int(len_input/2)+1:])

# for letter in set(input):
#     new_string = input.replace(letter,"")
#     print(new_string)
#     # for i in range(len(new_string)-1):
#     #     if(new_string[i] == new_string[i+1]):
#     #         count1+=1
#     #         print(new_string)


#     print()

# input = "5 1 2 3 7 8 6 4"
# n = 10
input = "abcbaba"
n = len(input)

# input = "778 3330 152792, 442 1282 529876, 1653 3109 21175, 3116 3834 105877, 146 3595 406523, 379 561 938920, 243 1318 865056, 1991 3725 342448, 1301 3248 554541, 2465 3994 288890, 1295 2146 630019"
# n = 30000
# input = "2 1 5 3 4"
# input = "2 5 1 3 4"

# queries = []
# for _ in input.split(","):
#     queries.append(list(map(int,_.split())))

substrCount(n, input)