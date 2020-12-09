import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


class Normal:

    def __init__(self):
        """

        """

    @staticmethod
    def draw(means: np.ndarray, deviations: np.ndarray):
        """

        :param means: An array of mean values
        :param deviations: An array of standard deviation values
        :return:
        """

        plt.figure(figsize=(2.7, 2.3))
        plt.tick_params(axis='both', labelsize='small')

        abscissae = np.linspace(-5, 5, 1000)

        for mean, deviation in zip(means, deviations):
            pdf = st.norm.pdf(abscissae, mean, deviation)
            plt.plot(abscissae, pdf, label=r'$\mu$ = {}, $\sigma$ = {}'.format(mean, deviation))

        plt.xlabel('x', fontsize='small')
        plt.ylabel('f(x)', fontsize='small')
        plt.legend(loc='upper right', fontsize='small')
        plt.show()
