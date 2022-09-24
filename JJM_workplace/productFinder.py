import re
import pandas as pd
import itertools

## raw data form
formalProductNames = """
    Samsung Galaxy S6
    Samsung Galaxy S7
    Samsung Galaxy S8
    Samsung Galaxy S8Plus
    Samsung Galaxy S9
    Samsung Galaxy S9Plus
    Samsung Galaxy S10
    Samsung Galaxy S10Plus
    Samsung Galaxy S10e
    Samsung Galaxy S10 5G
    Samsung Galaxy S20
    Samsung Galaxy S20Plus
    Samsung Galaxy S20Ultra 5G
    Samsung Galaxy S20Plus 5G
    Samsung Galaxy S205G
    Samsung Galaxy S20Ultra LTE
    Samsung Galaxy S20FE
    Samsung Galaxy S20FE 5G
    Samsung Galaxy S215G
    Samsung Galaxy S21Plus 5G
    Samsung Galaxy S21Ultra 5G
    Samsung Galaxy S21FE 5G
    Samsung Galaxy S225G
    Samsung Galaxy S22Plus 5G
    Samsung Galaxy S22Ultra 5G
    Samsung Galaxy S20FE 2022
    Samsung Galaxy A5Duos
    Samsung Galaxy A5Duos
    Samsung Galaxy A3
    Samsung Galaxy A3Duos
    Samsung Galaxy A5
    Samsung Galaxy A7
    Samsung Galaxy A7Duos
    Samsung Galaxy A8
    Samsung Galaxy A8Duos
    Samsung Galaxy A3 (2016)
    Samsung Galaxy A5 (2016)
    Samsung Galaxy A7 (2016)
    Samsung Galaxy A9 (2016)
    Samsung Galaxy A9Pro (2016)
    Samsung Galaxy A8 (2016)
    Samsung Galaxy A3 (2017)
    Samsung Galaxy A5 (2017)
    Samsung Galaxy A7 (2017)
    Samsung Galaxy A6 (2018)
    Samsung Galaxy A6Plus (2018)
    Samsung Galaxy A8Star 
    Samsung Galaxy A9Star
    Samsung Galaxy A7 (2018)
    Samsung Galaxy A9 (2018)
    Samsung Galaxy A6s
    Samsung Galaxy A8s
    Samsung Galaxy A10
    Samsung Galaxy A20
    Samsung Galaxy A20e
    Samsung Galaxy A30
    Samsung Galaxy A40
    Samsung Galaxy A50
    Samsung Galaxy A60
    Samsung Galaxy A70
    Samsung Galaxy A2Core
    Samsung Galaxy A80
    Samsung Galaxy A10e
    Samsung Galaxy A10s
    Samsung Galaxy A50s
    Samsung Galaxy A30s
    Samsung Galaxy A90 5G
    Samsung Galaxy A70s
    Samsung Galaxy A20s
    Samsung Galaxy A51
    Samsung Galaxy A71
    Samsung Galaxy A01
    Samsung Galaxy A31
    Samsung Galaxy A51 5G
    Samsung Galaxy A41
    Samsung Galaxy A Quantum
    Samsung Galaxy A21s
    Samsung Galaxy A71 5G
    Samsung Galaxy A21
    Samsung Galaxy A01Core
    Samsung Galaxy A71UW 5G 
    Samsung Galaxy A51UW 5G 
    Samsung Galaxy A42 5G
    Samsung Galaxy A12
    Samsung Galaxy A02s
    Samsung Galaxy A32 5G
    Samsung Galaxy A02
    Samsung Galaxy A32
    Samsung Galaxy A52 5G
    Samsung Galaxy A52
    Samsung Galaxy A72
    Samsung Galaxy A22
    Samsung Galaxy A22 5G
    Samsung Galaxy A12Nacho
    Samsung Galaxy A03s
    Samsung Galaxy A52s 5G
    Samsung Galaxy A03Core
    Samsung Galaxy A03
    Samsung Galaxy A13 5G
    Samsung Galaxy A13
    Samsung Galaxy A23
    Samsung Galaxy A33 5G
    Samsung Galaxy A53 5G
    Samsung Galaxy A73 5G
    Samsung Galaxy NotePro 12.2
    Samsung Galaxy Note3 Neo
    Samsung Galaxy Note3 Neo Duos
    Samsung Galaxy NotePro 12.2 5G
    Samsung Galaxy NotePro 12.2 LTE
    Samsung Galaxy Note4
    Samsung Galaxy Note4 Duos
    Samsung Galaxy NoteEdge
    Samsung Galaxy Note5Duos
    Samsung Galaxy Note5
    Samsung Galaxy Note7
    Samsung Galaxy NoteFE
    Samsung Galaxy Note8
    Samsung Galaxy Note9
    Samsung Galaxy Note10
    Samsung Galaxy Note10 5G
    Samsung Galaxy Note10 Plus
    Samsung Galaxy Note10 Plus 5G
    Samsung Galaxy Note10Lite
    Samsung Galaxy Note20
    Samsung Galaxy Note20 5G
    Samsung Galaxy Note20Ultra
    Samsung Galaxy Note20Ultra 5G
    Samsung Galaxy TabPro 8.4
    Samsung Galaxy Tab3Lite 7.0
    Samsung Galaxy TabPro 8.4 3G/LTE
    Samsung Galaxy TabPro 10.1
    Samsung Galaxy TabPro 10.1 LTE
    Samsung Galaxy TabPro 12.2
    Samsung Galaxy TabPro 12.2 3G
    Samsung Galaxy TabPro 12.2 LTE
    Samsung Galaxy Tab3Lite 7.0 3G
    Samsung Galaxy Tab4 7.0 LTE
    Samsung Galaxy Tab4 7.0 3G
    Samsung Galaxy Tab4 7.0
    Samsung Galaxy Tab4 10.1 LTE
    Samsung Galaxy Tab4 10.1 3G
    Samsung Galaxy Tab4 10.1
    Samsung Galaxy Tab4 8.0 LTE
    Samsung Galaxy Tab4 8.0 3G
    Samsung Galaxy Tab4 8.0
    Samsung Galaxy TabS 10.5
    Samsung Galaxy TabS 10.5 LTE
    Samsung Galaxy TabS 8.4
    Samsung Galaxy TabS 8.4 LTE
    Samsung Galaxy Tab3Lite 7.0 VE
    Samsung Galaxy Tab3V
    Samsung Galaxy TabA 8.0
    Samsung Galaxy TabA 9.7
    Samsung Galaxy TabA & S Pen
    Samsung Galaxy Tab4 10.1 (2015)
    Samsung Galaxy TabE 9.6
    Samsung Galaxy TabS2 8.0
    Samsung Galaxy TabS2 9.7
    Samsung Galaxy TabE 8.0
    Samsung Galaxy TabA 7.0 (2016)
    Samsung Galaxy TabA 10.1 (2016)
    Samsung Galaxy TabJ
    Samsung Galaxy TabS3 9.7
    Samsung Galaxy TabA 8.0 (2017)
    Samsung Galaxy TabActive 2
    Samsung Galaxy TabA 10.5
    Samsung Galaxy TabS4 10.5
    Samsung Galaxy TabA 8.0 (2018)
    Samsung Galaxy TabAdvanced2
    Samsung Galaxy TabA 8.0 & S Pen (2019)
    Samsung Galaxy TabA 10.1 (2019)
    Samsung Galaxy TabS5e
    Samsung Galaxy TabA 8.0 (2019)
    Samsung Galaxy TabS6
    Samsung Galaxy TabActivePro
    Samsung Galaxy TabS6 5G
    Samsung Galaxy TabA 8.4 (2020)
    Samsung Galaxy TabS6Lite
    Samsung Galaxy TabS7
    Samsung Galaxy TabS7Plus
    Samsung Galaxy TabA7 10.4 (2020)
    Samsung Galaxy TabActive3
    Samsung Galaxy TabS7FE
    Samsung Galaxy TabA7Lite
    Samsung Galaxy TabA8 10.5 (2021)
    Samsung Galaxy TabS8
    Samsung Galaxy TabS8Plus
    Samsung Galaxy TabS8Ultra
    Samsung Galaxy TabS6Lite (2022)
    Samsung Galaxy Fold
    Samsung Galaxy Fold 5G
    Samsung Galaxy ZFold2 5G
    Samsung Galaxy ZFold3 5G
    Samsung Galaxy ZFlip
    Samsung Galaxy ZFlip 5G
    Samsung Galaxy ZFlip3 5G
    Samsung Galaxy ZFold4
    Samsung Galaxy ZFlip4
    Apple iPhone 6
    Apple iPhone 6Plus
    Apple iPhone 6S
    Apple iPhone 6SPlus
    Apple iPhone SE 1st gen
    Apple iPhone 7
    Apple iPhone 7Plus
    Apple iPhone 8
    Apple iPhone 8Plus
    Apple iPhone X
    Apple iPhone XR
    Apple iPhone XS
    Apple iPhone XSMax
    Apple iPhone 11
    Apple iPhone 11Pro
    Apple iPhone 11ProMax
    Apple iPhone SE 2nd gen
    Apple iPhone 12
    Apple iPhone 12mini
    Apple iPhone 12Pro
    Apple iPhone 12ProMax
    Apple iPhone 13
    Apple iPhone 13mini
    Apple iPhone 13Pro
    Apple iPhone 13ProMax
    Apple iPhone SE 3rd gen
    Apple iPhone 14
    Apple iPhone 14Plus
    Apple iPhone 14Pro
    Apple iPhone 14ProMax
    Tecno SparkPlus
    Tecno SparkPro
    Tecno Phantom6
    Tecno PopLite
    Tecno Pouvoir2Pro
    Tecno Phantom6Plus
    Tecno Pouvoir
    Tecno Pop
    Tecno SparkCM
    Tecno Spark
    Tecno CamonCM
    Tecno F2LTE
    Tecno CamonCXAir
    Tecno CamonCX
    Tecno Pouvoir2
    Tecno PopPro
    Tecno PopS
    Tecno CamonX
    Tecno Spark2
    Tecno CamonXPro
    Tecno Phantom8
    Tecno Camon11
    Tecno SparkGo
    Tecno Spark8
    Tecno Spark8Pro
    Tecno F2
    """
