from nltk.corpus import brown
import copy
from nltk.probability import FreqDist


def findmostlikelytokens(testsentence, fq):
    stack=[([], testsentence)]
    resultlist=[]
    while len(stack) > 0:
        currentlist, sentence=stack.pop(0)
        if len(sentence)==0:
            resultlist.append(currentlist)
        for i in range(0, len(sentence)+1):
            if sentence[0:i] in fq:
                newlist=copy.deepcopy(currentlist)
                newlist.append(sentence[0:i])
                stack.append((newlist, sentence[i:]))
    finallist=sorted(resultlist, key=(lambda x: scorelist(x)), reverse=True)
    return ( finallist[0])

def scorelist(liste):
    global fq
    summe=0
    for value in liste:
        summe+=fq[value]**len(value)
    #print(str(liste)+ " : " + str(summe))
    return summe/len(liste)

if __name__=="__main__":
    fq=FreqDist([word.lower() for word in brown.words()[:1000000]] )
    print(fq["m"])
    while True:
        print(findmostlikelytokens(input("Next sentence to tokenize: "), fq))
