import sys

import matplotlib
import matplotlib.figure as mplfig

# mostrado/manejo de figuras y ventanas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# bindings de teclas por defecto de matplotlib
from matplotlib.backend_bases import key_press_handler
import tkinter as tk

import tikzplotlib  # generación de código PGF/TikZ para LaTeX

try:
    matplotlib.use('TkAgg')
    HEADLESS_MODE = False
except ImportError:
    HEADLESS_MODE = True


class Figure(mplfig.Figure):

    def __init__(self):
        super().__init__()

    def render(self, latexfile=None):
        for ax in self.axes:
            self._axes_legend(ax)
        if latexfile is None:
            if HEADLESS_MODE:
                print("Warning: running in headless mode, won't show anything", file=sys.stdout)
                return
            win = tk.Tk()
            win.title('Figure')

            canvas = FigureCanvasTkAgg(self, master=win)
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, win)
            toolbar.update()
            canvas.mpl_connect('key_press_event',
                               lambda ev: key_press_handler(ev, canvas, toolbar))

            canvas.draw()
            tk.mainloop()
        else:
            tikzcode = tikzplotlib.get_tikz_code(figure=self,
                                                 extra_axis_parameters=[
                                                     'scaled ticks=false',
                                                     'xticklabel style={/pgf/number format/.cd,fixed,precision=2}',
                                                     'yticklabel style={/pgf/number format/.cd,fixed,precision=2}'
                                                 ],
                                                 axis_width=r'\figW',
                                                 float_format='.5g')
            with open(latexfile, 'w') as f:
                f.write(tikzcode)

    def show(self, warn=True):
        self.render()

    @staticmethod
    def _axes_legend(ax):
        has_labels = False
        for line in ax.lines:
            label = line.get_label()
            if label and not label.startswith('_'):
                has_labels = True
                break
        if not has_labels:
            for patch in ax.patches:
                label = patch.get_label()
                if label and not label.startswith('_'):
                    has_labels = True
                    break
        if not has_labels:
            for coll in ax.collections:
                label = coll.get_label()
                if label and not label.startswith('_'):
                    has_labels = True
                    break
        if has_labels:
            ax.legend(fancybox=True, framealpha=0.5)


class SimpleFigure(Figure):

    def __init__(self, xlabel=None, ylabel=None):
        super().__init__()
        self.ax = self.add_subplot(111, xlabel=xlabel, ylabel=ylabel)
        self.ax.grid(True)
