src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
answer = []
for i in range(len(src)):
    for j in range(len(src)):
        if i != j and src[i] == src[j]:
            break
    else:
        answer.append(src[i])

print(answer, end=' ')
