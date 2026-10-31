from utils import read_config, create_client, send_request, extract_answer, get_user_prompt, save_answer

CONFIG_FILE = "./config.json"
ANSWERS_FILE = "./answers.txt"
DEFAULT_MESSAGE = "Привет"
SEPARATOR = "=" * 60

def main()->None:
    try:
        config = read_config(CONFIG_FILE)
        client = create_client(config)
        prompt = get_user_prompt(DEFAULT_MESSAGE)
        completion = send_request(client, config["model"], prompt)
        answer = extract_answer(completion)
        print(answer)
        save_answer(prompt, answer, ANSWERS_FILE, SEPARATOR)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

