import numpy as np
import matplotlib.pyplot as plt

# slope threshold
m_thr = 0.2

# 1 (km/s)/px = 64/15 (km/s)/kpc and inclination angle i = 30 deg
omg_fac = -64./15.
i = np.pi/6

data = np.loadtxt("speed_var.dat")
dist = data[:,0]
# considering only the slopes (speeds) which have errrors less than threshold
m = data[:,1]
m_err = data[:,2]
m = np.extract(m_err<m_thr, m)

bins = np.arange(0.0,30.0,2.0)
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed ((km/s)/kpc)")
plt.ylabel("Bin frequency")
plt.ylim(0,50)
plt.xlim(0.0,30.0)
plt.hist(m*omg_fac/np.sin(i), bins=bins, histtype='bar', color='greenyellow', ec='black')
plt.vlines(np.mean(m*omg_fac/np.sin(i)), 0, 50, color='green', linestyles='dashed')
plt.savefig("histogram.png")
plt.close()