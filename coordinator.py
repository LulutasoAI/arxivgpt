from gpt_handler.openai_functions import gptHandler
from research_handler.arxiv_handler import ArxivHandler
from summarization_handler.summarization_handler import SummarizationHandler

class Coordinator:
    def __init__(self) -> None:
        self.gpt_handler = gptHandler()
        self.arxiv_handler = ArxivHandler()
        self.summarization_handler = SummarizationHandler(sentences_count=8)
    
    def gather_input(self, question):
        user_input = str(input(question))
        return user_input
    
    def get_query(self, user_input):
        query = self.gpt_handler.call_GPT(user_input,self.gpt_handler.query_mode)
        return query
    
    def get_summaries_from_query(self, query):
        summaries = self.arxiv_handler.query_to_summaries(query)
        return summaries
    
    def get_summary_from_text(self, text, summarizer:str, sentences_count=None):
        if summarizer == "gpt":
            summary = self.gpt_handler.call_GPT(text,self.gpt_handler.summary_mode)
        elif summarizer == "summarization_handler":
            if sentences_count is None:
                sentences_count = self.summarization_handler.sentences_count
            summary = self.summarization_handler.summarize(text, sentences_count=sentences_count)
        return summary
    
    def translate_eng_to_jp(self, text):
        translated_text = self.gpt_handler.call_GPT(text, self.gpt_handler.translation_mode)
        return translated_text

    def user_input_to_results(self, user_input):
        query = self.get_query(user_input)
        print(query)
        results = self.arxiv_handler.query_to_results(query)
        return results
    
    def user_input_to_query(self,user_input):
        return self.get_query(user_input)
    def query_to_results(self,query):
        results = self.arxiv_handler.query_to_results(query)
        return results 
    
    def results_to_text(self, results):
        text = self.arxiv_handler.results_to_text(results)
        return text
    
    def result_to_text(self,result):
        text = self.arxiv_handler.result_to_text(result)
        return text

    def are_sentences_relevant(self, sentence1, sentence2):
        are_relevant = self.summarization_handler.are_sentences_relevant(sentence1, sentence2)
        return are_relevant
    
    

    

    


