import numpy as np
import nltk
def wordcount_fn(file_uri):
    nparr_words = open(file_uri, 'r')
    text_as_str = nparr_words.read() #for small textfiles
    text_as_list = text_as_str.split()

    
    counts = nltk.FreqDist(text_as_list).items()
    for key, val in counts:
        print(str(val) + " " + str(key))
    return


print(f"TF (Frequency Distribution) for each word in your file: {wordcount_fn('./textfile.txt')}")
    
        