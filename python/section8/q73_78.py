# -*- coding: utf-8 -*-
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate


def get_featured_datas(path='featured'):
    with open(path+'.pickle', 'rb') as f:
        datas = pickle.load(f)
    vocabulary = [v for v in open(path+'.vocab', 'r')]
    return vocabulary, datas


class Predictor:
    def __init__(self, dataset=None, vocabulary=None, dataset_path=None, test_dataset=None,
                 c=1e5, use_top_n_feature=None):
        """
        :param dataset: [(label, [word_idx, ...]), ...]
        :param vocabulary: [word1, word2, word3, ...]
        :param dataset_path: path to predesined dataset and vocabulary
        :param test_dataset: other dataset that feature extracted same metrics as dataset
        :param c: parameter of LogisticRegression model
        :param use_top_n_feature: the number of features used for prediction. If it is None, all features is used.
        """
        if dataset:
            self.dataset = dataset
            self.vocabulary = vocabulary
        elif dataset_path:
            self.vocabulary, self.dataset = get_featured_datas(dataset_path)

        self.use_top_n_feature = use_top_n_feature
        self.C = c
        self.vocabulary_size = len(self.vocabulary)

        self.label = np.array([lf[0] for lf in self.dataset])
        self.feature = np.array([self._one_hot(lf[1]) for lf in self.dataset])  # 単語インデックスからone-hot-like vecに変換
        if self.use_top_n_feature:
            self.feature = self.feature[:, :self.use_top_n_feature]

        if test_dataset:
            self.test_label = np.array([lf[0] for lf in test_dataset])
            self.test_feature = np.array([self._one_hot(lf[1]) for lf in test_dataset])
            if self.use_top_n_feature:
                self.test_feature = self.test_feature[:, :self.use_top_n_feature]
        else:
            # テストデータがなければとりあえず訓練データをコピーしてテストデータにしておく
            self.test_label = self.label
            self.test_feature = self.feature

        self.model = LogisticRegression(C=self.C)

    def _one_hot(self, numbers):
        d = np.zeros(self.vocabulary_size)
        for number in numbers:
            d[number] += 1
        return d

    def fit(self):
        self.model.fit(self.feature, self.label)

    def predict(self):
        train_predict = self.model.predict(self.feature)
        test_predict = self.model.predict(self.test_feature)
        train_accuracy = 1-sum(abs(train_predict-self.label)/2)/self.label.shape[0]
        test_accuracy = 1-sum(abs(test_predict-self.test_label)/2)/self.test_label.shape[0]
        return train_predict, train_accuracy, test_predict, test_accuracy

    def set_test_dataset(self, test_dataset):
        self.test_label = np.array([lf[0] for lf in test_dataset])
        self.test_feature = np.array([self._one_hot(lf[1]) for lf in test_dataset])
        if self.use_top_n_feature:
            self.test_feature = self.test_feature[:, self.use_top_n_feature]

    def cross_val(self, cv=5):
        # 完全にq78用の関数
        scores = cross_validate(self.model, self.feature, self.label,
                                scoring=['accuracy', 'precision', 'recall'], cv=cv)
        test_accuracy = scores['test_accuracy']
        test_precision = scores['test_precision']
        test_recall = scores['test_recall']
        test_f = (2*test_precision*test_recall)/(test_precision+test_recall)
        return test_accuracy, test_precision, test_recall, test_f

    def probability(self):
        train_proba = self.model.predict_proba(self.feature)
        test_proba = self.model.predict_proba(self.test_feature)
        return train_proba[:, 1], test_proba[:, 1]


def score(sentences):
    # 完全にq77用の関数. 使わない.
    correct = []
    predicted = []
    proba = []
    for sentence in sentences:
        c, p, pro = sentence.strip().split('\t')
        correct.append(int(c))
        predicted.append(int(p))
        proba.append(float(pro))
    correct = np.array(correct)
    predicted = np.array(predicted)
    proba = np.array(proba)
    accuracy = 1-sum(abs(correct-predicted)/2)/correct.shape[0]
    tmp = correct[predicted == 1]
    precision = sum((tmp+1)/2)/tmp.shape[0]
    tmp = predicted[correct == 1]
    recall = sum((tmp+1)/2)/tmp.shape[0]
    F = (2*precision*recall)/(precision+recall)
    return accuracy, precision, recall, F


def main():
    predictor = Predictor(dataset_path='featured')
    predictor.fit()
    correct_label = predictor.label
    predicted_label, accuracy, *_ = predictor.predict()
    print('q74', accuracy)

    w = abs(predictor.model.coef_[0])
    light = w.argsort()[9::-1]
    heavy = w.argsort()[:-11:-1]
    print('\nq75')
    print("----------heavy----------")
    for h in heavy:
        print("% 7.4f\t%s" % (w[h], predictor.vocabulary[h].strip()))

    print("-------------------------")
    print("----------light----------")
    for l in light:
        print("{0: 7.4f}\t{1}".format(w[l], predictor.vocabulary[l].strip()))

    print("-------------------------")

    print("\nq76（5つのみ表示）")
    print("正解\t予測\t確率")
    predicted_proba = predictor.model.predict_proba(predictor.feature)
    count = 0
    with open("resultq76.txt", 'w') as f:
        for c, p, proba in zip(correct_label, predicted_label, predicted_proba):
            if 1 == p:
                proba = proba[1]
            elif -1 == p:
                proba = proba[0]
            if count < 5:
                print("% 2d\t% 2d\t%.4f" % (c, p, proba))
            print("% 2d\t% 2d\t%.4f" % (c, p, proba), file=f)
            count += 1

    print("\nq78")
    accuracy, precision, recall, f = predictor.cross_val()
    print('accuracy', accuracy)
    print('precision', precision)
    print('recall', recall)
    print('F', f)

if __name__ == '__main__':
    main()
