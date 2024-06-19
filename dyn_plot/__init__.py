from IPython import display
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import typing as tp

if tp.TYPE_CHECKING:
  PlotBase = Axes
else:
  PlotBase = object


class Plot(PlotBase):
  def __init__(self, *args, **kwargs):
    self.fig = plt.figure(*args, **kwargs)
    self.ax = self.fig.gca()
    self.disp = display.display(self.fig, display_id=str(id(self)))

  if not tp.TYPE_CHECKING:

    def __getattr__(self, name):
      return getattr(self.ax, name)

  def __enter__(self):
    self.ax.clear()

  def __exit__(self, *args):
    self.fig.canvas.draw()
    self.disp.update(self.fig)

  def close(self):
    plt.close(self.fig)


__version__ = "0.1.0"
