import sys
import random

def randomSeq(n): #random dna sequence of length n
    seq = ""
    conversion = {0:'A',1:'T',2:'C',3:'G'}
    for i in range(0, n):
        seq += conversion[random.randint(0,3)]
    return seq

def lcs(dna1, dna2): 
    def score(x=len(dna2), y=len(dna1)):
        if x == 0 and y == 0:
            return 0
        elif x == 0:
            return score(x, y-1)
        elif y == 0:
            return score(x-1, y)
        
        if (((dna1[y-1] == dna2[x-1]) and (score(x-1, y-1) >= score(x-1, y)) and (score(x-1, y-1) >= score(x,y-1)))):
            return 1 + score(x-1, y-1)
        elif score(x-1, y) > score(x, y-1):
            return score(x-1, y)
        else:
            return score(x, y-1)
    print("DNA1:",dna1,"DNA2:",dna2)
    print("LCS has length:",score())

if len(sys.argv) == 1:
    seq1 = randomSeq(12)
    seq2 = randomSeq(12)
elif sys.argv[1].isdigit():
    digit = int(sys.argv[1])
    seq1 = randomSeq(digit)
    seq2 = randomSeq(digit)
else:
    seq1 = sys.argv[1]
    seq2 = sys.argv[2]

lcs(seq1,seq2)
