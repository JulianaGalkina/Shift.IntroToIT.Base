#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def count_w(str):
    return len(str.split())
s = "Python прекрасен!"
print(f"В '{s}' {count_w(s)} слов")
