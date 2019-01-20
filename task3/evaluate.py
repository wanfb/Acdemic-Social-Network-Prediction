# -*- coding: utf-8 -*-
import pdb

predict_file = open('./data/raw/output.txt', 'r')
true_file = open('./data/raw/testing_set_label.txt', 'r')

predict = predict_file.readlines()     
true = true_file.readlines()

TP = 0
TN = 0
FP = 0
FN = 0

for i in range(len(predict) - 1):
    predict[i + 1] = predict[i + 1].strip('\n').split(',')
    true[i] = true[i].strip('\n').split(' ')
    if predict[i + 1][1] == str(1) and predict[i + 1][1] == true[i][2]:
        TP = TP + 1
    if predict[i + 1][1] == str(0) and predict[i + 1][1] == true[i][2]:
        TN = TN + 1
    if predict[i + 1][1] == str(1) and predict[i + 1][1] != true[i][2]:
        FP = FP + 1
    if predict[i + 1][1] == str(0) and predict[i + 1][1] != true[i][2]:
        FN = FN + 1
pdb.set_trace()
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * precision * recall /(precision + recall)

#pdb.set_trace()
print('准确率：' + str(accuracy))
print('精确率：' + str(precision))
print('召回率：' + str(recall))
print('F1：' + str(F1))
print('TP：' + str(TP))
print('TN：' + str(TN))
print('FP：' + str(FP))
print('FN：' + str(FN))
 
    
