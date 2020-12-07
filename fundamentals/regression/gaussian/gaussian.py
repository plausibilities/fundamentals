import pymc3 as pm
import arviz as az


class Gaussian:

    def __init__(self, independent, dependent):
        """

        :param independent:
        :param dependent:
        """

        self.independent = independent
        self.dependent = dependent

    def inference(self):

        with pm.Model() as model:

            # Hypothesis priors
            gradient: pm.model.TransformedRV = pm.Normal(name='gradient', mu=1.7, sigma=20.0)
            intercept: pm.model.TransformedRV = pm.Normal(name='intercept', mu=1.3, sigma=20.0)

            # Hypothesis
            regression = pm.Deterministic('regression', intercept + gradient * self.independent)

            # Likelihood hyperprior, i.e., Gaussian distribution's hyperprior
            sigma_: pm.model.TransformedRV = pm.HalfCauchy(name='sigma', beta=5.0)

            # Likelihood
            # noinspection PyTypeChecker
            likelihood = pm.Normal(name='y', mu=regression, sigma=sigma_, observed=self.dependent)

            # Inference
            # Drawing posterior samples via the default NUTS sampling
            trace = pm.sample(draws=4000, cores=4, tune=10000)
            maximal = pm.find_MAP()

            # The trace generated from Markov Chain Monte Carlo sampling
            arviztrace = az.from_pymc3(trace=trace)

        return model, trace, maximal, arviztrace, likelihood
