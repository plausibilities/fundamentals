import numpy as np


class Predictions:

    def __init__(self, trace, maximal, futures, size: int):
        """

        :param trace:
        :param maximal:
        :param size:
        """

        self.trace = trace
        self.maximal = maximal
        self.futures = futures
        self.size = size

    def line(self):
        """

        :return:
        """

        return self.trace['intercept'].mean(axis=0) + (self.trace['gradient'].mean(axis=0) * self.futures)

    def lines(self):
        """

        :return:
        """

        samplings = self.trace.report.n_draws * self.trace.nchains
        indices = np.random.randint(low=0, high=samplings, size=self.size)

        return self.trace['intercept'][indices] + (self.trace['gradient']['indices'] * self.futures[:, np.newaxis])

    def posterior(self):
        return self.maximal['intercept'] + (self.maximal['gradient'] * self.futures)

    def exc(self):
        """

        :return:
        """

        return self.line(), self.lines(), self.posterior()
