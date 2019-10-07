def cumsum_and_erase(A, erase=1):

    B = []
    sum = 0
    for item in A:
        sum += item
        if sum == erase:
            continue
        else:
            B.append(sum)
    print(B)
    return B


def Test():
    # в последнем тесте и результате небольшая правка
    tests = [[[1, 2, 3, 4, 5, 6], 1], [[4, 2, 5, 1, 3, 2], 5], [[3, 3, 3, 3, 3, 0], 15]]
    result_test = [[3, 6, 10, 15, 21], [4, 6, 11, 12, 15, 17], [3, 6, 9, 12]]
    result = True
    for i in range(len(tests)):
        result = result and (cumsum_and_erase(tests[i][0], tests[i][1]) == result_test[i])
    if result:
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в решении!")
    # проверка на значение erase по умолчанию
    result = result and (cumsum_and_erase(tests[0][0]) == result_test[0])
    if result:
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в решении!")

Test()