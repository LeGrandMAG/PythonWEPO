import re
from unittest import result

samsung_raw = """Samsung Galaxy S6
Samsung Galaxy S7
Samsung Galaxy S8
Samsung Galaxy S8 +
Samsung Galaxy S9
Samsung Galaxy S9 +
Samsung Galaxy S10
Samsung Galaxy S10 +
Samsung Galaxy S10 e
Samsung Galaxy S10 5G
Samsung Galaxy S20
Samsung Galaxy S20 +
Samsung Galaxy S20 Ultra 5G
Samsung Galaxy S20 + 5G
Samsung Galaxy S20 5G
Samsung Galaxy S20 Ultra LTE
Samsung Galaxy S20 FE
Samsung Galaxy S20 FE 5G
Samsung Galaxy S21 5G
Samsung Galaxy S21 + 5G
Samsung Galaxy S21 Ultra 5G
Samsung Galaxy S21 FE 5G
Samsung Galaxy S22 5G
Samsung Galaxy S22 + 5G
Samsung Galaxy S22 Ultra 5G
Samsung Galaxy S20 FE 2022
Samsung Galaxy A5 Duos
Samsung Galaxy A5 Duos
Samsung Galaxy A3
Samsung Galaxy A3 Duos
Samsung Galaxy A5
Samsung Galaxy A7
Samsung Galaxy A7 Duos
Samsung Galaxy A8
Samsung Galaxy A8 Duos
Samsung Galaxy A3 (2016)
Samsung Galaxy A5 (2016)
Samsung Galaxy A7 (2016)
Samsung Galaxy A9 (2016)
Samsung Galaxy A9 Pro (2016)
Samsung Galaxy A8 (2016)
Samsung Galaxy A3 (2017)
Samsung Galaxy A5 (2017)
Samsung Galaxy A7 (2017)
Samsung Galaxy A6 (2018)
Samsung Galaxy A6 + (2018)
Samsung Galaxy A8 Star 
Samsung Galaxy A9 Star
Samsung Galaxy A7 (2018)
Samsung Galaxy A9 (2018)
Samsung Galaxy A6 s
Samsung Galaxy A8 s
Samsung Galaxy A10
Samsung Galaxy A20
Samsung Galaxy A20 e
Samsung Galaxy A30
Samsung Galaxy A40
Samsung Galaxy A50
Samsung Galaxy A60
Samsung Galaxy A70
Samsung Galaxy A2 Core
Samsung Galaxy A80
Samsung Galaxy A10 e
Samsung Galaxy A10 s
Samsung Galaxy A50 s
Samsung Galaxy A30 s
Samsung Galaxy A90 5G
Samsung Galaxy A70 s
Samsung Galaxy A20 s
Samsung Galaxy A51
Samsung Galaxy A71
Samsung Galaxy A01
Samsung Galaxy A31
Samsung Galaxy A51 5G
Samsung Galaxy A41
Samsung Galaxy A Quantum
Samsung Galaxy A21 s
Samsung Galaxy A71 5G
Samsung Galaxy A21
Samsung Galaxy A01 Core
Samsung Galaxy A71 5G UW
Samsung Galaxy A51 5G UW
Samsung Galaxy A42 5G
Samsung Galaxy A12
Samsung Galaxy A02 s
Samsung Galaxy A32 5G
Samsung Galaxy A02
Samsung Galaxy A32
Samsung Galaxy A52 5G
Samsung Galaxy A52
Samsung Galaxy A72
Samsung Galaxy A22
Samsung Galaxy A22 5G
Samsung Galaxy A12 Nacho
Samsung Galaxy A03 s
Samsung Galaxy A52 s 5G
Samsung Galaxy A03 Core
Samsung Galaxy A03
Samsung Galaxy A13 5G
Samsung Galaxy A13
Samsung Galaxy A23
Samsung Galaxy A33 5G
Samsung Galaxy A53 5G
Samsung Galaxy A73 5G
Samsung Galaxy Note Pro 12.2
Samsung Galaxy Note 3 Neo
Samsung Galaxy Note 3 Neo Duos
Samsung Galaxy Note Pro 12.2 5G
Samsung Galaxy Note Pro 12.2 LTE
Samsung Galaxy Note 4
Samsung Galaxy Note 4 Duos
Samsung Galaxy Note Edge
Samsung Galaxy Note 5 Duos
Samsung Galaxy Note 5
Samsung Galaxy Note 7
Samsung Galaxy Note FE
Samsung Galaxy Note 8
Samsung Galaxy Note 9
Samsung Galaxy Note 10
Samsung Galaxy Note 10 5G
Samsung Galaxy Note 10 +
Samsung Galaxy Note 10 + 5G
Samsung Galaxy Note 10 Lite
Samsung Galaxy Note 20
Samsung Galaxy Note 20 5G
Samsung Galaxy Note 20 Ultra
Samsung Galaxy Note 20 Ultra 5G
Samsung Galaxy Tab Pro 8.4
Samsung Galaxy Tab 3 Lite 7.0
Samsung Galaxy Tab Pro 8.4 3G/LTE
Samsung Galaxy Tab Pro 10.1
Samsung Galaxy Tab Pro 10.1 LTE
Samsung Galaxy Tab Pro 12.2
Samsung Galaxy Tab Pro 12.2 3G
Samsung Galaxy Tab Pro 12.2 LTE
Samsung Galaxy Tab 3 Lite 7.0 3G
Samsung Galaxy Tab 4 7.0 LTE
Samsung Galaxy Tab 4 7.0 3G
Samsung Galaxy Tab 4 7.0
Samsung Galaxy Tab 4 10.1 LTE
Samsung Galaxy Tab 4 10.1 3G
Samsung Galaxy Tab 4 10.1
Samsung Galaxy Tab 4 8.0 LTE
Samsung Galaxy Tab 4 8.0 3G
Samsung Galaxy Tab 4 8.0
Samsung Galaxy Tab S 10.5
Samsung Galaxy Tab S 10.5 LTE
Samsung Galaxy Tab S 8.4
Samsung Galaxy Tab S 8.4 LTE
Samsung Galaxy Tab 3 Lite 7.0 VE
Samsung Galaxy Tab 3 V
Samsung Galaxy Tab A 8.0
Samsung Galaxy Tab A 9.7
Samsung Galaxy Tab A & S Pen
Samsung Galaxy Tab 4 10.1 (2015)
Samsung Galaxy Tab E 9.6
Samsung Galaxy Tab S2 8.0
Samsung Galaxy Tab S2 9.7
Samsung Galaxy Tab E 8.0
Samsung Galaxy Tab A 7.0 (2016)
Samsung Galaxy Tab A 10.1 (2016)
Samsung Galaxy Tab J
Samsung Galaxy Tab S3 9.7
Samsung Galaxy Tab A 8.0 (2017)
Samsung Galaxy Tab Active 2
Samsung Galaxy Tab A 10.5
Samsung Galaxy Tab S4 10.5
Samsung Galaxy Tab A 8.0 (2018)
Samsung Galaxy Tab Advanced2
Samsung Galaxy Tab A 8.0 & S Pen (2019)
Samsung Galaxy Tab A 10.1 (2019)
Samsung Galaxy Tab S5 e
Samsung Galaxy Tab A 8.0 (2019)
Samsung Galaxy Tab S6
Samsung Galaxy Tab Active Pro
Samsung Galaxy Tab S6 5G
Samsung Galaxy Tab A 8.4 (2020)
Samsung Galaxy Tab S6 Lite
Samsung Galaxy Tab S7
Samsung Galaxy Tab S7 +
Samsung Galaxy Tab A7 10.4 (2020)
Samsung Galaxy Tab Active3
Samsung Galaxy Tab S7 FE
Samsung Galaxy Tab A7 Lite
Samsung Galaxy Tab A8 10.5 (2021)
Samsung Galaxy Tab S8
Samsung Galaxy Tab S8 +
Samsung Galaxy Tab S8 Ultra
Samsung Galaxy Tab S6 Lite (2022)
Samsung Galaxy Fold
Samsung Galaxy Fold 5G
Samsung Galaxy Z Fold 2 5G
Samsung Galaxy Z Fold 3 5G
Samsung Galaxy Z Flip
Samsung Galaxy Z Flip 5G
Samsung Galaxy Z Flip 3 5G
Samsung Galaxy Z Fold 4
Samsung Galaxy Z Flip 4"""
iphone_raw = """iPhone 6
iPhone 6 Plus
iPhone 6S
iPhone 6S Plus
iPhone SE (1st gen)
iPhone 7
iPhone 7 Plus
iPhone 8
iPhone 8 Plus
iPhone X
iPhone XR
iPhone XS
iPhone XS Max
iPhone 11
iPhone 11 Pro
iPhone 11 Pro Max
iPhone SE (2nd gen)
iPhone 12
iPhone 12 mini
iPhone 12 Pro
iPhone 12 Pro Max
iPhone 13
iPhone 13 mini
iPhone 13 Pro
iPhone 13 Pro Max
iPhone SE (3rd gen)
iPhone 14
iPhone 14 Plus
iPhone 14 Pro
iPhone 14 Pro Max"""
tecno_raw = """Spark Plus
Spark Pro
Phantom 6
Pop 1 Lite
Pouvoir 2 Pro
Phantom 6 Plus
Pouvoir 1
Pop 1
Spark CM
Spark
Camon CM
F2 LTE
Camon CX Air
Camon CX
Pouvoir 2
Pop 1 Pro
Pop 1 s
Camon X
Spark 2
Camon X Pro
Phantom 8
Camon 11
F2"""

