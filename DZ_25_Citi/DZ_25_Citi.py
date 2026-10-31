from cities import cities_list

print(f"Мы подключили датасет на {len(cities_list)} городов")

# Словарь: название в нижнем регистре -> оигенильное название
cities_dict = {city["name"].lower(): city["name"] for city in cities_list}
cities_set = set(cities_dict.keys())

computer_city = None

while True:
    user_input = input("Введите название города: ").strip()
    user_cituy_lower = user_input.lower()

    # Проверка существования города
    if user_cituy_lower not in cities_set:
        print("Кожаный мешок, ты проиграл. Такого города нет или он уже был.")
        break

    # Если компьютер уже сделал ход, проверить правило
    if computer_city is not None:
        if computer_city[-1].lower() != user_cituy_lower[0]:
            print("Кожаный мешок, ты проиграл. Ты нарушил правила игры.")
            break

    # Удаляем город пользователя

    cities_set.remove(user_cituy_lower)

    # Ход компьютера: ищем город на последнюю букву
    last_letter = user_cituy_lower[-1]
    computer_choice = None
    for city_lower in cities_set:
        if city_lower[0] == last_letter:
            computer_choice = city_lower
            break

    if computer_choice is None:
        print("Кожаный мешок, ты выиграл!")
        break

    # Получаем оригинальное название для вывода
    computer_city = cities_dict[computer_choice]
    print(f"Компьютер выбрал город: {computer_city}")

    # Удаляем город компьютера
    cities_set.remove(computer_choice)


