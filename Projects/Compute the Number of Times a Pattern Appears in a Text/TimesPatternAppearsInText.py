# Takes in a DNA string and a desired DNA substring as input
# outputs number of times DNA substring is found in DNA string
def patternCount(Text, Pattern):
    # accumulator that will store number of times substring is found in string
    count = 0
    lengthText = len(Text)
    lengthPattern = len(Pattern)
    # sliding frame shifts by one index to the right after each iteration, one is added because 0 based indexing
    slidingFrameSteps = lengthText - lengthPattern
    for i in range(slidingFrameSteps + 1):
        # Checks to see if the current sliding frame matches the desired pattern, if True then count increases by 1
        if Text[i:i + lengthPattern] == Pattern:
            count += 1
    return count


def inputToPatternCount():
    # retrieves the inputed DNA String and DNA substring from file and passes it on to patterCount function
    file_name = input("input name of file:")
    file = open(file_name)
    # removes "/n" character from both inputs
    text = file.readline().strip()
    pattern = file.readline().strip()
    count = patternCount(text, pattern)
    print(count)