samsung = {
    "company": "Samsung",
    "model": ["Galaxy", "Galaxy Note", "Galaxy Tab", "Galaxy Z"],
    "series": ['A01', '8', 'A73', 'A80', 'S8', 'S7', 'A71', 'A51', 'A40', 'A70',
               'A6', 'A7', 'A41', 'Fold', 'A20', '7', '9', '10', 'A2', 'A3',
               'A60', 'S9', 'A33', 'S22', 'A5', 'A12', 'A8', 'Edge', '5',
               '3', 'Pro', 'A32', 'A03', 'S21', 'S6', 'A31', 'A02', 'A72', 'A23', '20',
               'A21', 'A90', '4', 'A52', 'A', 'S20', 'FE', 'A22', 'A13', 'Flip', 'A50',
               'A53', 'S10', 'A42', 'A9', 'A10', 'A30'],
    "version": ['10.1', 'FE', 'Ultra', 'V', 'Star', 'Star ', '8.0', '2', 'Core', '+',
                '7.0', '4', '10.5', '9.7', 'Neo', 'Quantum', '12.2', 'e', 'Lite 7.0',
                's', 'UW', '10.4', 'Lite', 'Nacho', '3', 'Pro', 'Duos', 'Neo Duos',
                'Lite 7.0 VE', '8.4']
}
apple = {
    "company": "Apple",
    "model": ["iPhone"],
    "series": ['7', 'SE', '6', '8', '11', '12', 'XS', '14', '6S', 'XR', '13', 'X'],
    "version": ['3rd gen', 'Pro', 'Max', '2nd gen', 'Pro Max', '1st gen', 'mini', 'Plus']
}
tecno = {
    "company": "Tecno",
    "model": ['Camon', 'Phantom', 'Pouvoir', 'Spark', 'Pop', 'F2'],
    "series": ['8', '2', 'CX', 'X', '11', '6', 'CM', 'LTE', '1'],
    "version": ['Lite', 'Air', 's', 'Pro', 'Plus']
}

