# Quiz 2-3: predicting the next word

# Write a function predict_max to complete the sentence by finding the max likelihood word.
# For example, if the starting bigram is ('we', 'are') , the max likelihood word is 'going' .
# Given the next word 'going' , current bigram becomes ('are', 'going') , and then we can predict
# the next word. The predicting process will end when the next word is '.' or length of the sentence is
# larger than 15.
def predict_max(starting, cnt2=cnt2, cnt3=cnt3):
return list_of_words
sent = predict_max(('we', 'are'))
assert sent[-1] == '.' or len(sent) <= 15
print(' '.join(sent))