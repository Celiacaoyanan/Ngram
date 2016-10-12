#!/usr/bin/env python
# encoding: utf-8

import math

class Ngram():
    def  __init__(self, n):
        self.words = self.load_corpus()
        #self.unigram = self.make_unigram(self.words)
        self.ngram = self.make_ngram(self.words, n)
        self.n_1gram = self.make_ngram(self.words, n-1)
        return

    def load_corpus(self):#将语料转换为list
        f = open('corpus.txt', 'r')
        f1 = f.readlines()
        f.close()
        words = []
        for line in f1:
            list = line.split()
            words.extend(list)
        return words

    #def make_unigram(self, words):#一元模型，unigram字典里存储语料中每一个词的计数
        #unigram = {}
        #for i, word in enumerate(words):
        #    if not unigram.has_key(word):
        #        unigram[word] = 1
        #    else:
        #        unigram[word] += 1
      #  return unigram #返回一元字典模型

    def make_ngram(self, words, n):#n元模型，ngram_words字典里存储每n-1个词的计数
        ngram_words = {}
        for i, word in enumerate(words):
            if i == len(words)-n+1:
                break
            x = []#定义列表x临时存放这n-1个词
            for j in range(0, n):
                x.append(words[i+j])
            x1 = ' '.join(x) #将列表转换为字符串，用空格连接
            if not ngram_words.has_key(x1):
                ngram_words[x1] = 1
            else:
                ngram_words[x1] += 1
        return ngram_words #返回n元字典模型

    def probability(self, word_x, word_y):#已知前n-1个词和第n个词组成的字符串word_x，前n-1个词组成的字符串word_y，求概率
        a1 = self.ngram
        b1 = self.n_1gram
        a = a1.get(word_x, 0) #使用get函数获取字典中对应的字符串的计数
        b = b1.get(word_y, 0)
        p = float(a)/b
        return p

    def find_top10_probability(self, given_words, n): #找出和给出的前n-1个单词中，搭配概率最大的前10个
        words = self.words
        plist = {} #plist字典用来存储单词和对应的概率
        x = given_words
        x1 = ' '.join(x)
        if self.n_1gram.has_key(x1)== False:  # 如果给出的前n-1个词组成的字符串不在模型中，则输出以下提示
            print "The given words %s are not in corpus." % (x)
        else:
            for word in words:
                pp = 0
                y = x + [word]
                y1 = ' '.join(y)
                pp = self.probability(y1, x1)
                plist[word] = pp
            sorted_plist = sorted(plist.iteritems(), key=lambda d: d[1], reverse=True)  # 对plist字典进行排序得到sorted_plist元组
            flag = 0
            for i in sorted_plist:  # 输出概率最大的前10个单词
                flag = flag+1
                if flag == 11:
                    break;
                print i


if __name__ == "__main__":
    N = input("Input n: ")
    Given_words = []
    for i in range(0, N-1):
        w = raw_input("Input a word: ")
        Given_words.append(w)
    print "Given words: ", Given_words
    ng = Ngram(N)
    ng.find_top10_probability(Given_words, N)





