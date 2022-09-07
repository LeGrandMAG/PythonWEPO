# from unittest import result
import pandas as pd
# import nltk
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords
import re
import emoji

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

df = pd.read_excel("facebookData.xlsx")
contents = df["postDetail"].to_list()

#stopwords set up
stopWordList = stopwords.words('french')
noWord = re.compile("\W")

output = pd.DataFrame(columns={'rawData', 'content', 'products', 'battery', 'price'})
output['content'] = df['postDetail']
temp = []
for line in contents:
    line = give_emoji_free_text(line)
    line = remove_emoji(line)
    temp.append(line)

            
print(temp)