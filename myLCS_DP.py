import sys 
import random 

def randomSeq(n): #random dna sequence of length n
    seq = ""
    conversion = {0:'A',1:'T',2:'C',3:'G'}
    for i in range(0, n):
        seq += conversion[random.randint(0,3)]
    return seq

def lcs(dna1, dna2): 
    print(dna1, dna2)

    opt = [] 
    for i in range(0,len(dna1)+1):
        row = []
        for i in range(0,len(dna2)+1):
            row.append(0)
        opt.append(row)

    for i in range(1, len(opt[0])):
        opt[0][i] = opt[0][i-1]
    for i in range(1, len(opt)):
        opt[i][0] = opt[i-1][0]
    
    for i in range(1, len(opt)):
        for j in range(1, len(opt[0])):
            scores = [0,0,0]
            if dna1[i-1] == dna2[j-1]: #diagonal
                scores[0] = opt[i-1][j-1] + 1
            else:
                scores[0] = opt[i-1][j-1]
            scores[1] = opt[i][j-1] #left/right gap
            scores[2] = opt[i-1][j] #up/down gap
            opt[i][j] = max(scores)
    
    print("Intermediate Values Table:")
    for i in range(0,len(opt)):
        print(opt[i])
    first = ''        # alignment for dna1
    second = ''       # alignment for dna2

    i = len(dna1)
    j = len(dna2) 
        
    while i != 0 or j != 0:
        if j != 0 and opt[i][j] == (opt[i][j-1]):
            first = '-' + first
            second = dna2[j-1] + second
            j -= 1
        elif i != 0 and opt[i][j] == (opt[i-1][j]):
            second = '-' + second
            first = dna1[i-1] + first
            i -= 1
        elif opt[i][j] == (opt[i-1][j-1] + 1) or opt[i][j] == (opt[i-1][j-1]):
            first = dna1[i-1] + first
            second = dna2[j-1] + second
            j -= 1
            i -= 1
            
    longComSeq = ""
    for i in range(0, len(first)):
        if first[i] == second[i]:
            longComSeq += first[i]
    if len(longComSeq) == 0:
        print("These two genomes have no common sequence")
    else:
        print('LCS','"{}"'.format(longComSeq),'has length',len(longComSeq))
   
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

