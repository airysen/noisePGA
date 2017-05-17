Noise PGA
=====

# A simple genetic algorithm for feature selection based on DEAP library

*"Zhu, M., & Chipman, H. (2006). Darwinian Evolution in Parallel Universes: A Parallel Genetic Algorithm for Variable Selection. Technometrics, 48(4), 491-502"*
[http://www.jstor.org/stable/25471241](http://www.jstor.org/stable/25471241)

*"Chun-Xia Zhang et al.(2016) Randomizing outputs to increase variable selection accuracy. Neurocomputing, Volume 218, 19 December 2016, Pages 91-102, ISSN 0925-2312"*
[http://www.sciencedirect.com/science/article/pii/S0925231216309638](http://www.sciencedirect.com/science/article/pii/S0925231216309638)

Installation
------------

Install the following requirements:

 * [deap](https://github.com/DEAP/deap)
 * [scikit-learn](scikit-learn.org)

Example of usage
-----

```python
>>> from noisePGA import NoiseGAEnsemble
>>> from sklearn.datasets import make_regression
>>> from sklearn.linear_model import LinearRegression
>>> X, y, coef = make_regression(n_samples=150, n_features=100, n_informative=15, n_targets=1,
                             noise=0.0, coef=True)
>>> lr = LinearRegression()
>>> nga = NoiseGAEnsemble(lr, ngen=15, ens_size=50, cv=5, s=1.2)
>>> nga.fit(X, y)
>>> print('TRUE: ', np.where(coef > 0)[0])
>>> print('PRED: ', np.where(nga.get_rmean() > 0.5)[0])
```
