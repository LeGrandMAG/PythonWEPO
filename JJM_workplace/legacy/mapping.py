import re
import pandas as pd
from itertools import permutations

allproducts = {'Samsung Galaxy Tab S7 FE': ['tab s7 fe', 'tab_s7_fe', 'tabs7fe'], 'Samsung Galaxy S10 5G': ['s10'], 'Samsung Galaxy A8 Duos': ['a8duos', 'a8_duos', 'a8 duos'], 'Samsung Galaxy A01 Core': ['a01core', 'a01 core', 'a01_core'], 'Samsung Galaxy A8 Star ': ['a8_star_', 'a8 star ', 'a8star'], 'Samsung Galaxy A6 +': ['a6 +', 'a6_+', 'a6+'], 'Samsung Galaxy A30 s': ['a30 s', 'a30_s', 'a30s'], 'Samsung Galaxy S20 Ultra LTE': ['s20 ultra', 's20ultra', 's20_ultra'], 'Samsung Galaxy Tab S 8.4 LTE': ['tabs8.4', 'tab_s_8.4', 'tab s 8.4'], 'Samsung Galaxy Tab S8': ['tab_s8', 'tabs8', 'tab s8'], 'Samsung Galaxy S10 e': ['s10_e', 's10e', 's10 e'], 'Samsung Galaxy A02 s': ['a02 s', 'a02_s', 'a02s'], 'Samsung Galaxy Tab S6': ['tab_s6', 'tab s6', 'tabs6'], 'Samsung Galaxy A72': ['a72'], 'Samsung Galaxy Tab S 8.4': ['tabs8.4', 'tab_s_8.4', 'tab s 8.4'], 'Samsung Galaxy S22 + 5G': ['s22 +', 's22+', 's22_+'], 'Samsung Galaxy Tab S2 9.7': ['tab s2 9.7', 'tab_s2_9.7', 'tabs29.7'], 'Samsung Galaxy S10': ['s10'], 'Samsung Galaxy S9': ['s9'], 'Samsung Galaxy Tab A 8.0': ['tab a 8.0', 'tab_a_8.0', 'taba8.0'], 'Samsung Galaxy Tab 4 10.1': ['tab410.1', 'tab 4 10.1', 'tab_4_10.1'], 'Samsung Galaxy Z Flip 3 5G': ['z_flip_3', 'z flip 3', 'zflip3'], 'Samsung Galaxy S9 +': ['s9_+', 's9+', 's9 +'], 'Samsung Galaxy A12 Nacho': ['a12nacho', 'a12 nacho', 'a12_nacho'], 'Samsung Galaxy Tab S4 10.5': ['tabs410.5', 'tab_s4_10.5', 'tab s4 10.5'], 'Samsung Galaxy A8 s': ['a8_s', 'a8s', 'a8 s'], 'Samsung Galaxy Tab 3 V': ['tab_3_v', 'tab3v', 'tab 3 v'], 'Samsung Galaxy Tab Pro 12.2 3G': ['tab_pro_12.2', 'tabpro12.2', 'tab pro 12.2'], 'Samsung Galaxy A01': ['a01'], 'Samsung Galaxy Tab S8 Ultra': ['tabs8ultra', 'tab s8 ultra', 'tab_s8_ultra'], 'Samsung Galaxy Tab A8 10.5': ['tab_a8_10.5', 'tab a8 10.5', 'taba810.5'], 'Samsung Galaxy A10': ['a10'], 'Samsung Galaxy A6': ['a6'], 'Samsung Galaxy Tab A 8.0 & S Pen': ['tab a 8.0 & s pen', 'taba8.0&spen', 'tab_a_8.0_&_s_pen'], 'Samsung Galaxy Z Fold 4': ['z_fold_4', 'zfold4', 'z fold 4'], 'Samsung Galaxy Fold': ['fold'], 'Samsung Galaxy A21': ['a21'], 'Samsung Galaxy S6': ['s6'], 'Samsung Galaxy Tab 4 7.0': ['tab_4_7.0', 'tab 4 7.0', 'tab47.0'], 'Samsung Galaxy Tab S6 5G': ['tab_s6', 'tab s6', 'tabs6'], 'Samsung Galaxy Z Flip 5G': ['z_flip', 'z flip', 'zflip'], 'Samsung Galaxy A50': ['a50'], 'Samsung Galaxy A40': ['a40'], 'Samsung Galaxy A32 5G': ['a32'], 'Samsung Galaxy S20 + 5G': ['s20 +', 's20+', 's20_+'], 'Samsung Galaxy S20 FE': ['s20 fe', 's20fe', 's20_fe'], 'Samsung Galaxy S22 5G': ['s22'], 'Samsung Galaxy A8': ['a8'], 'Samsung Galaxy Tab A7 10.4': ['tab a7 10.4', 'tab_a7_10.4', 'taba710.4'], 'Samsung Galaxy A12': ['a12'], 'Samsung Galaxy A9 Pro': ['a9 pro', 'a9pro', 'a9_pro'], 'Samsung Galaxy Tab 4 7.0 LTE': ['tab_4_7.0', 'tab 4 7.0', 'tab47.0'], 'Samsung Galaxy Fold 5G': ['fold'], 'Samsung Galaxy A02': ['a02'], 'Samsung Galaxy Note 20 Ultra 5G': ['note20ultra', 'note 20 ultra', 'note_20_ultra'], 'Samsung Galaxy Z Flip 4': ['z flip 4', 'z_flip_4', 'zflip4'], 'Samsung Galaxy Note Pro 12.2 5G': ['note pro 12.2', 'note_pro_12.2', 'notepro12.2'], 'Samsung Galaxy Tab S7 +': ['tab_s7_+', 'tabs7+', 'tab s7 +'], 'Samsung Galaxy A03': ['a03'], 'Samsung Galaxy Note Pro 12.2': ['note pro 12.2', 'note_pro_12.2', 'notepro12.2'], 'Samsung Galaxy Tab S 10.5 LTE': ['tab s 10.5', 'tab_s_10.5', 'tabs10.5'], 'Samsung Galaxy A60': ['a60'], 'Samsung Galaxy Tab Pro 8.4 3G/LTE': ['tabpro8.4', 'tab pro 8.4', 'tab_pro_8.4'], 'Samsung Galaxy A7 Duos': ['a7_duos', 'a7duos', 'a7 duos'], 'Samsung Galaxy Note 10 + 5G': ['note10+', 'note_10_+', 'note 10 +'], 'Samsung Galaxy Note 20': ['note 20', 'note_20', 'note20'], 'Samsung Galaxy Tab A 9.7': ['taba9.7', 'tab a 9.7', 'tab_a_9.7'], 'Samsung Galaxy Tab A 7.0': ['taba7.0', 'tab a 7.0', 'tab_a_7.0'], 'Samsung Galaxy A20 s': ['a20s', 'a20_s', 'a20 s'], 'Samsung Galaxy Note 20 5G': ['note 20', 'note_20', 'note20'], 'Samsung Galaxy A33 5G': ['a33'], 'Samsung Galaxy Tab A 10.1': ['tab_a_10.1', 'taba10.1', 'tab a 10.1'], 'Samsung Galaxy Note 10 5G': ['note10', 'note_10', 'note 10'], 'Samsung Galaxy A52': ['a52'], 'Samsung Galaxy A9 Star': ['a9_star', 'a9 star', 'a9star'], 'Samsung Galaxy Z Fold 3 5G': ['zfold3', 'z fold 3', 'z_fold_3'], 'Samsung Galaxy A21 s': ['a21_s', 'a21s', 'a21 s'], 'Samsung Galaxy Tab 4 8.0': ['tab 4 8.0', 'tab_4_8.0', 'tab48.0'], 'Samsung Galaxy Note 3 Neo': ['note_3_neo', 'note 3 neo', 'note3neo'], 'Samsung Galaxy Tab A & S Pen': ['tab a & s pen', 'tab_a_&_s_pen', 'taba&spen'], 'Samsung Galaxy A9': ['a9'], 'Samsung Galaxy Tab S6 Lite': ['tabs6lite', 'tab_s6_lite', 'tab s6 lite'], 'Samsung Galaxy Z Flip': ['z_flip', 'z flip', 'zflip'], 'Samsung Galaxy A71 5G UW': ['a71uw', 'a71 uw', 'a71_uw'], 'Samsung Galaxy Tab Active3': ['tabactive3', 'tab_active3', 'tab active3'], 'Samsung Galaxy Tab S8 +': ['tabs8+', 'tab s8 +', 'tab_s8_+'], 'Samsung Galaxy A32': ['a32'], 'Samsung Galaxy A22 5G': ['a22'], 'Samsung Galaxy A51': ['a51'], 'Samsung Galaxy Tab Active Pro': ['tab_active_pro', 'tab active pro', 'tabactivepro'], 'Samsung Galaxy Tab S3 9.7': ['tab s3 9.7', 'tab_s3_9.7', 'tabs39.7'], 'Samsung Galaxy Tab E 8.0': ['tabe8.0', 'tab e 8.0', 'tab_e_8.0'], 'Samsung Galaxy A73 5G': ['a73'], 'Samsung Galaxy Note 4 Duos': ['note_4_duos', 'note4duos', 'note 4 duos'], 'Samsung Galaxy A50 s': ['a50s', 'a50_s', 'a50 s'], 'Samsung Galaxy Note 5 Duos': ['note5duos', 'note_5_duos', 'note 5 duos'], 'Samsung Galaxy Note FE': ['note_fe', 'note fe', 'notefe'], 'Samsung Galaxy A03 Core': ['a03core', 'a03_core', 'a03 core'], 'Samsung Galaxy A23': ['a23'], 'Samsung Galaxy A6 s': ['a6_s', 'a6 s', 'a6s'], 'Samsung Galaxy S8 +': ['s8+', 's8_+', 's8 +'], 'Samsung Galaxy A51 5G': ['a51'], 'Samsung Galaxy S20 Ultra 5G': ['s20 ultra', 's20ultra', 's20_ultra'], 'Samsung Galaxy A3 Duos': ['a3 duos', 'a3duos', 'a3_duos'], 'Samsung Galaxy Tab 3 Lite 7.0 3G': ['tab 3 lite 7.0', 'tab3lite7.0', 'tab_3_lite_7.0'], 'Samsung Galaxy Tab 4 8.0 3G': ['tab 4 8.0', 'tab_4_8.0', 'tab48.0'], 'Samsung Galaxy A13': ['a13'], 'Samsung Galaxy S8': ['s8'], 'Samsung Galaxy Note 10 +': ['note10+', 'note_10_+', 'note 10 +'], 'Samsung Galaxy Note 20 Ultra': ['note20ultra', 'note 20 ultra', 'note_20_ultra'], 'Samsung Galaxy A10 e': ['a10_e', 'a10 e', 'a10e'], 'Samsung Galaxy Tab A7 Lite': ['tab a7 lite', 'tab_a7_lite', 'taba7lite'], 'Samsung Galaxy S22 Ultra 5G': ['s22ultra', 's22 ultra', 's22_ultra'], 'Samsung Galaxy Note 3 Neo Duos': ['note3neoduos', 'note_3_neo_duos', 'note 3 neo duos'], 'Samsung Galaxy Note 5': ['note_5', 'note5', 'note 5'], 'Samsung Galaxy Note Pro 12.2 LTE': ['note pro 12.2', 'note_pro_12.2', 'notepro12.2'], 'Samsung Galaxy A52 5G': ['a52'], 'Samsung Galaxy A53 5G': ['a53'], 'Samsung Galaxy Note 4': ['note_4', 'note 4', 'note4'], 'Samsung Galaxy S21 + 5G': ['s21 +', 's21+', 's21_+'], 'Samsung Galaxy A41': ['a41'], 'Samsung Galaxy A2 Core': ['a2_core', 'a2core', 'a2 core'], 'Samsung Galaxy Note 9': ['note 9', 'note_9', 'note9'], 'Samsung Galaxy Note 10 Lite': ['note_10_lite', 'note10lite', 'note 10 lite'], 'Samsung Galaxy Tab Pro 12.2 LTE': ['tab_pro_12.2', 'tabpro12.2', 'tab pro 12.2'], 'Samsung Galaxy Note Edge': ['note_edge', 'note edge', 'noteedge'], 'Samsung Galaxy Note 10': ['note10', 'note_10', 'note 10'], 'Samsung Galaxy Tab 4 10.1 LTE': ['tab410.1', 'tab 4 10.1', 'tab_4_10.1'], 'Samsung Galaxy Tab J': ['tab j', 'tab_j', 'tabj'], 'Samsung Galaxy S21 5G': ['s21'], 'Samsung Galaxy A13 5G': ['a13'], 'Samsung Galaxy A70': ['a70'], 'Samsung Galaxy Tab 3 Lite 7.0 VE': ['tab3lite7.0ve', 'tab 3 lite 7.0 ve', 'tab_3_lite_7.0_ve'], 'Samsung Galaxy Note 8': ['note_8', 'note 8', 'note8'], 'Samsung Galaxy A71 5G': ['a71'], 'Samsung Galaxy A10 s': ['a10s', 'a10_s', 'a10 s'], 'Samsung Galaxy A42 5G': ['a42'], 'Samsung Galaxy A03 s': ['a03s', 'a03 s', 'a03_s'], 'Samsung Galaxy Tab Pro 12.2': ['tab_pro_12.2', 'tabpro12.2', 'tab pro 12.2'], 'Samsung Galaxy Tab E 9.6': ['tab e 9.6', 'tab_e_9.6', 'tabe9.6'], 'Samsung Galaxy A22': ['a22'], 'Samsung Galaxy S10 +': ['s10+', 's10_+', 's10 +'], 'Samsung Galaxy A5': ['a5'], 'Samsung Galaxy Tab S5 e': ['tabs5e', 'tab s5 e', 'tab_s5_e'], 'Samsung Galaxy A90 5G': ['a90'], 'Samsung Galaxy Tab Pro 8.4': ['tabpro8.4', 'tab pro 8.4', 'tab_pro_8.4'], 'Samsung Galaxy Tab S 10.5': ['tab s 10.5', 'tab_s_10.5', 'tabs10.5'], 'Samsung Galaxy Tab Advanced2': ['tabadvanced2', 'tab advanced2', 'tab_advanced2'], 'Samsung Galaxy S7': ['s7'], 'Samsung Galaxy Tab S2 8.0': ['tab s2 8.0', 'tabs28.0', 'tab_s2_8.0'], 'Samsung Galaxy A20 e': ['a20e', 'a20_e', 'a20 e'], 'Samsung Galaxy Tab Pro 10.1': ['tab pro 10.1', 'tabpro10.1', 'tab_pro_10.1'], 'Samsung Galaxy A70 s': ['a70_s', 'a70 s', 'a70s'], 'Samsung Galaxy A20': ['a20'], 'Samsung Galaxy A31': ['a31'], 'Samsung Galaxy Tab Pro 10.1 LTE': ['tab pro 10.1', 'tabpro10.1', 'tab_pro_10.1'], 'Samsung Galaxy S20 FE 5G': ['s20 fe', 's20fe', 's20_fe'], 'Samsung Galaxy A51 5G UW': ['a51_uw', 'a51 uw', 'a51uw'], 'Samsung Galaxy Z Fold 2 5G': ['z fold 2', 'zfold2', 'z_fold_2'], 'Samsung Galaxy Tab 4 8.0 LTE': ['tab 4 8.0', 'tab_4_8.0', 'tab48.0'], 'Samsung Galaxy Tab S7': ['tab_s7', 'tabs7', 'tab s7'], 'Samsung Galaxy S21 Ultra 5G': ['s21 ultra', 's21ultra', 's21_ultra'], 'Samsung Galaxy Note 7': ['note7', 'note_7', 'note 7'], 'Samsung Galaxy Tab A 8.4': ['taba8.4', 'tab a 8.4', 'tab_a_8.4'], 'Samsung Galaxy A71': ['a71'], 'Samsung Galaxy A5 Duos': ['a5 duos', 'a5duos', 'a5_duos'], 'Samsung Galaxy A3': ['a3'], 'Samsung Galaxy S21 FE 5G': ['s21 fe', 's21_fe', 's21fe'], 'Samsung Galaxy Tab A 10.5': ['taba10.5', 'tab_a_10.5', 'tab a 10.5'], 'Samsung Galaxy S20': ['s20'], 'Samsung Galaxy A30': ['a30'], 'Samsung Galaxy Tab 4 10.1 3G': ['tab410.1', 'tab 4 10.1', 'tab_4_10.1'], 'Samsung Galaxy Tab 4 7.0 3G': ['tab_4_7.0', 'tab 4 7.0', 'tab47.0'], 'Samsung Galaxy A52 s 5G': ['a52_s', 'a52 s', 'a52s'], 'Samsung Galaxy A Quantum': ['a_quantum', 'a quantum', 'aquantum'], 'Samsung Galaxy S20 5G': ['s20'], 'Samsung Galaxy Tab 3 Lite 7.0': ['tab 3 lite 7.0', 'tab3lite7.0', 'tab_3_lite_7.0'], 'Samsung Galaxy Tab Active 2': ['tabactive2', 'tab_active_2', 'tab active 2'], 'Samsung Galaxy A7': ['a7'], 'Samsung Galaxy A80': ['a80'], 'Samsung Galaxy S20 +': ['s20 +', 's20+', 's20_+'], 'iPhone 7': ['7'], 'iPhone 14 Plus': ['14_+', '14_plus', '14+', '14 +', '14plus', '14 plus'], 'iPhone 11 Pro Max': ['11 pro max', '11promax', '11_pro_max'], 'iPhone 6S Plus': ['6s +', '6s plus', '6s_plus', '6s+', '6splus', '6s_+'], 'iPhone 14 Pro': ['14_pro', '14pro', '14 pro'], 'iPhone 6S': ['6s'], 'iPhone XS': ['xs'], 'iPhone 8': ['8'], 'iPhone 8 Plus': ['8 +', '8+', '8_+', '8 plus', '8plus', '8_plus'], 'iPhone SE (2nd gen)': ['se 2 gen', 'se_2nd_gen', 'se2gen', 'se 2nd gen', 'se_2_gen', 'se2ndgen', 'se 2', 'se2'], 'iPhone 11': ['11'], 'iPhone SE (1st gen)': ['se_1st_gen', 'se1stgen', 'se 1st gen', 'se1gen', 'se_1_gen', 'se 1 gen', 'se', 'se 1', 'se1'], 'iPhone 6': ['6'], 'iPhone X': ['x'], 'iPhone 11 Pro': ['11pro', '11_pro', '11 pro'], 'iPhone SE (3rd gen)': ['se_3_gen', 'se_3rd_gen', 'se 3rd gen', 'se3rdgen', 'se 3 gen', 'se3gen', 'se 3', 'se3'], 'iPhone XR': ['xr'], 'iPhone 13 mini': ['13 mini', '13_mini', '13mini'], 'iPhone 12 Pro Max': ['12_pro_max', '12promax', '12 pro max'], 'iPhone 12': ['12'], 'iPhone XS Max': ['xsmax', 'xs_max', 'xs max'], 'iPhone 12 Pro': ['12pro', '12_pro', '12 pro'], 'iPhone 13': ['13'], 'iPhone 6 Plus': ['6plus', '6+', '6 +', '6_+', '6_plus', '6 plus'], 'iPhone 14': ['14'], 'iPhone 12 mini': ['12mini', '12_mini', '12 mini'], 'iPhone 7 Plus': ['7 +', '7+', '7_plus', '7_+', '7plus', '7 plus'], 'iPhone 14 Pro Max': ['14 pro max', '14_pro_max', '14promax'], 'iPhone 13 Pro': ['13_pro', '13pro', '13 pro'], 'iPhone 13 Pro Max': ['13 pro max', '13promax', '13_pro_max'], 'Tecno Pouvoir 2 Pro': ['pouvoir2pro', 'pouvoir 2 pro', 'pouvoir_2_pro'], 'Tecno Pop Pro': ['poppro', 'pop pro', 'pop_pro'], 'Tecno Camon CM': ['camoncm', 'camon_cm', 'camon cm'], 'Tecno Camon CX Air': ['camon cx air', 'camoncxair', 'camon_cx_air'], 'Tecno Pop': ['pop'], 'Tecno F2 LTE': ['f2_lte', 'f2 lte', 'f2lte'], 'Tecno Phantom 8': ['phantom_8', 'phantom 8', 'phantom8'], 'Tecno Pop Lite': ['poplite', 'pop_lite', 'pop lite'], 'Tecno Camon X': ['camonx', 'camon_x', 'camon x'], 'Tecno Phantom 6 Plus': ['phantom6+', 'phantom_6_plus', 'phantom 6 +', 'phantom 6 plus', 'phantom6plus', 'phantom_6_+'], 'Tecno Camon 11': ['camon_11', 'camon 11', 'camon11'], 'Tecno Spark Pro': ['spark pro', 'spark_pro', 'sparkpro'], 'Tecno Spark 2': ['spark_2', 'spark 2', 'spark2'], 'Tecno Phantom 6': ['phantom6', 'phantom_6', 'phantom 6'], 'Tecno Camon CX': ['camon_cx', 'camon cx', 'camoncx'], 'Tecno Pop s': ['pop_s', 'pop s', 'pops'], 'Tecno Pouvoir': ['pouvoir'], 'Tecno Spark Plus': ['spark_plus', 'sparkplus', 'spark_+', 'spark +', 'spark plus', 'spark+'], 'Tecno Spark': ['spark'], 'Tecno F2': ['f2'], 'Tecno Camon X Pro': ['camon x pro', 'camonxpro', 'camon_x_pro'], 'Tecno Spark CM': ['spark cm', 'spark_cm', 'sparkcm'], 'Tecno Pouvoir 2': ['pouvoir_2', 'pouvoir 2', 'pouvoir2']}

