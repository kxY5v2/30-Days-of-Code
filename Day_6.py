'''
Objective:
    Today we will expand our knowledge of strings, combining it with what we 
    have already learned about loops. Check out the Tutorial tab for learning
    materials and an instructional video.

Task:
    Given a string, S, of length N that is indexed from 0 to N - 1,
    print its even indexed and odd-indexed characters as 2 space-separated
    strings on a single line (see the Sample below for mroe detail).

Note:
    0 is considered to be an even index

Example:
    s= adbecf
    print abc def

Input Format:
    The first line contains an integer, T (the number of test cases).
    Each line i of the T subsequent line contain the string, S.

Constraints:
    1 <= T <= 10
    2 <= length of S <= 1000

Output Format:
   For each string S(j) (where 0 <= j <= T - 1), print S(j)'s even-indexed
   characters, followed by a space, followed by S(j)'s odd-indexed chacters

Sample Input:
    2
    Hacker
    Rank

Sample Output:
    Hce akr
    Rn ak

Explanation:
    Test Case 0: S = "Hacker"
        S[0] = "H"
        S[1] = "a"
        S[2] = "c"
        S[3] = "k"
        S[4] = "e"
        S[5] = "r"
    The even indicies are 0, 2, and 4, and the odd indicies are 1, 3, and 5.
    We then print a single line of 2 space-separated strings; the first string
    contains the from S's even indicies (Hce), and second string contains
    the ordered characters from S's odd indicies (akr).
    Test Case 0: S = "Rank"
        S[0] = "R"
        S[1] = "a"
        S[2] = "n"
        S[3] = "k"
    The even indicies are 0 and 2, and the odd indicies are 1 and 3. We then
    print a single line of 2 space-separated strings; the first string contains the 
    ordered characters from S's even indicies (Rn), and then second string
    contains the ordered charaters from S's odd indicies.
'''

if __name__ == "__main__":
    t = int(input())
    string_arr = []
    i = 0
    while i <= t-1:
        str = input()
        string_arr.append(str)
        i += 1
    for word in string_arr:
        print(word[::2], word[1::2])
