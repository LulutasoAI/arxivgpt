import arxiv
import pandas as pd
import urllib.request
from PyPDF2 import PdfReader
from io import BytesIO
import sys 

class ArxivHandler:
    def __init__(self) -> None:
        self.client = arxiv.Client()

    def search(self, query, max_results=15, sort_by=arxiv.SortCriterion.SubmittedDate) -> pd.DataFrame:
        return arxiv.Search(query=query, max_results=max_results, sort_by=sort_by)

    def view_search_result(self, search:pd.DataFrame):
        for result in self.client.results(search):
            print("Title: ", result.title)
            print("Authors: ", result.authors)
            print("Summary: ", result.summary)
            print("Comment: ", result.comment)
            print("Journal Reference: ", result.journal_ref)
            print("DOI: ", result.doi)
            print("Primary Category: ", result.primary_category)
            print("Categories: ", result.categories)
            print("Published: ", result.published)
            print("Updated: ", result.updated)
            print("PDF URL: ", result.pdf_url)
            print("\n")

    def search_results_to_text(self, search:pd.DataFrame):
        text = ""
        for result in self.client.results(search):
            try:
                print(result.title)
                print("PDF URL: ", result.pdf_url)
                response = urllib.request.urlopen(result.pdf_url)
                pdf_file = PdfReader(BytesIO(response.read()))
                for page in range(len(pdf_file.pages)):
                    text += pdf_file.pages[page].extract_text()
            except:
                pass 
        return text
    
    def result_to_text(self, result:arxiv.Result):
        text = ""
        try:
            print(result.title)
            print("PDF URL: ", result.pdf_url)
            response = urllib.request.urlopen(result.pdf_url)
            pdf_file = PdfReader(BytesIO(response.read()))
            for page in range(len(pdf_file.pages)):
                text += pdf_file.pages[page].extract_text()
        except:
            pass 
        return text
    def search_results_to_summaries(self, search:pd.DataFrame):
        text = ""
        counter = 0
        for result in self.client.results(search):
            print("______________________")
            print(result.title)
            print("______________________")
            text += result.summary
            counter += 1
        print(counter)
        if counter == 0:
            sys.exit("No results found.")
        return text
    
    def query_to_text(self, query: str) -> str:
        """Performs a search and extracts text from the results."""
        search = self.search(query=query)
        print(type(search))  # Add this line to check the type
        text = self.search_results_to_text(search)
        return text
    
    def query_sanitizer(self, query:str) -> str:
        query = query.replace("search_query=", "")
        return query
    def query_to_summaries(self, query: str) -> str:
        """Performs a search and extracts text from the results."""
        query = self.query_sanitizer(query)
        search = self.search(query=query,max_results=50)
        print(type(search))  # Add this line to check the type
        text = self.search_results_to_summaries(search)
        return text
    
    def query_to_results(self, query: str) -> list:
        """Performs a search and extracts text from the results."""
        query = self.query_sanitizer(query)
        search = self.search(query=query,max_results=10)
        print(type(search))
        results = self.search_to_results(search)
        return results
    def search_to_results(self, search:pd.DataFrame) -> list:
        results = []
        for result in self.client.results(search):
            results.append(result)
        return results

    
        