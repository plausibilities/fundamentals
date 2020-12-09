import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


class Student:

    def __init__(self):
        """

        """

    @staticmethod
    def draw(locations: np.ndarray, scales: np.ndarray, degrees: np.ndarray):
        """

        :param locations: An array of location values
        :param scales: An array of scale values
        :param degrees: An array of degrees of freedom values
        :return:
        """

        plt.figure(figsize=(2.3, 2.1))
        plt.tick_params(axis='both', labelsize='small')

        abscissae = np.linspace(-5, 5, 100)

        for location, scale, degree in zip(locations, scales, degrees):
            pdf = st.t.pdf(abscissae, degree, loc=location, scale=scale)
            plt.plot(abscissae, pdf, label=r'$\mu$ = {}, $\sigma$ = {}, $\nu$ = {}'.format(location, scale, degree))

        plt.xlabel('x', fontsize='small')
        plt.ylabel('f(x)', fontsize='small')
        plt.legend(loc='best', fontsize='x-small')
        plt.show()
