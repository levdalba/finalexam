def solution(word):
    str = len(word)
    ans = ""
    if str % 2 == 0:
        ans += word[str//2-1]
    ans += word[str//2]
    return ans


str_mid = input("Write string here: ")
print(solution(str_mid))
