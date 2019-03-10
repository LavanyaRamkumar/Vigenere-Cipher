import string
import random
import re
from nltk.corpus import brown
import copy
from nltk.probability import FreqDist
import sys

TEST_FILE = "input.txt"
alphabets = "abcdefghijklmnopqrstuvwxyz"

fq=FreqDist([word.lower() for word in brown.words()[:1000000]] )
print("freq table built")

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      p += alphabets[pos].lower()
      i +=1
    return p


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


def findBestShift(string):
    count=len(string)
    bestShift=""
    for shift in l:
        newWords = decrypt(string, shift)
        newWord = findmostlikelytokens(newWords,fq)
        if(len(newWord) <= count):
            print(shift)
            print(newWord)
            count = len(newWord)
            bestShift = shift
        # print(newWord)
        # print(shift)
        # print()
    return bestShift

def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)

def printAllKLengthRec(set, prefix, n, k):
    if (k == 0) :
        l.append(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)


def run(st):
    print(st)
    print((".")*100)
    best = findBestShift(st)
    print("")
    print("Chiper Test = " + st)
    print("Best fit key is = " + str(best))
    print("Plain Text is = " + " ".join(findmostlikelytokens(decrypt(st,best),fq)))
    print(" ")
    print(" ")
    print((".")*100)


# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha = ["n","c","e"]

k = 3

print("finding all permuntaions of size" + str(k))
l = list()
printAllKLength(alpha,k)
print("running all codes")

testFile = open(TEST_FILE, 'r')
wordList = testFile.read().split("\n")
for st in wordList:
	run(st.replace(" ",""))
