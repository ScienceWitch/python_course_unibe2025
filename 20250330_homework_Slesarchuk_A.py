#take a string and count 8 char palindromes
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

#example - Zika virus https://www.ncbi.nlm.nih.gov/nuccore/226377833
zika_virus_dna = open('Zika_virus_sequence.txt', 'r')

tmp = []
for line in zika_virus_dna:
    if line[0] != '#' and line[0] != '>':
        tmp.append(line.strip())
    zika_virus_dna_string = ''.join(tmp)

palindromes_in_Zika = count_palindromes(zika_virus_dna_string)
print(palindromes_in_Zika, 'palindromes of length=8 in Zika virus')

<<<<<<< HEAD
#make a list for number of palindromes in a random genome
zika_virus_random_palindromes = [palindromes_in_Zika]
=======
#make a list for a number of palindromes in a random genome
zika_virus_random_palindromes = [count_palindromes(zika_virus_dna_string)]
>>>>>>> 90fd6525acf5ed59cbc41fc6d89e253144eac903

#make a list from the DNA string for a random shuffle
import numpy as np

zika_virus_dna_list = np.array([char for char in zika_virus_dna_string])

#go wild
for _ in range(100):
    np.random.seed(0)
    np.random.shuffle(zika_virus_dna_list)
    num_palindromes = count_palindromes(''.join(zika_virus_dna_list))
    zika_virus_random_palindromes.append(num_palindromes)
print(zika_virus_random_palindromes)

#plot the distribution of number of palindroms with length = 8 in 100 randomized Zika virus genomes
import matplotlib.pyplot as plt

#plot the histogram
fig, ax = plt.subplots()
n, bins, patches = ax.hist(zika_virus_random_palindromes)

#add title and axes labels
plt.title('Number of palindromes of length 8 in randomized Zika virus DNA')
plt.xlabel('Number of palindromes of length 8')
plt.ylabel('Counts')

#add info
ax.text(18, 22, s=f'Palindromes in Zika virus: 41\nAverage number of palindromes: {int(np.mean(bins))}', fontsize='small')

#color the bar with Zika virus
for k in range(len(n)):
    if palindromes_in_Zika > bins[k] and palindromes_in_Zika < bins[k+1]:
        patches[k].set_facecolor('grey')
        ax.axvline(x=palindromes_in_Zika, color="grey", linestyle='--')

plt.savefig('zika_histogram.pdf', bbox_inches='tight')
plt.show()
plt.close()


