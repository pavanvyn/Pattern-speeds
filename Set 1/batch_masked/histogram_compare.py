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

bar_data = np.loadtxt("../batch_bar/speed_var.dat")
bar_dist = bar_data[:,0]
bar_m = bar_data[:,1]
bar_m_err = bar_data[:,2]
bar_m = np.extract(bar_m_err<m_thr, bar_m)

thresholds = [np.mean(m*omg_fac/np.sin(i)),np.mean(bar_m*omg_fac/np.sin(i))]
bins = np.arange(0.0,50.0,2.5)
colors = ['blue','green']
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed ((km/s)/kpc)")
plt.ylabel("Bin frequency")
plt.ylim(0,10)
plt.xlim(0.0,50.0)
plt.hist([m*omg_fac/np.sin(i),bar_m*omg_fac/np.sin(i)], bins=bins, histtype='stepfilled', alpha=0.7, color=['skyblue','greenyellow'], label=['Slits 15 to -15 spiral bar masked','Slits 15 to -15 bar only'], ec='black')
plt.vlines(thresholds, 0, 10, colors=colors, linestyles='dashed')
plt.legend()
plt.savefig("histogram_compare.png")
plt.close()