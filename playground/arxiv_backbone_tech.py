import arxiv
import pandas as pd
import urllib.request
from PyPDF2 import PdfReader
from io import BytesIO
# Construct the default API client.
client = arxiv.Client()

# Search for the 10 most recent articles matching the keyword "quantum."
search = arxiv.Search(query="quantum", max_results=10, sort_by=arxiv.SortCriterion.SubmittedDate)

for result in client.results(search):
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



# Construct the default API client.
client = arxiv.Client()

# Search for the most recent article matching the keyword "quantum."
search = arxiv.Search(query="quantum", max_results=1, sort_by=arxiv.SortCriterion.SubmittedDate)

# Get the first (and only) result.
result = next(client.results(search))

# Download the PDF.
response = urllib.request.urlopen(result.pdf_url)

# Read the PDF and convert it into text.
pdf_file = PdfReader(BytesIO(response.read()))
text = ""
for page in range(len(pdf_file.pages)):
    text += pdf_file.pages[page].extract_text()

print(text)
