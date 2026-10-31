from cities import cities_list


def load_cities(cities_list: list[dict]) -> set[str]:
    """
    Создает множество названий городов из списка словарей.

    Args:
        cities_list: Список словарей с информацией о городах.

    Returns:
        Множество названий городов в нижнем регистре.
    """
    cities_set = {city["name"].lower() for city in cities_list}
    return cities_set


def check_city_rules(city1: str, city2: str) -> bool:
    """
    Проверяет, соблюдается ли правило игры 'Города' между двумя городами.

    Args:
        city1: Первый город.
        city2: Второй город.

    Returns:
        True, если правило соблюдено, иначе False.
    """
    return city1[-1].lower() == city2[0].lower()


def find_computer_city(available_cities: set[str], letter: str) -> str | None:
    """
    Ищет город для компьютера, начинающийся на заданную букву.

    Args:
        available_cities: Множество доступных городов.
        letter: Буква, на которую должен начинаться город.

    Returns:
        Название города, если найден, иначе None.
    """
    for city in available_cities:
        if city[0] == letter:
            return city
    return None


def main() -> None:
    """
    Точка входа. Управляет ходом игры.
    """
    cities_set = load_cities(cities_list)
    print(f"Мы подключили датасет на {len(cities_set)} городов")

    cities_dict = {city["name"].lower(): city["name"] for city in cities_list}
    computer_city = None

    while True:
        user_input = input("Введите название города: ").strip().lower()

        if user_input == "стоп":
            print("Игра завершена.")
            break

        if user_input not in cities_set:
            print("Кожаный мешок, ты проиграл. Такого города нет или он уже был.")
            break

        if computer_city:
            if not check_city_rules(computer_city.lower(), user_input):
                print("Кожаный мешок, ты проиграл. Ты нарушил правила игры.")
                break

        cities_set.remove(user_input)

        last_letter = user_input[-1]
        computer_choice = find_computer_city(cities_set, last_letter)

        if computer_choice is None:
            print("Кожаный мешок, ты выиграл!")
            break

        computer_city = cities_dict[computer_choice]
        print(f"Компьютер выбрал город: {computer_city}")
        cities_set.remove(computer_choice)


main()
