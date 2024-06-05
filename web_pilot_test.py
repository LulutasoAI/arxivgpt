from webpilotcores.utils import WordInformationHandler
from gpt_handler.key import secret_key

def main():

    web_pilot = WordInformationHandler(secret_key)

    text = web_pilot.get_text("https://google.com")
    print(text)
    memory_path = web_pilot.memorize(text)
    web_pilot.chat(memory_path)

if __name__ == '__main__':
    main()

