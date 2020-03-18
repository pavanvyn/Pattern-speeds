import numpy as np
import matplotlib.pyplot as plt

# slope threshold
m_thr = 0.5

data = np.loadtxt("speed_var.dat")
dist = data[:,0]
# considering only the slopes (speeds) which have errrors less than threshold
m = data[:,1]
m_err = data[:,2]
m = np.extract(m_err<m_thr, m)

bins = np.arange(-6.5,-2.5,0.25)
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.ylim(0,10)
plt.xlim(-7,-2.5)
plt.hist(m, bins=bins, histtype='bar', color='silver', ec='black')
plt.vlines(np.mean(m), 0, 25, color='black', linestyles='dashed')
plt.savefig("histogram.png")
plt.close()