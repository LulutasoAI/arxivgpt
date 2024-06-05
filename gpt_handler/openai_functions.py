from gpt_handler import key
from gpt_handler.long_string_data import default_system_message, summary_message, translation_message
from openai import OpenAI

class gptHandler:
    def __init__(self) -> None:
        self.system_messages = [default_system_message,summary_message,translation_message]
        self.preset_tokens = [150, None, None]
        self.query_mode = 0 
        self.summary_mode = 1
        self.translation_mode = 2
        
        

    def call_GPT(self,text, mode=0):
        print("going to call chat gpt")
        client = OpenAI(api_key=key.secret_key)
        chat_models = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role":"system","content":self.system_messages[mode]},
                {"role": "user", "content": text}
                ],
                max_tokens=self.preset_tokens[mode],
                temperature = 1,
                top_p = 0.95,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
        return chat_models.choices[0].message.content
    
