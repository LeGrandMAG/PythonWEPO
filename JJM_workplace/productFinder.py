from audioop import reverse
import re
import pandas as pd
import itertools

## raw data form // 규칙 1) company, brand, model, version 은 띄어쓰기로 구분 // model 안에서는 Camel과 숫자로 구분
fomalProductNames = """Samsung Galaxy S6
    Samsung Galaxy S7
    Samsung Galaxy S8
    Samsung Galaxy S8 Plus
    Samsung Galaxy S9
    Samsung Galaxy S9 Plus
    Samsung Galaxy S10
    Samsung Galaxy S10 Plus
    Samsung Galaxy S10e
    Samsung Galaxy S10 5G
    Samsung Galaxy S20
    Samsung Galaxy S20 Plus
    Samsung Galaxy S20 Ultra 5G
    Samsung Galaxy S20 Plus 5G
    Samsung Galaxy S20 5G
    Samsung Galaxy S20 Ultra LTE
    Samsung Galaxy S20Fe
    Samsung Galaxy S20Fe 5G
    Samsung Galaxy S21 5G
    Samsung Galaxy S21 Plus 5G
    Samsung Galaxy S21 Ultra 5G
    Samsung Galaxy S21Fe 5G
    Samsung Galaxy S22 5G
    Samsung Galaxy S22 Plus 5G
    Samsung Galaxy S22 Ultra 5G
    Samsung Galaxy A5 Duos
    Samsung Galaxy A3
    Samsung Galaxy A3 Duos
    Samsung Galaxy A5
    Samsung Galaxy A7
    Samsung Galaxy A7 Duos
    Samsung Galaxy A8
    Samsung Galaxy A8 Duos
    Samsung Galaxy A9 Pro
    Samsung Galaxy A6 Plus
    Samsung Galaxy A8 Star 
    Samsung Galaxy A9 Star
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
    Samsung Galaxy A2 Core
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
    Samsung Galaxy AQuantum
    Samsung Galaxy A21s
    Samsung Galaxy A71 5G
    Samsung Galaxy A21
    Samsung Galaxy A01 Core
    Samsung Galaxy A71Uw 5G 
    Samsung Galaxy A51Uw 5G 
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
    Samsung Galaxy A12 Nacho
    Samsung Galaxy A03s
    Samsung Galaxy A52s 5G
    Samsung Galaxy A03 Core
    Samsung Galaxy A03
    Samsung Galaxy A13 5G
    Samsung Galaxy A13
    Samsung Galaxy A23
    Samsung Galaxy A33 5G
    Samsung Galaxy A53 5G
    Samsung Galaxy A73 5G
    Samsung Galaxy Note Pro 12.2
    Samsung Galaxy Note3Neo
    Samsung Galaxy Note3Neo Duos
    Samsung Galaxy Note Pro 12.2 5G
    Samsung Galaxy Note Pro 12.2 LTE
    Samsung Galaxy Note4
    Samsung Galaxy Note4 Duos
    Samsung Galaxy NoteEdge
    Samsung Galaxy Note5 Duos
    Samsung Galaxy Note5
    Samsung Galaxy Note7
    Samsung Galaxy NoteFe
    Samsung Galaxy Note8
    Samsung Galaxy Note9
    Samsung Galaxy Note10
    Samsung Galaxy Note10 5G
    Samsung Galaxy Note10 Plus
    Samsung Galaxy Note10 Plus 5G
    Samsung Galaxy Note10 Lite
    Samsung Galaxy Note20
    Samsung Galaxy Note20 5G
    Samsung Galaxy Note20 Ultra
    Samsung Galaxy Note20 Ultra 5G
    Samsung Galaxy Tab Pro 8.4
    Samsung Galaxy Tab3 Lite 7.0
    Samsung Galaxy Tab Pro 8.4 3G/LTE
    Samsung Galaxy Tab Pro 10.1
    Samsung Galaxy Tab Pro 10.1 LTE
    Samsung Galaxy Tab Pro 12.2
    Samsung Galaxy Tab Pro 12.2 3G
    Samsung Galaxy Tab Pro 12.2 LTE
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
    Samsung Galaxy Tab3 Lite 7.0 VE
    Samsung Galaxy Tab3V
    Samsung Galaxy TabA 8.0
    Samsung Galaxy TabA 9.7
    Samsung Galaxy TabA & S Pen
    Samsung Galaxy TabE 9.6
    Samsung Galaxy TabS2 8.0
    Samsung Galaxy TabS2 9.7
    Samsung Galaxy TabE 8.0
    Samsung Galaxy TabJ
    Samsung Galaxy TabS3 9.7
    Samsung Galaxy TabActive 2
    Samsung Galaxy TabA 10.5
    Samsung Galaxy TabS4 10.5
    Samsung Galaxy TabAdvanced2
    Samsung Galaxy TabS5e
    Samsung Galaxy TabS6
    Samsung Galaxy TabActive Pro
    Samsung Galaxy TabS6 5G
    Samsung Galaxy TabS6 Lite
    Samsung Galaxy TabS7
    Samsung Galaxy TabS7 Plus
    Samsung Galaxy TabActive3
    Samsung Galaxy TabS7Fe
    Samsung Galaxy TabA7 Lite
    Samsung Galaxy TabS8
    Samsung Galaxy TabS8 Plus
    Samsung Galaxy TabS8 Ultra
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
    Apple iPhone 6 Plus
    Apple iPhone 6s
    Apple iPhone 6s Plus
    Apple iPhone Se 1st gen
    Apple iPhone 7
    Apple iPhone 7 Plus
    Apple iPhone 8
    Apple iPhone 8 Plus
    Apple iPhone X
    Apple iPhone Xr
    Apple iPhone Xs
    Apple iPhone Xs Max
    Apple iPhone 11
    Apple iPhone 11 Pro
    Apple iPhone 11 Pro Max
    Apple iPhone Se 2nd gen
    Apple iPhone 12
    Apple iPhone 12 Mini
    Apple iPhone 12 Pro
    Apple iPhone 12 Pro Max
    Apple iPhone 13
    Apple iPhone 13 Mini
    Apple iPhone 13 Pro
    Apple iPhone 13 ProMax
    Apple iPhone Se 3rd gen
    Apple iPhone 14
    Apple iPhone 14 Plus
    Apple iPhone 14 Pro
    Apple iPhone 14 Pro Max
    Tecno Spark Plus
    Tecno Spark Pro
    Tecno Phantom6
    Tecno Pop Lite
    Tecno Pouvoir2 Pro
    Tecno Phantom6 Plus
    Tecno Pouvoir
    Tecno Pop
    Tecno SparkCm
    Tecno Spark
    Tecno CamonCm
    Tecno F2 LTE
    Tecno CamonCx Air
    Tecno CamonCx
    Tecno Pouvoir2
    Tecno Pop Pro
    Tecno PopS
    Tecno CamonX
    Tecno Spark2
    Tecno CamonX Pro
    Tecno Phantom8
    Tecno Camon11
    Tecno SparkGo
    Tecno Spark8
    Tecno Spark8 Pro
    Tecno F2"""

