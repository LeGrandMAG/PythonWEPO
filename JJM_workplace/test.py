import re

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