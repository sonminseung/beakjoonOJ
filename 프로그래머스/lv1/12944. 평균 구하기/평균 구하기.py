def solution(arr):
    if arr == 0:
        return 0
    else:
        result=sum(arr)
        result=result/len(arr)
        return result
print(solution(0))
