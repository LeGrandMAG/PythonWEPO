# from unittest import result
from cgitb import text
from pydoc import tempfilepager
from tempfile import tempdir
import pandas as pd
# import nltk
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords
import re
import emoji

from nltk.tag import StanfordPOSTagger
from textblob import TextBlob
import os

jar = 'C:/Users/KING-K-S/pythonWEPO/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/stanford-postagger.jar'
model = 'C:/Users/KING-K-S/pythonWEPO/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/models/french-ud.tagger'
os.environ['JAVAHOME'] = 'C:/Program Files (x86)/Java/jre1.8.0_341'


# nltk.download('stopwords')
# nltk.download('punkt')

# 이모지 제거 전처리 // source : https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def remove_emoji(string):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', string)

# 이모지 제거 전처리 2
def give_emoji_free_text(text):
    # allchars = [str for str in text.decode('utf-8')]
    # emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    emoji_list = [c for c in text if c in emoji.distinct_emoji_list(text)]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

#remove stopwords
def del_stopword(text):
    stopWordList = ['*','à','et','en', 'détail', 'contactez', 'nous', 'suis', 'un', 'peu', 'de', 'problème', 'proposez', 'num', ',','!', '?', 'show', 'app', 'promotion', 'semaine', 'ensemble']
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in stopWordList)])
    return clean_text


def get_contents(RAWDATA_PATH):
    df = pd.read_excel(RAWDATA_PATH)
    contents = df["postDetail"].to_list()

    #stopwords set up

    temp = []
    for line in contents:
        line = line.lower()
        line = give_emoji_free_text(line)
        line = remove_emoji(line)
        line = del_stopword(line)
        temp.append(line)

    out = pd.DataFrame(temp, columns=['content'], dtype='string')
    out.drop_duplicates(['content'], keep='first', ignore_index=True, inplace= True)
    out.dropna()

    dic = {}
    temp = []
    for line in out['content']:
        line = line.split(' ')
        temp.append(line)
        
    dic["raw"] = out['content'].to_list()
    dic["word"] = temp

    out = pd.DataFrame(dic, dtype="object")
    
    return out

def get_tag(df):
    tagger = StanfordPOSTagger(model, jar, encoding = 'utf8')
    out = []
    for line in df['raw']:
        blob = TextBlob(line)
        res = tagger.tag(blob.split())
        temp = []
        for i in range(len(res)):
            if res[i][1] == 'NUM' or res[i][1] == 'NOUN':
                temp.append(res[i][0])
        out.append(temp)

    dic = {}
    dic['words'] = out
    df = pd.DataFrame(dic, dtype='object')
    # df.to_excel("data/outputData/outputData_nounOnly.xlsx")
    
    return df

RAWDATA_PATH = "data/rawData/facebookData.xlsx"
df = get_contents(RAWDATA_PATH)
df.to_csv("data/inputData/facebookData")


#################################### legacy ####################################
#draft
def old_identifier():
    price = []
    product = []
    memory = []
    battery = []

    product_list = ['iphone', '5s', '6','6s','6+', '6s+', '7', '7+', '8',' 8+', 'se', 'x', 'xs', 'max', 'xr', '11','pro', 'promax', '12' ,'mini', 'spark', 's16', 's8', 'samsung', 'a36']

    for line in df["word"]:
        price.append([text for text in line if '$' in text])
        product.append([text for text in line if any(i in text for i in product_list) ])
        # [text for text in line if any(i in str for i in stopWordList)]
        memory.append([text for text in line if 'gb' in text])
        battery.append([text for text in line if '%' in text])

    dic = {}
    dic["price"] = price
    dic["product"] = product
    dic["memory"] = memory
    dic["battery"] = battery

    df = pd.DataFrame(dic, dtype="object")

