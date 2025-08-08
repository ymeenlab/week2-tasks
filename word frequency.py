# Python3 code to find frequency of each word
# function for calculating the frequency
def freq(str):

    # break the string into list of words
    str1 = str.split()

    # gives set of unique words
    unique_words = set(str1)
    
    for words in unique_words :
        print('Frequency of ', words , 'is :', str1.count(words))

# driver code
str = input('enter the sentence or words:')
    
    # calling the freq function
freq(str)