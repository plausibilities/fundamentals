import collections

import numpy as np


class Linear:

    def __init__(self, parameters):
        """

        :param parameters:
        """

        self.parameters: collections.namedtuple = parameters
        self.points = self.parameters.N + self.parameters.F

        self.Data = collections.namedtuple(
            typename='Data',
            field_names=['intercept', 'gradient', 'noiseloc', 'noisescale',
                         'abscissae', 'ordinates', 'independent', 'dependent'])

    @staticmethod
    def outliers(dependent: np.ndarray, deterministic: bool = True) -> np.ndarray:
        """

        :param dependent:
        :param deterministic:
        :return:
        """

        indices = [5, 7, 9]

        if deterministic:
            dependent[indices] = [8.5, 6.3, 9.2]
        else:
            dependent[indices] = np.random.uniform(low=5.5, high=6.5) * dependent[indices]

        return dependent

    def noise(self) -> np.ndarray:
        """

        :return:
        """

        return np.random.normal(loc=self.parameters.noiseloc, scale=self.parameters.noisescale,
                                size=self.points)

    def model(self) -> (np.ndarray, np.ndarray):
        """

        :return:
        """

        abscissae = np.linspace(start=min(self.parameters.range), stop=max(self.parameters.range),
                                num=self.points)

        ordinates = (self.parameters.gradient * abscissae) + self.parameters.intercept

        return abscissae, ordinates

    def exc(self, anomalies: bool = True):
        """

        :param anomalies:
        :return:
        """

        abscissae, ordinates = self.model()
        noise = self.noise()

        independent = abscissae[:self.parameters.N]
        dependent = ordinates[:self.parameters.N] + noise[:self.parameters.N]

        if anomalies:
            dependent = self.outliers(dependent=dependent)

        # noinspection PyUnresolvedReferences,PyProtectedMember
        return self.Data._make([self.parameters.intercept, self.parameters.gradient,
                                self.parameters.noiseloc, self.parameters.noisescale,
                                abscissae, ordinates, independent, dependent])
