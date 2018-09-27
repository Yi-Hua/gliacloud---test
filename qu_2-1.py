# Quiz 2-1: word counts (10%)
'''Download this English article from https://goo.gl/BDB6bE first.
We want to know the probabilities of each bigram and trigram.
Please write a function ngram_probs to calculate these counts.  '''
# Note: please convert text to lower cases before calculating.
# Note: please keep punctuations in the text.
# Note: in all quizs, you can use any Python packages on PyPI.
def ngram_probs(filename='raw_sentences.txt'):
    file = open(filename,'r')
    content = file.read()
    content = content.lower()
    conent = content.split()
    bigram_count = 0
    bigram_list = [('i', 'am'),('you', 'are'),('he', 'is'),('she', 'is'),('we', 'are'),('it', 'is'),('they', 'are')]
    bigram_probs = {}
    trigram_count = 0
    trigram_list = [('i', 'am', 'here'),('you', 'are', 'here'),('he', 'is', 'here'),('she', 'is', 'here'),('we', 'are', 'here'),('it', 'is', 'here'),('they', 'are', 'here')]
    trigram_probs = {}
    
    for t in bigram_list:
        t = list(t) 
        for i in range(len(content)):
            if t == content[i:i+2]:
                bigram_count += 1
        bigram_probs[tuple(t)] = bigram_count/len(conent)
        bigram_count = 0

    for t in trigram_list:
        t = list(t) 
        for i in range(len(content)):
            if t == content[i:i+3]:
                trigram_count += 1
        trigram_probs[tuple(t)] = trigram_count/len(conent)
        trigram_count = 0
    return bigram_probs, trigram_probs


print(ngram_probs())
cnt2, cnt3 = ngram_probs()
# print(cnt2[('we', 'are')])
# Note: an n-gram is a contiguous sequence of n items from a given sequence of text or speech.
# For example, ('we',) is an unigram, ('we', 'are') is a bigram, and ('we', 'are', 'here') is a trigram.