stop = ['LTE',] # we need to delete manipulated yr data
# variarion should be modified by human
variation = {
    'samsung': ['ss', 'smg', 'ssg', 'sam', 'sm', 'samsung'],
    'galaxy': ['galaxy', 'gal', 'glxy', 'glx'],
    'ultra': ['ult', 'ultra', 'ul'],
    'quantum': ['quantum', 'qantum', 'quontum', 'qauntum'],
    'advanced2': ['adv2', 'advanced2'],
    'iphone': ['iphone', 'iph', 'iphones'],
    'tecno': ['tecn', 'tecno', 'techno'],
    'spark': ['spark', 'spak'],
    'phantom': ['phantom', 'pantom', 'pahntom'],
    'pouvoir': ['pvr', 'pouvoir', 'pouvor', 'povir', 'pouvior', 'povoir'],
}
# variarion should be modified by human // 0=company, 1=brand, 2=model, 3=version
tag = {
    0: ['Samsung', 'Apple', 'Tecno', 'samsung', 'apple', 'tecno'],
    1: ['Galaxy', 'iPhone', 'galaxy', 'iphone'],
    2: [],
    3: []
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
# #// 여기는 맨처음에 variation 만드는건데, 성능이 별로임 => 나중에 Soundex, Metaphone 알고리즘 이용 => jellyfish
# rawDf = pd.read_csv("facebookData")
# variation = {}
# print(var)
# fomalNameList = re.split("\n", fomalProductNames)
# for text in fomalNameList:
#     text = text.strip()
#     words = re.split('\s', text)
#     for w in words:
#         string = re.search('\w*', w.lower()).group()
#         if string and len(string) >= 5:
#             for line in rawDf['raw']:
#                 tempVar = generate_variation(string, str(line))
#             variation[w.lower()] = list(set(tempVar))

# generate tag and candidates

productMap = {} # 제품명 매핑을 위한 dic  0=company, 1=brand, 2=model, 3=version

# rawData loaded / after textPreprocessing
rawDf = pd.read_csv("data/inputData/facebookData")


################################ generate variations and tagging ################################

fomalNameList = re.split("\n", fomalProductNames)
for text in fomalNameList:
    productDic = {}
    text = text.strip()
    words = re.split('\s', text)
    
    tempWords = []
    # remove company(0) & brand(1) name
    for w in words:
        if w in tag[0]:
            productDic[0] = [w.lower()] #add company(0) name to product list
            continue
        elif w in tag[1]:
            productDic[1] = [w.lower()] #add brand(1) name to product list
            continue
        else:
            tempWords.append(w)

    modelingrediant = []
    # modelingrediantForTag = []
    
    modelCandidates = []
    
    # model 요소 분해
    matches = re.finditer('.+?(?:(?<=[A-Za-z0-9])(?=[A-Z])|(?<=[A-Za-z])(?=[A-Z0-9])|$)', tempWords[0]) # 대문자(camel), 숫자 구분 ★★★
    # matchesForTag = re.finditer('.+?(?:(?<=[\w])(?=[A-Z])|(?<=[A-Z])(?=[A-Z])|$)', tempWords[0]) # 대문자(camel)만 구분
    
    # 제품 매핑 및 태깅 위한 자료 만들기
    for m in matches:
        modelingrediant.append(m.group().lower()) 

    if len(modelingrediant) >=2:
        if modelingrediant[0] == 'a' or modelingrediant[0] == 's':
            modelingrediant[0] = modelingrediant[0] + modelingrediant[1]
            modelingrediant = [modelingrediant[0]] + modelingrediant[2:]
        # print(modelingrediant)
        
    for ran in range(len(modelingrediant)):
        for c in itertools.combinations(modelingrediant, ran+1):
            modelCandidates.append(' '.join(c))
            modelCandidates.append(''.join(c))

    modelCandidates = list(set(modelCandidates))
    
    # 한글자 짜리 제거  
    tModelcd = []
    if len(modelCandidates) > 1:
        for cd in modelCandidates:
            if len(cd) > 1:
                tModelcd.append(cd)
        modelCandidates = tModelcd
        
    
    # version 조합 만들기
    tempVer = []
    for c in itertools.combinations(tempWords[1:], len(tempWords[1:])):
        tempVer.append(' '.join(c).lower())
        tempVer.append(''.join(c).lower())
    
    tempMC = []
    for mc in tempVer:
        mcVar = re.sub('ultra','u', mc)
        tempMC.append(mcVar)
        mcVar = re.sub('pro', 'p', mc)
        tempMC.append(mcVar)
        mcVar = re.sub('plus', '+', mc)
        tempMC.append(mcVar)
    tempVer = list(set(tempVer + tempMC))
        
    # print(modelCandidates, tempWords[1:], list(set(tempVer)))
    
    modelsForMapping = []
    for produc in itertools.product(modelCandidates, list(set(tempVer))):
        modelsForMapping.append(' '.join(produc).strip())
        modelsForMapping.append(''.join(produc).strip())
        
    # print(modelCandidates, list(set(modelsForMapping)))
    

    productDic[2] = list(set(modelsForMapping)) #매핑을 위해 model(2) 자료 넣기
    if len(tempWords) >=2:
        productDic[3] = [i.lower() for i in tempWords[1:]] #매핑을 위해 version(3) 자료 넣기
    
    productMap[text] = productDic #제품별로 넣기
    

# allocate tag 0=company, 1=brand, 2=model, 3=version
    tag[2] = tag[2] + modelCandidates + [i.lower() for i in tempWords[1:]] + modelsForMapping
    tag[3] = tag[3] + [i.lower() for i in tempWords[1:]]

tag[2] = list(set(tag[2]))
tag[3] = list(set(tag[3]))

## checking point 
# print(tag)
# for name in productMap:
#     if len(productMap[name]) > 1:
#         print("this is name : ", name)
#         print(productMap[name])


# variation => fomal name 
changedToFomalname = []
for line in rawDf['raw']:
    templi = re.split('\s', str(line))
    for realname in variation:
        for var in variation[realname]:
            rule = r'{}'
            for i in range(len(templi)):
                if re.search(rule.format(var), templi[i], re.IGNORECASE):
                    if len(var) == len(templi[i]):
                        templi[i] = realname
    changedToFomalname.append(' '.join(templi).lower())

# #check point
# for i in range(len(rawDf['raw'])):
#     print(rawDf['raw'][i])
#     print(changedToFomalname[i])


################################ product tagging ################################ 
docs = []
functionWords = ['+', '.', '*', '?']
for line in changedToFomalname:
    tempArr = re.split('\s', line)
    text = []
    for word in tempArr:
        x = 0
        for tagName in tag:
            for t in tag[tagName]:
                r = r"{}"
                # if re.search(r.format(t), word) and t == word:
                #     text.append((word, 'N', tagName))
                #     x=1
                if t == word:
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
            productName.append((tuples[0], tuples[2]))
                               
    productFromDocs.append(list(set(productName)))


# for i in range(len(productFromDocs)):
#     if len(productFromDocs[i]) >= 2:
#         productFromDocs[i].sort(key = lambda x : x[1])
#     print(changedToFomalname[i], productFromDocs[i])

# ################################ mapping to formal product ################################
## 조합 만들어서 / 모델끼리 

###모델 조합 만들기
modelCombination = []
for token in productFromDocs:
    tempToken = []
    tempCombi = []
    if token:
        for t in token:
            if t[1] == 1 or t[1] == 2:
                tempToken.append(t[0])

        if len(tempToken) == 1: #한글자 이지만
            if len(tempToken[0]):
                if re.search("\d", tempToken[0]): #숫자이면
                    tempCombi.append(tempToken[0]) #후보군에 집어넣기
        else:
            for count in range(len(tempToken)): #한글자가 아닌경우에는 
                for c in itertools.combinations(tempToken, count+1): #2개 이상으로 조합
                    tempCombi.append(' '.join(c))

    modelCombination.append(list(set(tempCombi)))

# check point
# for i in range(len(productFromDocs)):
#     if len(productFromDocs[i]) >= 2:
#         productFromDocs[i].sort(key = lambda x : x[1])
#     print(changedToFomalname[i], productFromDocs[i], modelCombination[i])


# ###모델 조합과 , 제품 이름 매칭
fomalProductList = []
for combi in modelCombination:
    tempFomal = []
    if combi:
        for word in combi:
            for name in productMap:
                if re.search('\D', word):
                    if word in productMap[name][2]:
                        tempFomal.append(name)
                else:
                    if productMap[name][0][0] == 'apple':
                        if word in productMap[name][2]:
                            tempFomal.append(name)
    fomalProductList.append(tempFomal)

# check point
for i in range(len(fomalProductList)):
    if len(productFromDocs[i]) >= 2:
        productFromDocs[i].sort(key = lambda x : x[1])
    print(changedToFomalname[i], fomalProductList[i])


## 아닌것들 제외하기
# 1단계 scoring
finalProductList = []

for i in range(len(fomalProductList)):
    point = 0
    tempFomalList = []
    if len(fomalProductList[i]) > 1:
        for fomalproduct in fomalProductList[i]:
            tokenProduct = re.split("\s", fomalproduct.lower())
            tempTokens = []
            # print(tokenProduct)

            for tkn in tokenProduct:
                # tkn = tkn.lower()
                if tkn in tag[0]:
                    if tkn in modelCombination[i]: # 회사명이 있으면 point +1
                        point = point + 10000
                    # else:
                    #     point = point - 20000
                elif tkn in tag[1]:
                    if tkn in modelCombination[i]: # 모델명이 있으면 point +1
                        point = point + 10000
                    # else:
                    #     point = point - 20000
                else:
                    tempTokens.append(tkn)
            
            tListFind = re.finditer('.+?(?:(?<=[A-Za-z0-9])(?=[A-Z])|(?<=[A-Za-z])(?=[A-Z0-9])|$)', tempTokens[0])

            # print(modelCombination[i])
            tList=[]
            for tf in tListFind:
                tList.append(tf.group())
 
            # print("tempTokens : ", tList)
            for tm in tList:
                if tm in modelCombination[i]:
                    point = point + 10
                else:
                    for model in modelCombination[i]:
                        if re.search("{}".format(tm), model):
                            point = point + 1
                        else:
                            point = point - 10
            
            tempFomalList.append((fomalproduct, point))
        
    finalProductList.append(tempFomalList)

# for i in range(len(finalProductList)):
#     if len(finalProductList[i]) >= 2:
#         finalProductList[i].sort(key = lambda x : x[1], reverse=True)
#     print(modelCombination[i], finalProductList[i])

# ## sorting by score
# fomalName = []
# for token in productFromDocs:
#     compareList = []
#     for t in token:     
#         for product in candidates:
#             if t in candidates[product]:
#                 compareList.append(product)
#         fomalName.append(compareList)
    
#     # tempCompare = []
#     # # 비교 시작
#     # for var in compareList:
#     #     for productName in candidates:
#     #         if var in candidates[productName]:
#     #             tempCompare.append(productName)

#     # fomalName.append(tempCompare)
    

# final = []
# # 전체 연결후 아닌거 빼내기
# for i in range(len(fomalName)):
#     arr = {}
#     if len(fomalName[i]) >= 2:
#         g = 0
#         allNew = ""
#         for candidate in fomalName[i]:
#             p = 0
#             temp = candidate.lower()
#             tempArr = temp.split(' ')
#             for t in tempArr:
#                 f = re.findall("{}".format(t), lines[i])
#                 if f:
#                     p = p + 1
#                     allNew = allNew + " {}".format(f[0])
#                     g = g + p
#             arr[temp] = p
#             # # 조합해보기
#             # if candidate == fomalName[i][-1]:
#             #     print('hi')
#             #     arr.append((g, allNew[1:]))
#         final.append(arr)

#         for c in final:
#             blank = []
#             li = list(c.items())
#             li.sort(key= lambda x:x[1], reverse=True)
#             a = 0
#             for j in range(len(li)):
#                 # print(len(li), i, li[i])
#                 if j == 0:
#                     a = li[j][1]
#                     blank.append(li[j][0])
#                     continue
#                 else:
#                     if a > li[j][1]:
#                         continue
#                     elif a == li[j][1]:
#                         blank.append(li[j][0])
#         fomalName[i] = blank


# # rawDf["productMapped"] = fomalName
# # for i in rawDf['productMapped']:
# #     print(i)