stop = ["5g", "lte", "3g" , "samsung", "iphone", "galaxy", "apple", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"] # we need to delete manipulated yr data
# variarion should be modified by human
variation = {
    'samsung': ['ss', 'smg', 'ssg', 'sam', 'sm', 'samsung'],
    'galaxy': ['galaxy', 'gal', 'glxy', 'glx'],
    'ultra': ['ult', 'ultra', 'u', 'ul'],
    'quantum': ['quantum', 'qantum', 'quontum', 'qauntum'],
    'advanced2': ['adv2', 'advanced2'],
    'iphone': ['iphone', 'iph', 'iphones'],
    'tecno': ['tecn', 'tecno', 'techno'],
    'spark': ['spark', 'spak'],
    'phantom': ['phantom', 'pantom', 'pahntom'],
    'pouvoir': ['pvr', 'pouvoir', 'pouvor', 'povir', 'pouvior', 'povoir']
}

## generate variation for word longer than 5words
# 퍼뮤테이션 알고리즘// 재귀함수를 이용한 조합 만들기 출처, https://kjhoon0330.tistory.com/15
def combination(arr, n):
    out = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        t = arr[i]
        for e in t:
            for rest in combination(arr[i + 1:], n - 1):
                out.append([e] + rest)
    return out

# make variation with fomal word and line and we need to add more rules if we need.
def generate_variation(str, line):
    variations = []
    splited = re.split("\s", str)

    # 1st rule : 첫 3글자
    arr = []
    for w in splited:
        t = []
        t.append(w)
        # variations.append(w)

        t.append(w[:3])
        # variations.append(w[:3])
        arr.append(t)
    f = combination(arr, len(arr))
    for words in f:
        t = ""
        for w in words:
            t = t + w
        variations.append(t)

    # 2rd rule : 모음앞에 있는 단어 조합
    temp = re.findall(r"(\w{0,2})[aeiouy]", str, re.IGNORECASE)  # 모음 앞에 있는 녀석들 추출
    arr = []
    for word in temp:
        t = []
        for a in word:
            t.append(a)
        arr.append(t)
    f = combination(arr, len(arr))

    for words in f:
        t = ""
        for w in words:
            t = t + w
        variations.append(t)
        variations.append(t + str[-1])

    # 대문자 기준으로 나누기 + 붙여쓰기, 띄어쓰기 모두 만들기
    arr = []
    for word in variations:
        t = re.findall(r"([A-Z][a-z]*)", word)
        stemp = ""
        for li in t:
            arr.append(li)
            stemp = stemp + " " + li
            stemp = re.findall("\s*(.+)", stemp)[0]
            arr.append(stemp)

    variations = variations + arr

    ##### line에서 찾기 #####

    # 첫글자와 마지막글자가 같은 문자
    variations = variations + re.findall(r"{}\w*{}".format(str[0], str[-1]), line, re.IGNORECASE)

    return variations


############### Start! ###############

# # if no variation, make new variation
# rawDf = pd.read_csv("facebookData")
# variation = {}
# print(var)
# formalNameList = re.split("\n", formalProductNames)
# for text in formalNameList:
#     text = text.strip()
#     words = re.split('\s', text)
#     for w in words:
#         string = re.search('\w*', w.lower()).group()
#         if string and len(string) >= 5:
#             for line in rawDf['raw']:
#                 tempVar = generate_variation(string, str(line))
#             variation[w.lower()] = list(set(tempVar))

# generate tag and candidates
tag = {}
candidates = {}

# rawData loaded / after textPreprocessing
rawDf = pd.read_csv("data/inputData/facebookData")


################################ generate variations and tagging ################################
formalNameList = re.split("\n", formalProductNames)
companyTags = []
brandTags = []
modelTags = []
for text in formalNameList:
    text = text.strip().lower()
    words = re.split('\s', text)
    companyTags.append(words[0]) # make company tag
    brandTags.append(words[1]) # make brand tag

    for i in range(len(words[2:])) :
        words[i+2] = re.sub("\W", "", words[i+2])
        # make model tag
        if words[i+2] and words[i+2] not in stop:
            modelTags.append(words[i+2])

    # make possible model combinations
    candidatesList = []
    if len(words) >= 2:
        for count in range(len(words)):
            if count <= len(words):
                wwc=[]
                for wc in words:
                    if wc not in stop:
                        wwc.append(wc)
                for com in itertools.combinations(wwc, count+1):
                    candidatesList.append(' '.join(com))
                    candidatesList.append(''.join(com))
        candidates[text] = list(set(candidatesList))

# allocate tag
tag["company"] = list(set(companyTags))
tag["brand"] = list(set(brandTags))
tag["model"] = list(set(modelTags))

print("this is tags : ", tag)
for name in candidates:
    print("this is name : ", name)
    print(candidates[name])


# variation => fomal name 
lines = []
for li in rawDf['raw']:
    tempLine = re.sub("[+]", 'plus', str(li))
    lines.append(tempLine)

changedToFomalname = []
for line in lines:
    temp = re.split('\s', str(line))
    for realname in variation:
        for var in variation[realname]:
            for i in range(len(temp)):
                if re.search(r'{}'.format(var), temp[i]):
                    if len(var) == len(temp[i]):
                        temp[i] = realname
    changedToFomalname.append(' '.join(temp).lower())


################################ product tagging ################################
docs = []
# functionWords = ['+', '.', '*', '?']
for line in changedToFomalname:
    temp = re.split('\s', line)
    text = []
    for word in temp:
        x = 0
        for tagName in tag:
            for t in tag[tagName]:
                r = r"{}"
                if re.search(r.format(t), word) and t == word:
                    text.append((word, 'N', tagName))
                    x=1
                elif t == word:
                    text.append((word, 'N', tagName))
                    x=1
        if x == 0:
            text.append((word, 'I', 'OUT'))
    docs.append(text)

# for d in docs:
#     print(d)

productFromDocs = []
for labeled in docs:
    productName = []
    for tuples in labeled:

        if tuples[1] == 'N':
            productName.append(tuples[0])
    productFromDocs.append(list(set(productName)))


################################ mapping to formal product ################################

fomalName = []

# for token in productFromDocs:
#     compareList = []
#     if len(token) >= 2:
#         for count in range(len(token)):
#             if count <= len(token):
#                 for com in itertools.permutations(token, count+1):
#                     compareList.append(' '.join(com))
#     fomalName.append(compareList)
    
    # tempCompare = []
    # # 비교 시작
    # for var in compareList:
    #     for productName in candidates:
    #         if var in candidates[productName]:
    #             tempCompare.append(productName)

    # fomalName.append(tempCompare)
    
for a in range(len(productFromDocs)):
    print(lines[a], productFromDocs[a], fomalName[a])

final = []
# 전체 연결후 아닌거 빼내기
for i in range(len(fomalName)):
    arr = {}
    if len(fomalName[i]) >= 2:
        g = 0
        allNew = ""
        for candidate in fomalName[i]:
            p = 0
            temp = candidate.lower()
            tempArr = temp.split(' ')
            for t in tempArr:
                f = re.findall("{}".format(t), lines[i])
                if f:
                    p = p + 1
                    allNew = allNew + " {}".format(f[0])
                    g = g + p
            arr[temp] = p
            # # 조합해보기
            # if candidate == fomalName[i][-1]:
            #     print('hi')
            #     arr.append((g, allNew[1:]))
        final.append(arr)

        for c in final:
            blank = []
            li = list(c.items())
            li.sort(key= lambda x:x[1], reverse=True)
            a = 0
            for j in range(len(li)):
                # print(len(li), i, li[i])
                if j == 0:
                    a = li[j][1]
                    blank.append(li[j][0])
                    continue
                else:
                    if a > li[j][1]:
                        continue
                    elif a == li[j][1]:
                        blank.append(li[j][0])
        fomalName[i] = blank


# rawDf["productMapped"] = fomalName
# for i in rawDf['productMapped']:
#     print(i)