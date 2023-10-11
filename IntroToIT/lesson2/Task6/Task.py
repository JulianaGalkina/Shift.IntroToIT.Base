#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def count_gl(str):
    return sum(1 for a in str if a.lower() in "аеёиоуыэюя")
str1 = "Привет, мир!"
print(f"В '{str1}' {count_gl(str1)} гласных")
