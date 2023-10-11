#INTRO TO IT 2nd COURSE
# Задача 3: Четное или нечетное?
# Попробуй определить, является ли введенное число четным или нечетным.
def chet_or_no(number):
    return "Четное" if number % 2 == 0 else "Нечетное"
number = 5
print(f"{number} - {chet_or_no(number)}")
