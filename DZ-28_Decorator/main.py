from typing import Callable

def password_checker(func: Callable)-> Callable:
    def wrapper(password: str)->str:
      
        
        if len(password) < 8:
            return "Ваш пароль слишком короткий"

        if not any(char.isdigit() for char in password):
            return "В пороле нет цифр"

        if not any(char.isupper() for char in password):
            return "В пороле нет заглавной буквы"

        if not any(char.islower() for char in password):
            return "В пароле должна быть хотя бы одна строчная буква"

        user_pas = func(password)

        return user_pas

    return wrapper

@password_checker
def register_user(password: str)-> str:
    
    return "Успешная регистрация"


def password_validator(
        min_length: int = 8, 
        min_uppercase: int = 1,
        min_lowercase: int = 1,
        min_digits: int = 1,
        min_special_chars: int = 1
        )-> Callable:

    def decorator(func: Callable)->Callable:
        def wrapper(*args, **kwargs)->str:

            """
    Декоратор с параметрами для проверки пароля.
    Поднимает ValueError, если пароль не соответствует правилам.

    """
            password = args[0]
            # Проверка длины
            if len(password) < min_length:
                raise ValueError(f"Пароль слишком короткий: требуется минимум {min_length} символов, найдено {len(password)}")

            # Заглавные
            uppercase_count = sum(1 for c in password if c.isupper())
            if uppercase_count < min_uppercase:
                raise ValueError(f"Недостаточно заглавных букв: нужно минимум {min_uppercase}, найдено {uppercase_count}")
            
            # Строчные
            lowercase_count = sum(1 for l in password if l.islower())
            if lowercase_count < min_lowercase:
                raise ValueError("В пароле должна быть хотя бы одна строчная буква")

            # Цифры
            digits_count = sum(1 for s in password if s.isdigit())
            if digits_count < min_digits:
                raise ValueError("В пороле нет цифр")

            special_count = sum(1 for s in password if not s.isalnum())
            if special_count < min_special_chars:
                raise ValueError(f"Недостаточно специальных символов: нужно минимум {min_special_chars}, найдено {special_count}")

           

            return func(*args, **kwargs)

        return wrapper

    return decorator



            

                               
def username_validator(func: Callable)->Callable:
    def wrapper(*args, **kwargs)->str:
        """
    Декоратор для проверки имени пользователя:
    - имя не должно быть пустым (в том числе состоять только из пробелов);
    - в имени не должно быть пробелов.
    При нарушении правил поднимает ValueError.
    """
        username = args[0]

        if not username.strip():
            raise ValueError("Строка не должна быть пустой")

        if " " in username:
            raise ValueError("Имя не должно содержать пробелов")

        return func(*args, **kwargs)
    return wrapper

users = []

@username_validator
@password_validator(
    min_length=8,
    min_digits=1,
    min_uppercase=1,
    min_lowercase=1,
    min_special_chars=1
    )
def register_account(username: str, password: str)-> str:
    """
    Основная функция регистрации аккаунта.
    Проверяется имя (username_validator) и пароль (password_validator).
    При успехе добавляет пользователя в список users и возвращает сообщение.
    """
    users.append({"username": username,"password": password })
    return "Пользователь зарегестрирован"

if __name__ == "__main__":
    test_cases = [
        
        ("", "ValidPass123!", "Пустое имя"),
        ("   ", "ValidPass123!", "Имя из одних пробелов"),
        ("ivan petrov", "ValidPass123!", "Имя с пробелом"),
        ("ivan", "Short1!", "Слишком короткий пароль"),
        ("ivan", "nouppercase123!", "Нет заглавной буквы"),
        ("ivan", "NOPASSWORD123!", "Нет строчной буквы"),
        ("ivan", "NoDigitsHere!", "Нет цифр"),
        ("ivan", "ValidPass1!", "Пароль без спецсимвола (если min_special_chars=1)"),
        ("ivan", "ValidPass123!", "Корректная регистрация"),
        ("alex", "StrongPass99!", "Ещё одна корректная регистрация"),
    ]

    for username, password, description in test_cases:
        print(f"Тест: {description}")
        try:
            result = register_account(username, password)
            print(f"  → {result}")
        except ValueError as e:
            print(f"  → Ошибка: {e}")
        print()  # пустая строка для читаемости

    print("Итоговый список пользователей:")
    for user in users:
        print("  -", user)



