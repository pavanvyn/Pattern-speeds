import numpy as np
import matplotlib.pyplot as plt

# slope threshold
m_thr = 0.5

# 1 (km/s)/px = 3.2 (km/s)/kpc and inclination angle i = 30 deg
omg_fac = -3.2
i = np.pi/6

data = np.loadtxt("speed_var.dat")
dist = data[:,0]
# considering only the slopes (speeds) which have errrors less than threshold
m = data[:,1]
m_err = data[:,2]
m = np.extract(m_err<m_thr, m)

bins = np.arange(0.0,45.0,2.5)
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed ((km/s)/kpc)")
plt.ylabel("Bin frequency")
plt.ylim(0,8)
plt.xlim(0.0,45.0)
plt.hist(m*omg_fac/np.sin(i), bins=bins, histtype='bar', color='skyblue', label='Slits 15 to -15 spiral bar masked', ec='black')
plt.vlines(np.mean(m*omg_fac/np.sin(i)), 0, 10, color='blue', linestyles='dashed')
plt.legend()
plt.savefig("histogram.png")
plt.close()

print(np.mean(m*omg_fac/np.sin(i)))