#take a string and count 8-character palindromes

def count_palindromes(s):
    counter = 0
    for i in range(len(s) - 7):
        if s[i:i+4] == s[i+4:i+8:][::-1]:
            # check if the fifth surrounding letters are the same
            # and thus guarantee that the palindromes are of
            # lenght 8 and no longer
            if s[i-1] != s[i+8]:
                counter +=1
    return counter

#test example - random nucleotides
print(count_palindromes('aaggtgattaattagccggccgtgta'), 'palindromes in a random string')
print()

#example - Zika virus https://www.ncbi.nlm.nih.gov/nuccore/226377833
zika_virus_dna = open('Zika_virus_sequence.txt', 'r')
<<<<<<< HEAD
zika_virus_dna = ''.join(zika_virus_dna.readlines()[1:]) #the string includes the '\n', so it's not 59 palindromes, better:
#tmp = []
#for line in f:
#if line[0] != '#':
#tmp.append(line.strip())
#clean_string = ''.join(tmp)
print(count_palindromes(zika_virus_dna), 'palindromes in Zika virus')
=======
#my solution lines = f.readlines()
# clean_string = ''.join(lines[1:])
#wrong, since the string is interrupted by \n
tmp = []
for line in zika_virus_dna:
    if line[0] != '#':
        tmp.append(line.strip())
    zika_virus_dna_string = ''.join(tmp)

print(count_palindromes(zika_virus_dna_string), 'palindromes in Zika virus')
>>>>>>> edf51c0 (upd)
