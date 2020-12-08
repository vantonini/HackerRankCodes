def alternatingCharacters(s):
    count_deletion = 0
    for idx in range(len(s)-1):
        if (s[idx+1] == s[idx]):
            count_deletion += 1
    return count_deletion



input = "AAAA"
alternatingCharacters(input)
