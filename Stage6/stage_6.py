from __future__ import division
import nltk
import codecs
from nltk import re
    #Функція для формування списку слів з пункту 1 (позитивних,негативних, нейтральних)
def words_1(polarity):
    global dict_list
    if polarity == 'pos':
        wordlist = [key for key, val in dict_list.items() if int(val) > 1]
    elif polarity == 'neg':
        wordlist = [key for key, val in dict_list.items() if int(val) < 1]
    else:
        wordlist = [key for key, val in dict_list.items() if int(val) == 0]
    return wordlist
    #Функція для формування списків слів (позитивних,негативних, нейтральних)
    #на основі певного словника
def words_2(polarity, dic):
    if polarity == 'pos':
        wordlist = [key for key, val in dic.items() if val == '+']
    elif polarity == 'neg':
        wordlist = [key for key, val in dic.items() if val == '-']
    else:
        wordlist = [key for key, val in dic.items() if val == 'U']
    return wordlist

    #Читання файлу Rybchak_pnn.txt з пункту 1
List = codecs.open('D:\Rybchak_pnn.txt', encoding = 'utf-8').readlines()
    #Формування словника з файлу Rybchak_pnn.txt
dict_list = {}
for line in List:
    re.sub('\s', ' ', line)
    dict_list[line.split()[0]] = line.split()[1]

    #Читання файлу Rybchak_dic1.txt з пункту 6
Dic1 = codecs.open('D:\Rybchak_dic1.txt', encoding = 'utf-8').readlines()
    #Формування словника з файлу Rybchak_dic1.txt
dict_dic1 = {}
for line in Dic1:
    dict_dic1[line.split(',')[0]] = line.split(',')[1]

    #Читання файлу Rybchak_dic2.txt з пункту 6
Dic2 = codecs.open('D:\Rybchak_dic2.txt', encoding = 'utf-8').readlines()
    #Формування словника з файлу Rybchak_dic2.txt
dict_dic2 = {}
for line in Dic2:
    dict_dic2[line.split(',')[0]] = line.split(',')[1]

    #Визначення змінних, необхідних для обчислення
TP_FN_pos = words_1('pos')
TP_FN_neg = words_1('neg')
TP_FN_neu = words_1('neu')
TP_pos_1 = [w for w in TP_FN_pos if w in words_2('pos', dict_dic1)]
TP_neg_1 = [w for w in TP_FN_neg if w in words_2('neg', dict_dic1)]
TP_neu_1 = [w for w in TP_FN_neu if w in words_2('neu', dict_dic1)]
FP_pos_1 = [w for w in words_2('pos', dict_dic1) if w in TP_FN_neg or w in TP_FN_neu]
FP_neg_1 = [w for w in words_2('neg', dict_dic1) if w in TP_FN_pos or w in TP_FN_neu]
FP_neu_1 = [w for w in words_2('neu', dict_dic1) if w in TP_FN_pos or w in TP_FN_neg]
TP_pos_2 = [w for w in TP_FN_pos if w in words_2('pos', dict_dic2)]
TP_neg_2 = [w for w in TP_FN_neg if w in words_2('neg', dict_dic2)]
TP_neu_2 = [w for w in TP_FN_neu if w in words_2('neu', dict_dic2)]
FP_pos_2 = [w for w in words_2('pos', dict_dic2) if w in TP_FN_neg or w in TP_FN_neu]
FP_neg_2 = [w for w in words_2('neg', dict_dic2) if w in TP_FN_pos or w in TP_FN_neu]
FP_neu_2 = [w for w in words_2('neu', dict_dic2) if w in TP_FN_pos or w in TP_FN_neg]
    #Обчислення для першого словника
print '     Результати обчислень для пергошо словника:'
Precision_1_pos = len(TP_pos_1)/len(TP_pos_1 + FP_pos_1)
Recall_1_pos = len(TP_pos_1)/len(TP_FN_pos)
print 'Точність для позитивних слів =', Precision_1_pos
print 'Повнота для позитивних слів =', Recall_1_pos
Precision_1_neg = len(TP_neg_1)/len(TP_neg_1 + FP_neg_1)
Recall_1_neg = len(TP_neg_1)/len(TP_FN_neg)
print 'Точність для негативних слів =', Precision_1_neg
print 'Повнота для негативних слів =', Recall_1_neg
Precision_1_neu = len(TP_neu_1)/len(TP_neu_1 + FP_neu_1)
Recall_1_neu = len(TP_neu_1)/len(TP_FN_neu)
print 'Точність для нейтральних слів =', Precision_1_neu
print 'Повнота для нейтральних слів =', Recall_1_neu
 #Обчислення для другого словника
print '     Результати обчислень для другого словника:'
Precision_2_pos = len(TP_pos_2)/len(TP_pos_2 + FP_pos_2)
Recall_2_pos = len(TP_pos_2)/len(TP_FN_pos)
print 'Точність для позитивних слів =', Precision_2_pos
print 'Повнота для позитивних слів =', Recall_2_pos
Precision_2_neg = len(TP_neg_2)/len(TP_neg_2 + FP_neg_2)
Recall_2_neg = len(TP_neg_2)/len(TP_FN_neg)
print 'Точність для негативних слів =', Precision_2_neg
print 'Повнота для негативних слів =', Recall_2_neg
Precision_2_neu = len(TP_neu_2)/len(TP_neu_2 + FP_neu_2)
Recall_2_neu = len(TP_neu_2)/len(TP_FN_neu)
print 'Точність для нейтральних слів =', Precision_2_neu
print 'Повнота для нейтральних слів =', Recall_2_neu
    #Запис результатів у файл
output_file = open('D:\Rybchak_results.txt', 'w')
output_file.write('     Результати обчислень для пергошо словника:'+'\n' \
                  + 'Точність для позитивних слів =' \
                  + str(Precision_1_pos).encode('utf-8')+'\n'\
                  + 'Повнота для позитивних слів ='\
                  + str(Recall_1_pos).encode('utf-8')+'\n'\
                  + 'Точність для негативних слів =' \
                  + str(Precision_1_neg).encode('utf-8')+'\n'\
                  + 'Повнота для негативних слів ='\
                  + str(Recall_1_neg).encode('utf-8')+'\n'\
                  + 'Точність для нейтральних слів =' \
                  + str(Precision_1_neu).encode('utf-8')+'\n'\
                  + 'Повнота для нейтральних слів ='\
                  + str(Recall_1_neu).encode('utf-8')+'\n'\
                  + '     Результати обчислень для другого словника:' +'\n'\
                  + 'Точність для позитивних слів =' \
                  + str(Precision_2_pos).encode('utf-8')+'\n'\
                  + 'Повнота для позитивних слів ='\
                  + str(Recall_2_pos).encode('utf-8')+'\n'\
                  + 'Точність для негативних слів =' \
                  + str(Precision_2_neg).encode('utf-8')+'\n'\
                  + 'Повнота для негативних слів ='\
                  + str(Recall_2_neg).encode('utf-8')+'\n'\
                  + 'Точність для нейтральних слів =' \
                  + str(Precision_2_neu).encode('utf-8')+'\n'\
                  + 'Повнота для нейтральних слів ='\
                  + str(Recall_2_neu).encode('utf-8')+'\n')
output_file.close()

