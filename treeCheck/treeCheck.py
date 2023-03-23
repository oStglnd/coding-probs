
tree1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
tree2 = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
tree3 = ["(2,3)", "(4,3)", "(5,4)", "(1,2)", "(7,4)", "(8,2)"]


def numOccurence(L):
    
    maxCount = 0
    for idx, elem in enumerate(L[:-1]):    
        counter = 1
        for comp in L[idx+1:]:
            if elem == comp:
                counter += 1
                maxCount = max(maxCount, counter)
            
    return maxCount
    

def treeCheck(tree):
    
    parents = [pair.split(',')[-1][0] for pair in tree]
    children = [pair.split(',')[0][-1] for pair in tree]
    
    parentsCheck = numOccurence(parents) < 3
    childrenCheck = numOccurence(children) < 2
    
    return bool(parentsCheck * childrenCheck)

print(treeCheck(tree1))
print(treeCheck(tree2))
print(treeCheck(tree3))