import numpy as np

import latex
from src.plotter import SimpleFigure


def ruleta(n_min=0, n_max=36, max_size=1000, x=18, runs=10):
    spins_list = [
        np.random.randint(n_min, n_max + 1, size=max_size)
        for _ in range(runs)
    ]

    expected_freq = np.array([1/(n_max - n_min + 1)] * max_size)
    expected_mean = np.array([(n_min + n_max)/2] * max_size)
    expected_variance = np.array([((n_max - n_min + 1)**2 - 1)/12] * max_size)
    expected_deviation = np.sqrt(expected_variance)

    freqs_list = []
    for spins in spins_list:
        fr = np.zeros(max_size)
        for i in range(max_size):
            part = spins[:i+1]
            fr[i] = (part == x).sum()/len(part)
        freqs_list.append(fr)

    means_list = []
    for spins in spins_list:
        m = np.zeros(max_size)
        for i in range(max_size):
            m[i] = spins[:i+1].mean()
        means_list.append(m)

    variances_list = []
    deviations_list = []
    for spins in spins_list:
        v = np.zeros(max_size)
        for i in range(max_size):
            v[i] = spins[:i+1].var()
        d = np.sqrt(v)
        variances_list.append(v)
        deviations_list.append(d)

    n = np.arange(1, max_size + 1)

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$f_{r}$ (frecuencia relativa)')
    fig.ax.plot(n, freqs_list[0], label='$f_{{r}}$ (frecuencia relativa de ${}$)'.format(x))
    fig.ax.plot(n, expected_freq, label='$f_{{r_{{e}}}}$ (frecuencia relativa esperada de ${}$)'.format(x), linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-frecuencia.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{p}$ (valor promedio)')
    fig.ax.plot(n, means_list[0], label='$v_{p}$ (valor promedio de las tiradas)')
    fig.ax.plot(n, expected_mean, label='$v_{p_{e}}$ (valor promedio esperado)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-promedio.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor del desvío)')
    fig.ax.plot(n, deviations_list[0], label='$v_{d}$ (valor del desvío de las tiradas)')
    fig.ax.plot(n, expected_deviation, label='$v_{d_{e}}$ (valor del desvío esperado)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-desvio.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor de la varianza)')
    fig.ax.plot(n, variances_list[0], label='$v_{v}$ (valor de la varianza de las tiradas)')
    fig.ax.plot(n, expected_variance, label='$v_{v_{e}}$ (valor de la varianza esperada)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-varianza.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$f_{r}$ (frecuencia relativa)')
    for fr in freqs_list:
        fig.ax.plot(n, fr)
    fig.ax.plot(n, expected_freq, label='$f_{{r_{{e}}}}$ (frecuencia relativa esperada de ${}$)'.format(x), linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-frecuencia-multi.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{p}$ (valor promedio)')
    for m in means_list:
        fig.ax.plot(n, m)
    fig.ax.plot(n, expected_mean, label='$v_{p_{e}}$ (valor promedio esperado)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-promedio-multi.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor del desvío)')
    for d in deviations_list:
        fig.ax.plot(n, d)
    fig.ax.plot(n, expected_deviation, label='$v_{d_{e}}$ (valor del desvío esperado)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-desvio-multi.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{d}$ (valor de la varianza)')
    for v in variances_list:
        fig.ax.plot(n, v)
    fig.ax.plot(n, expected_variance, label='$v_{v_{e}}$ (valor de la varianza esperada)', linestyle='dashed')
    fig.render(latexfile=latex.PATH.joinpath('tp1-varianza-multi.tex'))


def main():
    ruleta()


if __name__ == '__main__':
    main()
