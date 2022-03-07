def solution(n, arr1, arr2):
    answer = [ ''.join([ '0' ] * n) ] * n
    binArr1 = list(map(lambda binNum: binNum[2:].zfill(n), list(map(bin, arr1))))
    binArr2 = list(map(lambda binNum: binNum[2:].zfill(n), list(map(bin, arr2))))

    for i in range(0, n):
        for j in range(0, n):
            if binArr1[i][j] == '1' or binArr2[i][j] == '1':
                curStrList = list(answer[i])
                curStrList[j] = '#'
                answer[i] = ''.join(curStrList)

    return list(map(lambda item: item.replace('0', ' '), answer))