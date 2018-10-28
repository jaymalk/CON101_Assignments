#!/usr/bin/env python3

from random import randint as r
from math import log2 as l

def generate_dictionary(data_set, hockey, baseball):
    base_keys = list(baseball.keys())
    hock_keys = list(hockey.keys())
    for item in data_set:
        if item.startswith("rec.sport.baseball"):
            baseball.update({0:baseball[0]+1})
            new_words = item.split()
            for i in range(1, len(new_words)):
                word = new_words[i]
                if base_keys.count(word) == 0:
                    baseball.update({word: 1})
                    base_keys.append(word)
                else:
                    baseball.update({word: baseball[word]+1})
        else:
            hockey.update({0:hockey[0]+1})
            new_words = item.split()
            for i in range(1, len(new_words)):
                word = new_words[i]
                if hock_keys.count(word) == 0:
                    hockey.update({word: 1})
                    hock_keys.append(word)
                else:
                    hockey.update({word: hockey[word]+1})
    return [hockey, baseball]

def count_all(dct):
    dkeys = list(dct.keys())
    _sum = 0
    for key in dkeys:
        _sum += dct[key]
    return _sum

def naive_bayes_guess(lines, hockey, baseball):
    line_words = lines.split()
    total_count_H = count_all(hockey)
    total_count_B = count_all(baseball)
    PH = float(hockey[0])/(float(baseball[0]+hockey[0]))
    PB = 1-PH
    h = 0
    b = 0
    for i in range(1, len(line_words)):
        word = line_words[i]
        try:
            wh = hockey[word]
        except:
            wh = 0
        try:
            wb = baseball[word]
        except:
            wb = 0
        p_word = l(float(wh+wb+1)/float(total_count_B+total_count_H+2))
        p_h_word = l(float(wh+1)/float(2+total_count_H))+l(PH) - p_word
        p_b_word = l(float(wb+1)/float(2+total_count_B))+l(PB) - p_word
        h += p_h_word
        b += p_b_word
    if h>b :
        return "rec.sport.hockey"
    else:
        return "rec.sport.baseball"

def test_case(case_set, hockey, baseball):
    total = len(case_set)
    correctness = 0
    # total_count_H = count_all(hockey)
    # total_count_B = count_all(baseball)
    # PH = float(hockey[0])/(float(baseball[0]+hockey[0]))
    # PB = 1-PH
    for lines in case_set:
        # line_words = lines.split()
        # h = 0
        # b = 0
        # for i in range(1, len(line_words)):
            # word = line_words[i]
            # try:
                # wh = hockey[word]
            # except:
                # wh = 0
            # try:
                # wb = baseball[word]
            # except:
                # wb = 0
            # p_word = l(float(wh+wb+1)/float(total_count_B+total_count_H+2))
            # p_h_word = l(float(wh+1)/float(2+total_count_H))+l(PH) - p_word
            # p_b_word = l(float(wb+1)/float(2+total_count_B))+l(PB) - p_word
            # h += p_h_word
            # b += p_b_word
        # if h>b:
        #     if line_words[0] == "rec.sport.hockey":
        #         correctness+=1
        # else:
        #     if line_words[0] == "rec.sport.baseball":
        #         correctness+=1
        guess = naive_bayes_guess(lines, hockey, baseball)
        if lines.startswith(guess):
            correctness+=1
    return "Total = "+str(total)+"\nCorrect = "+str(correctness)

def random_division(st):
    st_1 = []
    while len(st)!=1:
        st_1.append(st.pop(r(0, len(st)-1)))
    return [st_1, st[0]]

def main():
    _data_set = open("./20ng-sports.txt")
    _data = list(_data_set.readlines())
    cross_set = []
    k = 2   # TOTAL DIVISIONS
    list_size = (len(_data)//k)+1
    for item in range(k):
        cross_set.append([])
        for _ in range(list_size):
            if not _data:
                break
            line = _data.pop(r(0, len(_data)-1))
            cross_set[item].append(line[:-1])

    [training_sets, test_set] = random_division(cross_set)
    [hockey, baseball] = [{0:0}, {0:0}]
    for sets in training_sets:
        [hockey, baseball] = generate_dictionary(sets, hockey, baseball)
    print(test_case(test_set, hockey, baseball))

    # [hockey, baseball] = [{0:0}, {0:0}]
    # for i in range(4):
    #     [hockey, baseball] = generate_dictionary(cross_set[i-k], hockey, baseball)
    # print(test_case(cross_set[4-k], hockey, baseball))

if __name__ == '__main__':
    main()
