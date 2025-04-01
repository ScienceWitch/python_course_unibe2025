#take a string and count 8-character palindromes

def count_palindromes(s):
    counter = 0
    for i in range(len(s) - 7):
        if s[i:i+4] == s[i+4:i+8:][::-1]:
            counter +=1
    return counter

#test example - random nucleotides
print(count_palindromes('aaggtgattaattagccggccgtgta'), 'palindromes in a random string')
print()

#example - Zika virus https://www.ncbi.nlm.nih.gov/nuccore/226377833
zika_virus_dna = open('Zika_virus_sequence.txt', 'r')
zika_virus_dna = ''.join(zika_virus_dna.readlines()[1:]) #the string includes the '\n', so it's not 59 palindromes, better:
#tmp = []
#for line in f:
#if line[0] != '#':
#tmp.append(line.strip())
#clean_string = ''.join(tmp)
print(count_palindromes(zika_virus_dna), 'palindromes in Zika virus')
