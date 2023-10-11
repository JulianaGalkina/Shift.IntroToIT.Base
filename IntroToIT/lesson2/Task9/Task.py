#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def it_palindrom(s_name):
    return s_name == s_name[::-1]
s = "радар"
print(f"Является ли '{s}' палиндромом? {it_palindrom(s)}")
