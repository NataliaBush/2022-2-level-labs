"""
TextRank keyword extraction starter
"""
import string
from pathlib import Path
from main import TextPreprocessor, TextEncoder, extract_pairs, AdjacencyMatrixGraph, VanillaTextRank
from string import punctuation

if __name__ == "__main__":

    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH = ASSETS_PATH / 'article.txt'
    with open(TARGET_TEXT_PATH, 'r', encoding='utf-8') as file:
        text = file.read()

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as file:
        stop_words = tuple(file.read().split('\n'))

    TOKENS = TextPreprocessor(stop_words=stop_words, punctuation=tuple(punctuation)).preprocess_text(text)
    ENCODED = TextEncoder().encode(TOKENS)
    GRAPH = AdjacencyMatrixGraph()
    GRAPH.fill_from_tokens(ENCODED, 5)
    TEXT_RANK = VanillaTextRank(GRAPH)
    TEXT_RANK.train()
    TOP = TEXT_RANK.get_top_keywords(10)
    RESULT = TextEncoder.decode(TOP)
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Keywords are not extracted'
