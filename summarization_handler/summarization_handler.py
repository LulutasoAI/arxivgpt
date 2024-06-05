from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import nltk
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.metrics import jaccard_distance

"""

LANGUAGE = "english"
SENTENCES_COUNT = 10


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
"""

class SummarizationHandler:
    def __init__(self, language="english",sentences_count=5, relevance_threshold= 0.022) -> None:
        self.language = language
        stemmer = Stemmer(self.language)
        self.summarizer = Summarizer(stemmer)
        self.summarizer.stop_words = get_stop_words(self.language)
        self.sentences_count = sentences_count
        self.relevance_threshold = relevance_threshold
    
    def summarize(self, text, sentences_count=None):
        if sentences_count is None:
            sentences_count = self.sentences_count
        parser = PlaintextParser.from_string(text, Tokenizer(self.language))
        summary = ""
        for sentence in self.summarizer(parser.document, sentences_count):
            summary += str(sentence)
        return summary
    
    def preprocess_text(self, text):
        # Tokenize the text
        words = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

        # Stemming (optional)
        ps = PorterStemmer()
        words = [ps.stem(word) for word in words]

        return words

    def sentence_similarity(self, sentence1, sentence2):
        # Preprocess the sentences
        words1 = self.preprocess_text(sentence1)
        words2 = self.preprocess_text(sentence2)

        # Calculate Jaccard similarity
        jaccard_similarity = len(set(words1).intersection(words2)) / len(set(words1).union(words2))


        return jaccard_similarity
    
    def are_sentences_relevant(self, shorter_sentence, longer_sentence):
        similarity = self.sentence_similarity(shorter_sentence, longer_sentence)
        print(similarity)
        return similarity >= self.relevance_threshold