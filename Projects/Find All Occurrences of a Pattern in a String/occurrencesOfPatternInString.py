#function takes in a desired pattern and dnaString as input
# outputs each starting index that the desired pattern appears in the dnaString
def ba1d():
    # retrieves the input of Pattern and DNA string from file
    file_name = input("input name of file:")
    file = open(file_name)
    # removes "/n" character from both inputs
    pattern = file.readline().strip()
    dnaString = file.readline().strip()
    lengthPattern = len(pattern)
    lengthDNAString = len(dnaString)
    # creates sliding frame looking through dnaString of size Pattern and shifts it to the right by 1 index through
    # each iteration. One is added to slidingFrameLength because 0 based indexing
    slidingFrameLength = lengthDNAString - lengthPattern + 1
    for i in range(slidingFrameLength):
        # if the current slidingFrame slice is identical to the desired pattern,
        # it prints the starting index of the slice
        slidingFrame = dnaString[i:i + lengthPattern]
        # prints all starting indexes on the same line and separates each number with a space
        if slidingFrame == pattern:
            print(i, "", end="")
"""
sample input:
ATAT
GATATATGCATATACTT
sample output:
1 3 9
"""
