from summarization_handler.summarization_handler import SummarizationHandler

if __name__ == "__main__":
    summarization_handler = SummarizationHandler(sentences_count=3)
    text = """強化学習の最近の研究について調べたい"""
    #text = summary_message
    summary = summarization_handler.summarize(text)
    print(summary)

    print(summarization_handler.are_sentences_relevant("I'd like to utilize python library to summarize long texts.","Simple library and command line utility for extracting summary from HTML pages or plain texts. The package also contains simple evaluation framework for text summaries. Implemented summarization methods are described in the documentation. I also maintain a list of alternative implementations of the summarizers in various programming languages."))