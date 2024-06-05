import research_handler.arxiv_handler as arxiv_handler
from gpt_handler.openai_functions import gptHandler
from wrapper import Wrapper


def main():
    wrapper = Wrapper()
    #wrapper.ask_input_and_generate_relevant_summary()
    #wrapper.ask_input_and_generate_answer_using_relevance_info()
    #wrapper.simplychat()
    result = wrapper.arxiv_research_using_langchaing()
    print(result)
    """
    arxiv = arxiv_handler.ArxivHandler()
    gpt_handler = gptHandler()
    user_input = str(input("調べたいことを入力してください。\n"))
    query = gpt_handler.call_GPT(user_input,gpt_handler.query_mode)
    print(query)
    #text = arxiv.query_to_text(query)
    
    text = arxiv.query_to_summaries(query)
    print(text)
    
    summary = gpt_handler.call_GPT(text,gpt_handler.summary_mode)
    print(summary)
    summary_jp = gpt_handler.call_GPT(summary, gpt_handler.translation_mode)
    print(summary_jp)
    """
if __name__ == "__main__":
    main()