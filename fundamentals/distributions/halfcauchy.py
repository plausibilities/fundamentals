import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


class HalfCauchy:

    def __init__(self):
        """

        """

    @staticmethod
    def draw(scales: np.ndarray):
        """

        :param scales: An array of scale values
        :return:
        """

        plt.figure(figsize=(2.5, 2.0))
        plt.tick_params(axis='both', labelsize='small')

        abscissae = np.linspace(0, 5, 200)

        for scale in scales:
            pdf = st.halfcauchy.pdf(abscissae, loc=0, scale=scale)
            plt.plot(abscissae, pdf, label=r'$\beta$ = {}'.format(scale))

        plt.xlabel('x', fontsize='small')
        plt.ylabel('f(x)', fontsize='small')
        plt.legend(loc='upper right', fontsize='small')
        plt.show()
