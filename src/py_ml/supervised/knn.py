# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 2020/4/2 22:14

class KNN(object):
    """
    KNN : Kth nearest neighbors.

    简介： 待测样本标签由距离最近的 K 个样本的标签中的多数决定。

    约束：

    优点：

    缺点：

    """

    def __distance__(self, x, y):
        """
        计算两个样本之间的距离
        :param x:
        :param y:
        :return:
        """
        raise NotImplementedError

    def predict(self, training_samples_with_tag, sample, k=5):
        """
        使用 KNN 算法预测样本的分类
        :param list training_samples_with_tag: 训练集 list，每个元素是包含两个元素的数组，第一个元素为特征值，第二个元素为标签。
        :param list sample: 待预测样本的特征值。
        :param int k: KNN 的 k 值。
        :return: string
        """
        raise NotImplementedError


if __name__ == '__main__':
    pass
