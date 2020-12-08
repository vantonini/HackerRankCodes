def repeatedString(s, n):
    total = s.count("a") * int(n/len(s))
    total += s[:n % len(s)].count("a")
    return total

s = "aba"
n = 10
n = int(n)

repeatedString(s, n)
