##Python Imports
import tkinter as tk
from tkinter import ttk
import numpy as np

#System Imports
import logging

logger = logging.getLogger(__name__)

try:
    from ..waveframe.PlotDisplay import PlotDisplay
    from ..waveframe.Waveform import Waveform
    from ..waveframe.Notebook import Notebook
except:
    pass

try:
    from waveframe.PlotDisplay import PlotDisplay
    from waveframe.Waveform import Waveform
    from waveframe.Notebook import Notebook
except:
    pass

class BiquadNotebook(Notebook):
    def __init__(self, frame: ttk.Frame, figsize: tuple, index: int = None):
        super().__init__(frame, figsize)