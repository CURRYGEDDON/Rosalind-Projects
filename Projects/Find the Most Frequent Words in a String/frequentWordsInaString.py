# ba1b functions takes in a DNA String(string) and a number(sizeOfKmer) as inputs
# prints the Kmer, of sizeOfKmer length, with the highest frequency in the DNA String
# if more than one Kmer appears with the highest frequency, all length sized, of same high frequency, Kmers are printed
def ba1b():
    # gets the DNA String and size of desired Kmer from file
    file_name = input("input name of file:")
    file = open(file_name)
    string = file.readline().strip()
    sizeOfKmer = int(file.readline())

    # Dictionary that will store every Kmer of sizeOfKmer and the number of times it occurs in the string
    Kmers = {}
    for i in range(len(string) - sizeOfKmer+1):
        currentKmer = string[i:i + sizeOfKmer]
        # if the currentKmer is not in the dictionary, places it in the dictionary and sets its count to 1
        if currentKmer not in Kmers:
            Kmers[currentKmer] = 1
        else:
            # if the currentKmer is already in the dictionary, then just adds one to its count
            Kmers[currentKmer] += 1
    # finds the highest number of times a Kmer is present in the string
    maxKey = max(Kmers.values(), key=int)
    # prints out all Kmers that appear maxKey times in the string
    for Kmer in Kmers:
        if (Kmers[Kmer]) == maxKey:
            print(Kmer, "", end="")
            
            
"""
sample input:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
sample output:
CATG GCAT
"""
