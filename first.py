import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.plot(x, y1, 'r--', label='y = 2x + 1')  # red dashed line
plt.plot(x, y2, 'g-.', label='y = 2x + 2')  # green dash-dot line
plt.plot(x, y3, 'b:', label='y = 2x + 3')   # blue dotted line

plt.title('Lines with Different Slopes and Intercepts')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()