samsung_variation = {
    "company": {"Samsung": ['Samsung', 'Sam', 'Sm', 'Smg', 'Ss', 'Ssg', 'Samsung', 'Sam', 'Sm', 'Smg', 'Ss', 'Ssg', 'samsung']},
    "model": {"Galaxy": ['Galaxy', 'Gal', 'Glx', 'Glxy', 'Galaxy', 'Galaxy', 'Gal', 'Gal', 'Glx', 'Glx', 'Glxy', 'Glxy', 'galaxy'],
              "Galaxy Note": ['Not', 'GalaxyNot', 'Note', 'GalaxyNote', 'GalNot', 'Glx Nte', 'Nte', 'Gal Note', 'GlxNte', 'GlxNt', 'GalNote', 'Nt', 'Gal Not', 'Glx Nt', 'Galaxy Note', 'Galaxy Not'],
              "Galaxy Tab": ['Galaxy Tab', 'Tb', 'Gal Tab', 'GalTab', 'T', 'Glx T', 'Glx Tb', 'GalaxyTab', 'GlxTb', 'Tab', 'GlxT'],
              "Galaxy Z": ['GalZ', 'Z', 'Galaxy Z', 'GalaxyZ', 'Glx Z', 'Gal Z', 'GlxZ']},
    "series": ['A01', '8', 'A73', 'A80', 'S8', 'S7', 'A71', 'A51', 'A40', 'A70',
               'A6', 'A7', 'A41', 'Fold', 'A20', '7', '9', '10', 'A2', 'A3',
               'A60', 'S9', 'A33', 'S22', 'A5', 'A12', 'A8', 'Edge', '5',
               '3', 'Pro', 'A32', 'A03', 'S21', 'S6', 'A31', 'A02', 'A72', 'A23', '20',
               'A21', 'A90', '4', 'A52', 'A', 'S20', 'FE', 'A22', 'A13', 'Flip', 'A50',
               'A53', 'S10', 'A42', 'A9', 'A10', 'A30'],
    "version": ['10.1', 'FE', 'Ultra', 'V', 'Star', 'Star ', '8.0', '2', 'Core', '+',
                '7.0', '4', '10.5', '9.7', 'Neo', 'Quantum', '12.2', 'e', 'Lite 7.0',
                's', 'UW', '10.4', 'Lite', 'Nacho', '3', 'Pro', 'Duos', 'Neo Duos',
                'Lite 7.0 VE', '8.4']
}

