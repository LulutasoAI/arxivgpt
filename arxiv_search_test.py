import research_handler.arxiv_handler as arxiv_handler


def main():
    arxiv = arxiv_handler.ArxivHandler()
    query = "all:Ai trend, surveilance"
    print(query)
    
    text = arxiv.query_to_summaries(query)
    print(text)
    """
    summary = gpt_handler.call_GPT(text,gpt_handler.summary_mode)
    print(summary)
    summary_jp = gpt_handler.call_GPT(summary, gpt_handler.translation_mode)
    print(summary_jp)
    """
if __name__ == "__main__":
    main()