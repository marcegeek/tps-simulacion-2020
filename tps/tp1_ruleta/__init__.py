import numpy as np

import latex
from src.plotter import SimpleFigure


def ruleta(n_min=0, n_max=36, max_size=1000, x=18):
    spins = np.random.randint(n_min, n_max + 1, size=max_size)

    expected_freq = np.array([1/(n_max - n_min + 1)] * max_size)
    expected_mean = np.array([(n_min + n_max)/2] * max_size)

    freq_x = []
    for i in range(max_size):
        part = spins[:i+1]
        freq_x.append((part == x).sum()/len(part))

    means = []
    for i in range(max_size):
        means.append(spins[:i+1].mean())

    n = np.arange(1, max_size + 1)

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$f_{r}$ (frecuencia relativa)')
    fig.ax.plot(n, freq_x, label='$f_{{r}}$ (frecuencia relativa de ${}$)'.format(x))
    fig.ax.plot(n, expected_freq, label='$f_{{r_{{e}}}}$ (frecuencia relativa esperada de ${}$)'.format(x))
    fig.render(latexfile=latex.PATH.joinpath('tp1-frecuencia.tex'))

    fig = SimpleFigure(xlabel='$n$ (número de tiradas)', ylabel='$v_{p}$ (valor promedio)')
    fig.ax.plot(n, means, label='$v_{p}$ (valor promedio de las tiradas)')
    fig.ax.plot(n, expected_mean, label='$v_{p_{e}}$ (valor promedio esperado)')
    fig.render(latexfile=latex.PATH.joinpath('tp1-promedio.tex'))


def main():
    ruleta()


if __name__ == '__main__':
    main()
