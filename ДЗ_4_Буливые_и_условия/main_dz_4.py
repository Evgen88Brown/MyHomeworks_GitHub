check_mark = input("Введите бал от 1 до 12 для расчета оценки: ")
completion = "завершения"
if not check_mark.isdigit():
    print(" Введите число")
    input(f"Нажмите Enter для {completion}...")
    exit(1)

number = int(check_mark)

if 10 <= number <= 12:
    print("Ваша оценка 5")
elif 8 <= number <= 9:
    print("Ваша оценка 4")
elif 6 <= number <= 7:
    print("Ваша оценка 3")
elif 1 <= number <= 5:
    print("Ваша оценка 2")
else:
    print("Вы ввели число не в диопазоне от 1 до 12")


input(f"Нажмите Enter  для {completion}...")
exit(0)
