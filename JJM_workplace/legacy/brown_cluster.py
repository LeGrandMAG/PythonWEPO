import yake
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from brown_clustering_yangyuan import *

# take keywords for each post & turn them into a text string "sentence"
simple_kwextractor = yake.KeywordExtractor()

df = pd.read_csv('data/inputData/facebookData')
sentences = df['raw'].tolist()

tokenizer = RegexpTokenizer(r'\w+')
sample_data_tokenized = [w.lower() for w in sentences if type(w)=='str']
sample_data_tokenized = [tokenizer.tokenize(i) for i in sample_data_tokenized]

corpus = Corpus(sample_data_tokenized, 0.001)
clustering = BrownClustering(corpus, 3)
clustering.train()