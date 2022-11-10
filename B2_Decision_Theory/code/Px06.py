import numpy as np
import matplotlib.pyplot as plt


def compute_roc(alpha):
    alpha = np.array(alpha)
    Pfa = (1 - alpha)**2 * (alpha < 1)
    Pd = 1 - (alpha - 0.5)**2 * (alpha > 0.5)
    return Pfa, Pd


# Set font
plt.rc('text', usetex=True)
plt.rc('font', family='Times New Roman')
plt.rc('font', size=10)

# To paint axes only, not bounding box
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

plt.rcParams["figure.figsize"] = (2.8, 2.8)
plt.rcParams['figure.dpi'] = 200

xmin = 0
xmax = 3 / 2
alpha = np.linspace(xmin, xmax, 1000)

Pfa, Pd = compute_roc(alpha)

alpha_sample = [0, 0.5, 0.75, 1, 1.5]
Pfa_sample, Pd_sample = compute_roc(alpha_sample)

Pfa_bayes, Pd_bayes = compute_roc(5 / 6)
Pfa_NP, Pd_NP = compute_roc(0.8)

plt.figure(layout='constrained')
plt.plot(Pfa, Pd)
plt.plot(Pfa_sample, Pd_sample, 'r.')
plt.plot(Pfa_bayes, Pd_bayes, 'k.', label='Bayes')
plt.plot(Pfa_NP, Pd_NP, 'g.', label='NP')

plt.xlabel('$P_{\\rm FA}$')
plt.ylabel('$P_{\\rm D}$')
plt.axis('equal')
plt.legend()

# This is to get axis equal and xlim, ylim, working simultaneously.
plt.gca().set_adjustable("box")

plt.xlim([-0.005, 1])
plt.ylim([0, 1.005])
plt.grid()
plt.savefig('Px06_ROC.png')
plt.show()
