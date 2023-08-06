import numpy as np

from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix, make_scorer

# Define Custom Cost Function
def custom_CostFunction(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    TN, FP, FN, TP = cm.ravel()
    score = 250 * FN + 5 * FP
    return score

# Assign Score Aboject for GridSearchCV
def GridSearch_CustomScorer():
    custom_score = make_scorer(custom_CostFunction, greater_is_better = False)
    return custom_score


def reportEvaluation(y_true: np.array, y_pred: np.array, dName: str = 'Train'):
    # Dictonary Object to return
    # Contain evaluation scores and Confusion Matrix Informs
    score_dict = {'DataSplit Name' : dName}
    
    # Accuracy
    print('-{0} Accuracy'.format(dName))
    acc = accuracy_score(y_true, y_pred)
    print(round(acc, 3))
    
    # F1-score
    print('-{0} F1'.format(dName))
    f1 = f1_score(y_true, y_pred)
    print(round(f1, 3))
    
    # Custom Cost
    print('-{0} Custom Cost'.format(dName))
    custom_score = custom_CostFunction(y_true, y_pred)
    print(round(custom_score, 1))
    
    # Custom Score which sacled by number of data
    # Scaling Score is used to compare Model Performance across various DataSet
    print('-{0} Custom Cost Scaled by num{0}'.format(dName))
    scaled_score = custom_score/len(y_true)
    print(round(scaled_score, 3))
    
    # Confusion Matrix and its elements
    print('-Confusion Matrix')
    cm = confusion_matrix(y_true, y_pred)
    TN, FP, FN, TP = cm.ravel()
    print('TP: {0}\tFP: {1}'.format(TP, FP))
    print('FN: {0}\tTN: {1}'.format(FN, TN))
    
    # Add informs to dictionary
    score_dict['Accuracy'] = acc
    score_dict['F1-Score'] = f1
    score_dict['CustomScore'] = custom_score
    score_dict['CustomScoreScaled'] = scaled_score
    score_dict['ConfusionMatrix'] = cm
    score_dict['TP'] = TP
    score_dict['FP'] = FP
    score_dict['FN'] = FN
    score_dict['TN'] = TN
    
    return score_dict
    