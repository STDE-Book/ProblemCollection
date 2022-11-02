import numpy as np
import matplotlib.pyplot as plt

# Set font
plt.rc('text', usetex=True)
plt.rc('font', family='Times New Roman')
plt.rc('font', size=10)
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams["figure.figsize"] = (4, 2)
plt.rcParams['figure.dpi'] = 200

xmin = -1
xmax = 3
x = np.linspace(xmin, xmax, 1000)

p1 = (x >= 0) & (x <= 1)
p2 = 2 * np.exp(-2 * x) * (x >= 0)
p3 = 2 * np.exp(2 * (x - 1)) * (x <= 1)
p23 = np.exp(- 2 * np.abs(1 - x))

plt.figure()
plt.plot(x, p1, '-', label='$p_{X|H}(x|1)$')
plt.plot(x, p2, '--', label='$p_{X|H}(x|2)$')
plt.plot(x, p3, ':', label='$p_{X|H}(x|3)$')
plt.legend()
plt.xlabel('$x$')
plt.xlim([xmin, xmax])
plt.ylim([0, 2.1])
plt.savefig('Px15_3class_likelihoods.png')
plt.show()


plt.figure()
plt.plot(x, p23, '-', label='$p_{X|H}(x|0)$')
plt.plot(x, p1, '-.', label='$p_{X|H}(x|1)$')
plt.legend()
plt.xlabel('$x$')
plt.xlim([xmin, xmax])
plt.ylim([0, 2.1])
plt.savefig('Px15_2class_likelihoods.png')
plt.show()