rawDf = pd.read_csv("facebookData_withProduct")
# object to list
rawDf['product'] = rawDf['product'].apply(lambda x : re.sub("'", "" , x))
rawDf['product'] = rawDf['product'].apply(lambda x : x[1:-1].split(', '))
fomalName = []

for token in rawDf['product']:
    # 단어 수준
    compareWords = []
    compareWords = compareWords + token

    # 단어가 2개 이상일 경우 조합
    if len(token) == 2:
        compareWords.append(' '.join(token))

    # 단어가 3개 이상일 경우 조합
    elif len(token) >= 3:
        for a in permutations(token, 2):
            compareWords.append(' '.join(a))
        for b in permutations(token, 3):
            compareWords.append(' '.join(b))
    temp = []

    # 비교 시작
    for var in compareWords:
        point = 0
        for productName in allproducts:
            if var in allproducts[productName]:
                temp.append(productName)

    fomalName.append(temp)

final = []
# 전체 연결후 아닌거 빼내기

for i in range(len(fomalName)):
    arr = []
    if len(fomalName[i]) >= 2:
        print(fomalName[i])
        g = 0
        allNew = ""
        for candidate in fomalName[i]:
            p = 0
            temp = candidate.lower()
            tempArr = temp.split(' ')
            for t in tempArr:
                f = re.findall("{}".format(t), rawDf['raw'][i])
                if f:
                    p = p + 1
                    allNew = allNew + " {}".format(f[0])
                    g = g + p
            arr.append((p, temp))
            # # 조합해보기
            # if candidate == fomalName[i][-1]:
            #     print('hi')
            #     arr.append((g, allNew[1:]))
        final.append(arr)
print(final)
# for nameList in fomalName:
#     if len(nameList) >= 2:
#         print(nameList)
#         for candidate in nameList:
#             p = 0
#             temp = candidate.lower()
#             tempArr = temp.split(' ')
#             for t in tempArr:
#                 for line in rawDf['raw']:
#                     f = re.findall("{}".format(t), str(line))
#                     if f:
#                         p = p + len(f)
#                         print(f, p, len(f))
#             final.append((candidate, point))
# print(final)


# for i in range(len(fomalName)):
#     print(i, rawDf['raw'][i], fomalName[i])
