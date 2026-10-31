import json
from openai import OpenAI
from openai.types.chat import ChatCompletion


def read_config(path:str)->dict:
    """ Функция читает JSON-файл конфигурации
        и возрощает ошибки 
        path путь к файлу конфигурации
    """
    try:

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Файл конфигурации не найден: {path}")
        raise
    except json.JSONDecodeError:
        print("Конфиг повреждён — это не валидный JSON.")
        raise

def create_client(config:dict)->OpenAI:
    """Функция берет ключи API_KEY и BASE_URL из файла config
    Создает client и возращает его 
    """

    BASE_URL = config["baseURL"]
    API_KEY = config["api_key"]
    

    client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    )


    return client

def send_request(client: OpenAI, model:str, message:str)->ChatCompletion:
    """Функция принимает готовый client, название model и текст message (промпт), отправлять запрос 
    к API и возвращать сырой объект ответа от нейросети. """

    completion = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": message
        }]
        )
    return completion


def extract_answer(completion: ChatCompletion) -> str:
    """достаёт текст ответа из объекта завершения."""

    return completion.choices[0].message.content

def get_user_prompt(default: str)->str:

    """Функция принимает ввод пользователя user_input
    Проверяет на наличие пусой строки
    Возвращает ввод
    """

    user_input = input("Введите ваш запрос: ")

    if user_input.strip() == "":
        return default 

    return user_input

def save_answer(prompt: str, answer: str, filepath:str, separator:str)->None:
    """дописывает блок с промптом и ответом в текстовый файл."""

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(f"ПРОМПТ:\n{prompt}\n{separator}\n")
        file.write(f"ОТВЕТ:\n{answer}\n{separator}\n")
        file.write("\n")




            

   

   

    