#퍼뮤테이션 알고리즘// 재귀함수를 이용한 조합 만들기 출처, https://kjhoon0330.tistory.com/15
def combination(arr, n):
    out = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        t = arr[i]
        for e in t:
            for rest in combination(arr[i+1:], n-1):
                out.append([e] + rest)
    return out

# make variation
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
            t=t+w
        variations.append(t)

    # 2rd rule : 모음앞에 있는 단어 조합
    temp = re.findall(r"(\w{0,2})[aeiouy]", str, re.IGNORECASE) # 모음 앞에 있는 녀석들 추출
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
            t=t+w
        variations.append(t)
        variations.append(t+str[-1])

    #대문자 기준으로 나누기 + 붙여쓰기, 띄어쓰기 모두 만들기
    arr = []
    for word in variations:
        t=re.findall(r"([A-Z][a-z]*)", word)
        stemp = ""
        for li in t:
            arr.append(li)
            stemp = stemp + " " + li
            stemp = re.findall("\s*(.+)", stemp)[0]
            arr.append(stemp)

    variations = variations + arr

    ##### line에서 찾기 #####
    
    # 첫글자와 끝 글자가 같은 문자
    variations = variations + re.findall(r"{}\w*{}".format(str[0], str[-1]), line, re.IGNORECASE)

    # # lower
    # arr = []
    # for var in variations:
    #     arr.append(var.lower())
    # variations = variations + arr
        
    # # variation하고 같은 문자 찾기
    # output = []
    # for rule in variations:
    #     r1 = r"{}".format(rule.lower())
    #     t = re.findall(r1, line, re.IGNORECASE)
    #     if t:
    #         output.append(t[0])
    # output = list(set(output))
    return variations


##################### trial #####################
line = "samsung galaxy s9+ (fissuré ) 40$ à discuter 0899125152"

out = generate_variation("Galaxy", line)
print(out)

for i in samsung["model"]:
    out3 = []
    out2 = generate_variation(i, line)
    for o2 in out2:
        if not o2 in out:
            out3.append(o2)
    out3 = list(set(out3))
    print(out3)








# # 이거는 tecno
# splited = re.split("\n", tecno_raw)
# for line in splited:
#     model = re.findall("\w+", line)
#     if tecno:
#         tecno["model"].append(model[0])
#         if len(model) >=3:
#             tecno["version"].append(model[2])
#         else:
#             tecno["series"].append(model[1])


# # 이거는 iphone series 찾기
# splited = re.split("\n", iphone_raw)
# for model in apple["model"]:
#     for line in splited:
#         series = re.findall(r"{}\s(\w+)".format(model), line)
#         apple["series"].append(series[0])

# 이거는 iphone version 찾기
# splited = re.split("\n", iphone_raw)
# for model in apple["model"]:
#     for series in apple["series"]:
#         product = "{} {}".format(model, series)
#         for line in splited:
#             version = re.findall(r"{}\s(.+)".format(product), line)
#             if version:
#                 out = re.sub(r"[()]", "", version[0])
#                 apple["version"].append(out)

# #이거는 version 찾기
# splited = re.split("\n",samsung_raw)
# for model in samsung["model"]:
#     for series in samsung["series"]:
#         product = "Samsung {} {}".format(model, series)
#         for line in splited:
#             version = re.findall(r"{}\s(.+)".format(product), line)
#             if version:
#                 out = re.sub(r"\s*3G\s*|\s*5G\s*|\s*LTE\s*|\s*\W\d{4}\W\s*|\s*\d{4}\s*|\s*& S Pen\s*|/", "", version[0])
#                 samsung["version"].append(out)
