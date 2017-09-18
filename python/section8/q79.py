# -*- coding: utf-8 -*-
# 参考：http://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
from q73 import Predictor
from matplotlib import pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score


def figure(precision, recall, avg, fig_name='resultq79'):
    # precision,recallからグラフを描画し保存する
    plt.clf()
    plt.step(recall, precision, color='b', alpha=0.2,
             where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2,
                     color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('2-class Precision-Recall curve: AUC={0:0.2f}'.format(avg))
    plt.savefig(fig_name)


def main(use_top_n_feature=1000):
    # データセットからprecision,recallを取得しfigure関数に投げる
    predictor = Predictor(dataset_path='featured', use_top_n_feature=use_top_n_feature)
    predictor.fit()
    correct_label = predictor.label
    probability, _ = predictor.probability()
    precision, recall, _ = precision_recall_curve(correct_label, probability)
    figure(precision, recall, average_precision_score(correct_label, probability), 'q79_%d' % use_top_n_feature)

if __name__ == '__main__':
    main(use_top_n_feature=1000)
    main(use_top_n_feature=2000)
    main(use_top_n_feature=3000)
