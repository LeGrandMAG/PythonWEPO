import spacy
from spacy.language import Language

@Language.component("my_component")
def __init__(self, nlp, name):
        self.nlp = nlp
        
def my_component(doc):
    return doc

