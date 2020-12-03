wordlist = open("wordlist.txt", "r").read().split("\n")
matrix = open("matrix.txt", "r").read()

for i in wordlist:
    if(str(i) in matrix):
        wordlist.remove(i)
    elif("".join((reversed(str(i)))) in matrix):
        wordlist.remove(i)

print(", ".join(wordlist))











