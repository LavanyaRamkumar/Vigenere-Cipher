from itertools import permutations

def printAllKLength(set, k):

    n = len(set)
    printAllKLengthRec(set, "", n, k)
l = list()
def printAllKLengthRec(set, prefix, n, k):
    if (k == 0) :
        l.append(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)

if __name__ == "__main__":
# 	string = "XUKW   LGEE   YINN   WBVL   BWKU   VXUC   XLQY   FJSH   NHNV   PRCW\
# GQRP   GMAA   SHTP   VHIO   TSJU   IGJI   JGFS   QVFQ   QRMM   AFIE\
# IEEV   IAEV   LRXB   VSBN   WNUC   BWWR   GWRX   IECP   BHXU   GQNT\
# INXE   VNEO   NINP   HNTI   DWMG   GEON   IGQT   RTJB   TQNH   VRSY\
# RPGL   CRNN   CFKW   NPHG   JYFV   SRXI   AIYR   UWGJ   IFGG   EGXX\
# GCBH   XUKW   PKTU   GVCN   ELKR   TCVB   WRQY   MGJX   UGQP   CROG\
# EYQX   BHJH   PFHV   RBYT   YGEF   GJBT   KRVE   OQYG   VLVU   EAEM\
# RPXF   VYSH   JBTX   UGVR   UXBH   XUKW   PQYE   UIVP   XUGV   ROEV\
# PHRT   SSVL   RESH   TWRY   IJKP   YHSP   WWBP   QBTI   RNEO   QVNV\
# ISQV   ZUSS   UIPW   VVVC   GJEG   EEAP   SGDI   OTSX   GROA   WHEL\
# NUMZ   RPRV   IPJR   VSYR"
	string = "dpzcqjuqikv"
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	k = 3
	printAllKLength(alpha,k)
	print(l)
	# for keyword in l:
	# 	print (keyword)
	# 	key = generateKey(string, keyword)
	# 	cipher_text = cipherText(string,key)
	# 	print(cipher_text)
		# print("Ciphertext :", cipher_text)
		# print()
		# print("Original/Decrypted Text :",
		# originalText(cipher_text, key))
