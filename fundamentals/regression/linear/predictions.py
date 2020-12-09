import numpy as np
import collections


class Predictions:
    """

    """

    def __init__(self, trace, maximal, abscissae, size: int):
        """

        :param trace: Trace
        :param maximal: The maximum a posteriori
        :param size: The number estimated regression lines to randomly select
        """

        self.trace = trace
        self.maximal = maximal
        self.abscissae = abscissae
        self.size = size

        self.ModelPredictions = collections.namedtuple(
            typename='ModelPredictions', field_names=['line', 'lines', 'posterior'])

    def line(self):
        """

        :return:
        """

        return self.trace['intercept'].mean(axis=0) + (self.trace['gradient'].mean(axis=0) * self.abscissae)

    def lines(self):
        """

        :return:
        """

        samplings = self.trace.report.n_draws * self.trace.nchains
        indices = np.random.randint(low=0, high=samplings, size=self.size)

        if self.trace['intercept'].ndim == 1:
            values = self.trace['intercept'][indices, None] + \
                     (self.trace['gradient'][indices, None] * self.abscissae.T)
        else:
            values = self.trace['intercept'][indices] + \
                     (self.trace['gradient'][indices] * self.abscissae.T)

        return values.T

    def posterior(self):
        return self.maximal['intercept'] + (self.maximal['gradient'] * self.abscissae)

    def exc(self):
        """

        :return:
        """

        # noinspection PyUnresolvedReferences,PyProtectedMember
        return self.ModelPredictions._make(
            [self.line(), self.lines(), self.posterior()])
