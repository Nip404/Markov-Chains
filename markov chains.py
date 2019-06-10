import os
import random
import numpy as np

def flatten(arr):
    new = []
    for i in arr:
        for j in i:
            new.append(j)
    return new

def main(file,words):
    all_words = []
    
    with open(file,"r") as f:
        for line in f:
            new = []

            for item in [i for i in line.replace("\n","").split(" ") if not i == ""][:-1]:
                    if item[-1] in ", . ; : ! ? / -".split(" "):
                        new += [item[:-1],item[-1]]
                    else:
                        new.append(item)

            all_words += new
        f.close()

    freq = {all_words[0]:{}}
    for i,word in enumerate(all_words[1:]):
        if not word in freq.keys():
            freq[word] = {}

        if not word in freq[all_words[i]].keys(): 
            freq[all_words[i]][word] = 1
        else:
            freq[all_words[i]][word] += 1

    freq_prob = {}
    for k,v in freq.items():
        freq_prob[k] = flatten([[k2 for _ in range(v2)] for k2,v2 in v.items()])

    current = random.choice(list(freq_prob.keys()))
    for i in range(words):
        print(current,end=" ")
        current = random.choice(freq_prob[current])
        
if __name__ == "__main__":
    file = "bible.txt"
    words = 50
    main(file,words)
