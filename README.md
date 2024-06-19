# dyn_plot

Create `matplotlib` figures that can be easily updated at runtime in Jupyter.

```python
import numpy as np
from dyn_plot import Plot

# accepts all plt.figure() arguments
plot = Plot(figsize=(10, 5))

ts = np.linspace(0, 10, 200)
losses = []
for t in ts:
  loss = -np.log(t + 0.001) + np.random.normal() * 0.4
  losses.append(loss)

  with plot: # clear and redraw
    # use any methods from Axes
    plot.set_title(f't = {t:.2f}')
    plot.plot(losses)

# close to avoid an additional rendering of the inner figure
plot.close() 
```

![dyn plot video](https://github.com/cgarciae/dyn_plot/assets/5862228/5e2ecf91-5ee8-418a-9317-01ff390a8f31)


