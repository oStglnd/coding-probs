
strArr1 = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
strArr2 = ["bananaman", "man,woman,dog,apple,banana,blue"]
strArr3 = ["caterpillar", "cat,pillar,dog,fly,shoes,red"]

def wordChecker(strArr):
    
    doubleWord = strArr[0]
    csvList = strArr[-1].split(',')
    
    csvWord = ','
    for word in csvList:
        if doubleWord.find(word) == 0:
            csvWord = word + csvWord
        elif doubleWord.find(word) > 0:
            csvWord += word
        
    if csvWord.replace(',', '') == doubleWord:
        return csvWord
    else:
        return 'not possible'
    