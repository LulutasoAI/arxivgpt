from gpt_handler.openai_functions import gptHandler


if __name__ == "__main__":
    gpt_handler = gptHandler()
    query = gpt_handler.call_GPT("強化学習の最近の研究について調べたい",gpt_handler.query_mode)
    print(query)