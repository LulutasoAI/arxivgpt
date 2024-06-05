from utils import get_text, memorize, chat


def main():


    text = get_text("https://google.com")
    print(text)
    memory_path = memorize(text)
    chat(memory_path)

if __name__ == '__main__':
    main()

