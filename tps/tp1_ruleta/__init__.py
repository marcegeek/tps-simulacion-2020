import numpy as np

import latex
from src.plotter import SimpleFigure


def ruleta(n_min=0, n_max=36, max_size=1000, x=18):
    spins = np.random.randint(n_min, n_max + 1, size=max_size)

    expected_freq = np.array([1/(n_max - n_min + 1)] * max_size)
    expected_mean = np.array([(n_min + n_max)/2] * max_size)
    expected_variance = np.array([((n_max - n_min + 1)**2 - 1)/12] * max_size)
    expected_deviation = np.sqrt(expected_variance)

    freq_x = np.zeros(max_size)
    for i in range(max_size):
        part = spins[:i+1]
        freq_x[i] = (part == x).sum()/len(part)

    means = np.zeros(max_size)
    for i in range(max_size):
        means[i] = spins[:i+1].mean()

    variances = np.zeros(max_size)
    for i in range(max_size):
        variances[i] = spins[:i+1].var()
    deviations = np.sqrt(variances)

    n = np.arange(1, max_size + 1)

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$f_{r}$ (frecuencia relativa)')
    fig.ax.plot(n, freq_x, label='$f_{{r}}$ (frecuencia relativa de ${}$)'.format(x))
    fig.ax.plot(n, expected_freq, label='$f_{{r_{{e}}}}$ (frecuencia relativa esperada de ${}$)'.format(x))
    fig.render(latexfile=latex.PATH.joinpath('tp1-frecuencia.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{p}$ (valor promedio)')
    fig.ax.plot(n, means, label='$v_{p}$ (valor promedio de las tiradas)')
    fig.ax.plot(n, expected_mean, label='$v_{p_{e}}$ (valor promedio esperado)')
    fig.render(latexfile=latex.PATH.joinpath('tp1-promedio.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor del desvío)')
    fig.ax.plot(n, deviations, label='$v_{d}$ (valor del desvío de las tiradas)')
    fig.ax.plot(n, expected_deviation, label='$v_{d_{e}}$ (valor del desvío esperado)')
    fig.render(latexfile=latex.PATH.joinpath('tp1-desvio.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor de la varianza)')
    fig.ax.plot(n, variances, label='$v_{v}$ (valor de la varianza de las tiradas)')
    fig.ax.plot(n, expected_variance, label='$v_{v_{e}}$ (valor de la varianza esperada)')
    fig.render(latexfile=latex.PATH.joinpath('tp1-varianza.tex'))


def main():
    ruleta()


if __name__ == '__main__':
    main()
