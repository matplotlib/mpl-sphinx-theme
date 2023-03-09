import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4, 0.05)

fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.pcolormesh(x, x, np.random.randn(len(x)-1, len(x)-1) )
ax.set_xlabel('t [s]')
ax.set_ylabel('S [V]')
ax.set_title('Sine wave')