def main():
    A = []
    B = []

    for k in range(3):
        value = int(input("Enter values for Alice: "))
        value2 = int(input("Enter values for Bob: "))
        A.append(value)
        B.append(value2)

    print(compare_triplets(A, B))

def compare_triplets(a, b):
    scoreA = scoreB = 0
    result = []

    for i in range(len(a)):
        if a[i] > b[i]:
            scoreA += 1
        elif a[i] < b[i]:
            scoreB += 1
        elif a[i] == b[i]:
            scoreA += 0
            scoreB += 0

    result.append(scoreA)
    result.append(scoreB)

    return result

main()