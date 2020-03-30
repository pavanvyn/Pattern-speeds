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

bar_data = np.loadtxt("../batch/speed_var.dat")
bar_dist = bar_data[:,0]
bar_m = bar_data[:,1]
bar_m_err = bar_data[:,2]
bar_m = np.extract(bar_m_err<m_thr, bar_m)

thresholds = [np.mean(m),np.mean(bar_m)]
bins = np.arange(-7.5,0.5,0.5)
colors = ['green','black']
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.ylim(0,15)
plt.xlim(-8,0.5)
plt.hist([m,bar_m], bins=bins, histtype='stepfilled', alpha=0.7, color=['greenyellow','silver'], label=['Slits 15 to -15 spiral bar masked','Slits 15 to -15 bar only'], ec='black')
plt.vlines(thresholds, 0, 15, colors=colors, linestyles='dashed')
plt.legend()
plt.savefig("histogram_compare.png")
plt.close()