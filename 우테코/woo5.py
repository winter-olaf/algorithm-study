def solution(penter, pexit, pescape, data):
    result = []
    result.append(penter)
    for i in range(len(data)//len(penter)):
        split = data[i * len(penter): i * len(penter) + len(penter)]
        if split in [penter, pexit, pescape]:
            result.append(pescape)
            result.append(split)
        else:
            result.append(split)
    result.append(pexit)
    return ("".join(result))
res = solution("1100", "0010", "1001", "1101100100101111001111000000")
if (res == "110011011001100110010010111100111001110000000010"):
    print("correct!")
print(solution("1100", "0010", "1001", "1101100100101111001111000000"))