import collections

import matplotlib.pyplot as plt


class Graphs:

    def __init__(self, data: collections.namedtuple, predictions_: tuple, title_: tuple):
        """

        :param data:
        :param predictions_:
        :param title_:
        """

        self.data = data
        self.predictions_ = predictions_
        self.title_ = title_

    def draw(self, handle, predictions: collections.namedtuple, title: str):
        """

        :param handle:
        :param predictions:
        :param title:
        :return:
        """

        handle.plot(self.data.abscissae, predictions.lines, '#cccc4d', alpha=0.6, label=None)
        handle.plot(self.data.independent, self.data.dependent, 'ko', alpha=0.25, label='observations')

        handle.plot(self.data.abscissae, self.data.ordinates, 'r-', label='underlying model')

        handle.plot(self.data.abscissae, predictions.line, 'b-', label='est. (via Mean)')
        handle.plot(self.data.abscissae, predictions.posterior, 'g-', label='est. (via MAP)')

        handle.tick_params(axis='both', labelsize='small')
        handle.set_xlabel('\nx', fontsize='small')
        handle.set_ylabel('y\n', fontsize='small')
        handle.set_title('\n{}\n'.format(title), fontsize='small')

        handle.legend(loc='upper right', fontsize='small')

    def exc(self):
        """

        :return:
        """

        ncols = len(self.predictions_)

        box, handle = plt.subplots(nrows=1, ncols=ncols, figsize=(9.7, 3.3))

        for i in range(ncols):
            self.draw(handle=handle[i], predictions=self.predictions_[i], title=self.title_[i])
