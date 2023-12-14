# Intro-to-CS-Final
<h2>Longest Common Sequence</h2>
Finds the longest common sequence of two DNA sequences by using a Needleman-Wunsch algorithm.

Two scripts are provided, one uses dynamic programming (myLCS_DP.py) while the other uses recursion (myLCS_Re.py) <br />
Notable differences include:
1. DP version executes much faster
2. DP version will display the table it used to generate the LCS
3. DP version will display the LCS it generated

<h2>Usage</h2> 
Either script can be executed in the python command line. For instance: <br />
<code>python myLCS_DP.py arg1 arg2</code> <br />

Arguments can include: 
1. Two DNA sequences. The program will simply generate the LCS of the two given sequences.
2. One integer *n*. The program will create two random DNA sequences of length *n* and generate the LCS.
3. No arguments. The program will create two random DNA sequences of length 12 and generate the LCS.
