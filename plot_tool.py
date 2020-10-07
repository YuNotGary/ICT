import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as _CanvasWidget
from matplotlib.figure import Figure
from matplotlib.backend_bases import PickEvent


class CanvasWidget(_CanvasWidget):
    sig_picked = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        figure = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        super().__init__(figure)
        self.ax = figure.add_subplot(111)

    def plot_data(self, data: list, typo: str, title: str = 'Normalised Spectra Plot'):
        """
        Plot Data
        :param data: the data to plot, a list of many rows, each row has exact same columns.
        :param typo: ether "line" or "scatter". This param tells you what kind of plot user is expecting.
        :param title: title of the plot
        :return:
        """

        # todo： Please paste your plot code here
        # ==============================================


        row0 = data[0]  # first row, you can know how many columns.
        cols = len(row0)  # how many columns the "data" has.
        self.ax.cla()  # clear the plot and get prepared
        # your plot begins
        if cols == 2:
            wave = [i[0] for i in data]
            sp = [i[1] for i in data]

            self.ax.plot(wave, sp, label='Spectra')

        elif cols == 3:
            wave = [i[0] for i in data]
            sp1 = [i[1] for i in data]
            sp2 = [i[2] for i in data]

            self.ax.plot(wave, sp1, label='Spectra 1')
            self.ax.plot(wave, sp2, label='Spectra 2')

        elif cols == 4:
            wave = [i[0] for i in data]
            sp1 = [i[1] for i in data]
            sp2 = [i[2] for i in data]
            sp3 = [i[3] for i in data]

            self.ax.plot(wave, sp1, label='Spectra 1')
            self.ax.plot(wave, sp2, label='Spectra 2')
            self.ax.plot(wave, sp3, label='Spectra 3')

        else:
            raise ValueError
        self.ax.set_title(title)
        self.ax.set_xlabel('Wavelength')
        self.ax.set_xlabel('Spectra')
        self.ax.legend()

        # end of your code
        # ==============================================
        self.draw()

    def plot_clear(self):
        """clear a plot-"""
        self.ax.cla()
        self.draw()