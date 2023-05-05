
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

def findSubstring(s: str, words: list) -> list:
    
    subStrLen = len(words) * len(words[0])
    
    if len(s) < subStrLen: 
        return []
    
    else:
        sLen = len(s) // len(words)
        wordLen = len(words[0])
        subStrings = [s[idx*wordLen:idx*wordLen+subStrLen] for idx in range(sLen)]
        print(subStrings)
        
        subStrIdxs = []
        for idx, subStr in enumerate(subStrings):
            
            validStr = True
            if len(subStr) == subStrLen:
                for word in words:
                    if word not in subStr:
                        validStr = False
                    else:
                        subStr = subStr.replace(word, '')
                
                if validStr == True:
                    subStrIdxs.append(idx * len(word))
                
        return subStrIdxs
                