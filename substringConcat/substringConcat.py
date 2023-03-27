
input1 = ('barfoothefoobarman', ['foo', 'bar'])
input2 = ('barfoofoobarthefoobarman', ["bar","foo","the"])


def getWords(wordList):
    
    words = []
    words.append(''.join(wordList))
    
    if len(wordList) >= 3:
        for i in range(1, len(wordList)):
            words.append(''.join(wordList[-i:] + wordList[:-i]))
            
    return words

def substringConcat(inputTup):
    
    s = inputTup[0]
    words = getWords(inputTup[1]) + getWords(inputTup[1][::-1])
    
    idxList = []
    
    for word in words:
        idxList.append(s.find(word))
        sTemp = s.replace(word, '', 1)
        
        while len(sTemp) >= len(word):
            idx = sTemp.find(word)
            if idx == -1:
                break
            else:
                idxList.append(idx) 
                sTemp = sTemp.replace(word, '', 1)
                
    return [i for i in idxList if i != -1]
            