import pymc3 as pm
import collections
import arviz as az


class Stochastic:

    def __init__(self, independent, dependent):
        """

        :param independent:
        :param dependent:
        """

        self.independent = independent
        self.dependent = dependent

        self.ModelFeatures = collections.namedtuple(
            typename='ModelFeatures',
            field_names=['model', 'trace', 'maximal', 'arviztrace', 'likelihood'])

    def inference(self):

        with pm.Model() as model:

            # Hypothesis priors
            gradientdrift = pm.Normal(name='gradientDrift', mu=1.7, sigma=20.0)
            gradientdeviation = pm.HalfCauchy(name='gradientDeviation', beta=1.0)
            gradient = pm.GaussianRandomWalk(name='gradient', mu=gradientdrift, sigma=gradientdeviation)

            interceptdrift = pm.Normal(name='interceptDrift', mu=1.3, sigma=20.0)
            interceptdeviation = pm.HalfCauchy(name='interceptDeviation', beta=1.0)
            intercept = pm.GaussianRandomWalk(name='intercept', mu=interceptdrift, sigma=interceptdeviation)

            # Hypothesis
            # noinspection PyUnresolvedReferences
            regression = pm.Deterministic('regression', intercept + (gradient * self.independent))

            # Likelihood hyperpriors, i.e., student's t-distribution hyperpriors
            sigma_ = pm.HalfCauchy(name='sigma_', beta=10.0)
            nu_ = pm.Gamma(name='nu_', alpha=2.0, beta=0.1)

            # Likelihood
            # noinspection PyTypeChecker
            likelihood = pm.StudentT(name='y', nu=nu_, mu=regression, sigma=sigma_, observed=self.dependent)

            # Inference
            # Drawing posterior samples via the default NUTS sampling
            trace = pm.sample(draws=4000, cores=2, tune=4000)
            maximal = pm.find_MAP()

            # The trace generated from Markov Chain Monte Carlo sampling
            arviztrace = az.from_pymc3(trace=trace)

        # noinspection PyUnresolvedReferences,PyProtectedMember
        return self.ModelFeatures._make([model, trace, maximal, arviztrace, likelihood])
