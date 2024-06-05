from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import VectorStoreRetrieverMemory
import os
import faiss
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS





class AIWrapper():
    def __init__(self, openai_api_key):
        self.language_model = OpenAI(openai_api_key=openai_api_key, temperature=0)
        #self.memory = ConversationBufferMemory()
        embedding_size = 1536 # Dimensions of the OpenAIEmbeddings
        index = faiss.IndexFlatL2(embedding_size)
        openai_emb = OpenAIEmbeddings(openai_api_key = openai_api_key)
        embedding_fn = openai_emb.embed_query
        vectorstore = FAISS(embedding_fn, index, InMemoryDocstore({}), {})
        retriever = vectorstore.as_retriever(search_kwargs=dict(k=3))
        self.memory = VectorStoreRetrieverMemory(retriever=retriever)

    def memorize_search_result(self, query:str, result:str):
        self.memory.save_context({"input": query}, {"output": result})
        
    def converse(self, user_input:str) -> str:
        conversation = ConversationChain(llm=self.language_model, verbose=True, memory=self.memory)
        response = conversation.predict(input=user_input)
        result = response
        return result 



