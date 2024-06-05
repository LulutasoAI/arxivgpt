from langchain_utils.ai_wrapper import AIWrapper
from gpt_handler.key import secret_key
from gpt_handler.long_string_data import default_system_message
ai_wrapper = AIWrapper(secret_key)


ai_wrapper.memorize_search_result("How do you make the Arxiv search query?", default_system_message)
result = ai_wrapper.converse("I would like to search for Reinforcement learning on Arxiv platform can you make a proper Query?")

print(result)