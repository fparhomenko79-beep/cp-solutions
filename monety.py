def string_to_words_solution(s: str) -> list:
    arr = [""]
    for i in range(len(s)):
        if s[i] != " ":
            arr[-1] += s[i]
        else:
            arr.append("")
    return arr

def count_word_solution(s: str, target: str) -> int:
    arr = string_to_words_solution(s)
    count_of_target_word = 0
    for word in arr:
        if word == target:
            count_of_target_word += 1
    return count_of_target_word

