# Ngram Word Prediction
Input number N and N-1 words, then predict top 10 words that is most likely to appear after those N-1 words according to the probabilities. 

For example, when N=3, and Given_words = ['is', 'a'], then we get the top 10 words that are most likely to appear after Given_words.

![image](https://raw.githubusercontent.com/Celiacaoyanan/Ngram/master/result_pic.png)

N-gram is simply a sequence of N words. For example: 
- Thank you (is a 2-gram)
- By the way (is a 3-gram)
- As soon as possible (is a 4-gram)

N-gram model is used to predict the occurrence of a word based on the occurrence of its N-1 previous words. So Bigram model (N = 2) predicts the occurrence of a word given only its previous word (as N-1 = 1). Trigram model (N = 3) predicts the occurrence of a word based on its previous two words (as N-1 = 2 ). To do this, we need to assign a probability to several words that might occur after in a sequence of words. 

First, we need a very large corpus of sentences, then given a sequence of words and based on this corpus, we calculate:

(the number of times the sequence occurs before a certain word) / (the total number of times the sequence occurs in the corpus)

Steps:

1. preprocess copurs to change it to words separated by space  
2. count the occurrence of every n adjacent words and every n-1 adjacent words  
3. for every word in the corpus, we combine it with the given n-1 words and get # occurrence of these n words, then get occurrence of the given n-1 words, calculate probabilities and pick the word with highest probability is the word that is most likely to occur after the given words
