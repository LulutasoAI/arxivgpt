from coordinator import Coordinator
import sys
from webpilotcores.utils import WordInformationHandler
from gpt_handler.key import secret_key
from langchain_utils.ai_wrapper import AIWrapper
from word_processing_utils.utils import WordProcessing
from internet_handler.internet_handler import gather_info
import time
class Wrapper:
    def __init__(self) -> None:
        self.coordinator = Coordinator()
        self.word_information_handler = WordInformationHandler(secret_key)
        self.ai_wrapper = AIWrapper(secret_key)
        self.word_processor = WordProcessing()
        self.search_query = ""
        self.query = ""

    def ask_input_and_generate_relevant_summary(self,):
        user_input = self.coordinator.gather_input("調べたいことを入力してください。\n ")
        self.query = user_input
        #results = self.coordinator.user_input_to_results(user_input)
        self.search_query = self.coordinator.get_query(user_input)
        results = self.coordinator.query_to_results(self.search_query)
        relevant_summary = ""
        for result in results:
            if self.coordinator.are_sentences_relevant(user_input, result.summary):
                retrieved_text = self.coordinator.result_to_text(result)
                txt_length = len(retrieved_text)
                separate = int(txt_length*0.3)
                relevant_summary += self.coordinator.get_summary_from_text(retrieved_text[:separate], "summarization_handler")

        print(relevant_summary)
        print("_"*35)
        if relevant_summary == "":
            print("関連性の高い論文が見つかりませんでした。")
            return ""
        """
        relevant_summary = self.coordinator.get_summary_from_text(relevant_summary,"summarization_handler",sentences_count=5)

        print(relevant_summary)
        relevant_summary = self.coordinator.get_summary_from_text(relevant_summary,"summarization_handler",sentences_count=5)
        relevant_summary = self.coordinator.get_summary_from_text(relevant_summary,"summarization_handler",sentences_count=5)
        relevant_summary = self.coordinator.get_summary_from_text(relevant_summary,"summarization_handler",sentences_count=5)

        #relevant_summary = self.coordinator.translate_eng_to_jp(relevant_summary)
        print("_"*35)
        """
        #print(relevant_summary)
        return relevant_summary
    
    def arxiv_research_using_langchaing(self):
        relevant_summary = self.ask_input_and_generate_relevant_summary()
        
        chunk_size = 500
        chunks = self.word_processor.chunk_text(relevant_summary, chunk_size)
        for chunk in chunks:
            self.ai_wrapper.memorize_search_result(self.search_query, chunk)
        #time.sleep(3)
        print(self.query, "testing it2")
        internet_query = self.search_query.replace("all:","").lower()
        internet_info = gather_info(internet_query)
        #time.sleep(3)
        print(internet_info,"a",self.query)
        if(internet_info=="" and relevant_summary==""):
            print("関連情報の取得に失敗しました。Internet_query:",internet_query, ", Search query arxiv :", self.search_query, "\n")
            sys.exit()
        chunks = self.word_processor.chunk_text(internet_info, chunk_size)
        for chunk in chunks:
            self.ai_wrapper.memorize_search_result(internet_query, chunk)
        #print(chunk)
        result = self.ai_wrapper.converse(self.query)
        print("\n searched:", self.search_query, "user:", self.query, "internet_query:", internet_query,"\n")
        #print(chunk)
        user_input = ""
        while True:
            print(result)
            user_input = str(input("What would you like to ask further? input end to end.\n"))
            if user_input == "end":
                break
            else:
                result = self.ai_wrapper.converse(user_input)
                #print(result)
        return result 
    

    
    def ask_input_and_generate_answer_using_relevance_info(self):
        user_input = self.coordinator.gather_input("調べたいことを入力してください。\n ")
        results = self.coordinator.user_input_to_results(user_input)
        relevant_summary = ""
        for result in results:
            if self.coordinator.are_sentences_relevant(user_input, result.summary):
                relevant_summary += self.coordinator.get_summary_from_text(self.coordinator.result_to_text(result), "summarization_handler")
        relevant_summary = self.coordinator.get_summary_from_text(relevant_summary,"gpt",sentences_count=20)
        print(relevant_summary)
        print("_"*35)
        if relevant_summary == "":
            sys.exit("関連性の高い論文が見つかりませんでした。")
        #relevant_summary to txt file
        text_path = "relevant_summary.txt"
        with open(text_path, "w") as f:
            f.write(relevant_summary)
        text = self.word_information_handler.get_text(text_path)
        memory_path = self.word_information_handler.memorize(text)
        self.word_information_handler.chat(memory_path)

        return relevant_summary
    
    def simplychat(self):
        text_path = "relevant_summary.txt"
        text = self.word_information_handler.get_text(text_path)
        memory_path = self.word_information_handler.memorize(text)
        self.word_information_handler.chat(memory_path)
