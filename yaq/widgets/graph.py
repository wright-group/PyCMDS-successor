"""Graph."""


# --- import --------------------------------------------------------------------------------------


import os

from qtpy import QtCore

import pyqtgraph as pg

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class Graph(pg.GraphicsView):
    
    def __init__(self, title=None, xAutoRange=True, yAutoRange=True):
        super().__init__(background='#1d1f21') 
        #create layout
        self.graphics_layout = pg.GraphicsLayout(border=None)
        self.setCentralItem(self.graphics_layout)
        self.graphics_layout.layout.setSpacing(0)
        self.graphics_layout.setContentsMargins(0., 0., 1., 1.) 
        #create plot object
        self.plot_object = self.graphics_layout.addPlot(0, 0)
        self.labelStyle = {'color': '#FFF', 'font-size': '14px'}
        self.x_axis = self.plot_object.getAxis('bottom')
        self.x_axis.setLabel(**self.labelStyle)
        self.y_axis = self.plot_object.getAxis('left')
        self.y_axis.setLabel(**self.labelStyle)
        self.plot_object.showGrid(x = True, y = True, alpha = 0.5)
        self.plot_object.setMouseEnabled(False, True)
        self.plot_object.enableAutoRange(x=xAutoRange, y=yAutoRange)
        #title
        if title: 
            self.plot_object.setTitle(title)
            
    def add_scatter(self, color='c', size=3, symbol='o'):
        curve = pg.ScatterPlotItem(symbol=symbol, pen=(color), brush=(color), size=size)
        self.plot_object.addItem(curve)
        return curve 
        
    def add_line(self, color='c', size=3, symbol='o'):
        curve = pg.PlotCurveItem(symbol=symbol, pen=(color), brush=(color), size=size)
        self.plot_object.addItem(curve)
        return curve 
        
    def add_infinite_line(self, color='y', style='solid', angle=90., movable=False, hide=True):
        '''
        Add an InfiniteLine object.
        
        Parameters
        ----------
        color : (optional)
            The color of the line. Accepts any argument valid for `pyqtgraph.mkColor <http://www.pyqtgraph.org/documentation/functions.html#pyqtgraph.mkColor>`_. Default is 'y', yellow.
        style : {'solid', 'dashed', dotted'} (optional)
            Linestyle. Default is solid.
        angle : float (optional)
            The angle of the line. 90 is vertical and 0 is horizontal. 90 is default.
        movable : bool (optional)
            Toggles if user can move the line. Default is False.
        hide : bool (optional)
            Toggles if the line is hidden upon initialization. Default is True.
        
        Returns
        -------
        InfiniteLine object
            Useful methods: setValue, show, hide
        '''
        if style == 'solid':
            linestyle = QtCore.Qt.SolidLine
        elif style == 'dashed':
            linestyle = QtCore.Qt.DashLine
        elif style == 'dotted':
            linestyle = QtCore.Qt.DotLine
        else:
            print('style not recognized in add_infinite_line')
            linestyle = QtCore.Qt.SolidLine
        pen = pg.mkPen(color, style=linestyle)
        line = pg.InfiniteLine(pen=pen)
        line.setAngle(angle)
        line.setMovable(movable)
        if hide:
            line.hide()
        self.plot_object.addItem(line)
        return line  
            
    def clear(self):
        self.plot_object.clear()

    def set_labels(self, xlabel=None, ylabel=None):
        if xlabel:
            self.plot_object.setLabel('bottom', text=xlabel)
            self.plot_object.showLabel('bottom')
        if ylabel:
            self.plot_object.setLabel('left', text=ylabel)
            self.plot_object.showLabel('left')
            
    def set_xlim(self, xmin, xmax):
        self.plot_object.setXRange(xmin, xmax)
        
    def set_ylim(self, ymin, ymax):
        self.plot_object.setYRange(ymin, ymax)
