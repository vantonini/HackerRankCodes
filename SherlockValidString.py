def isValid(s):
    frequencies = []
    freq_frequencies = []
    for letter in set(s):
        frequencies.append(s.count(letter))
    for freq in set(frequencies):
        freq_frequencies.append(frequencies.count(freq))
    if (len(freq_frequencies) > 2):
        return "NO"
    if (sum(frequencies) % len(frequencies) == 0):
        return "YES"
    if ((max(frequencies) - min(frequencies) > 1)):
        return "NO"
    if ((sum(frequencies) - (max(frequencies) - min(frequencies) ) ) % len(frequencies) == 0):
        return "YES"
    if ((sum(frequencies) + (max(frequencies) - min(frequencies) )) % len(frequencies) == 0):
        return "YES"
    return "NO"

input = "xxxaabbccrry"

isValid(input)
