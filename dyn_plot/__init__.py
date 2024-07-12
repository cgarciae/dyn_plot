# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


__version__ = "0.1.1"
