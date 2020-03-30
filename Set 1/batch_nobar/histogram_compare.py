import numpy as np
import matplotlib.pyplot as plt

# slope threshold
m_thr = 0.5

data = np.loadtxt("speed_var.dat")
dist = data[:,0]
# considering only the slopes (speeds) which have errrors less than threshold
m1 = data[:,1]
m1_err = data[:,2]
m1 = np.extract(m1_err<m_thr, m1)
m2 = data[:,3]
m2_err = data[:,4]
m2 = np.extract(m2_err<m_thr, m2)
m3 = data[:,5]
m3_err = data[:,6]
m3 = np.extract(m3_err<m_thr, m3)

bar_data = np.loadtxt("../batch/speed_var.dat")
bar_dist = bar_data[:,0]
bar_m = bar_data[:,1]
bar_m_err = bar_data[:,2]
bar_m = np.extract(bar_m_err<m_thr, bar_m)

thresholds = [np.mean(m1),np.mean(m3),np.mean(bar_m)]
bins = np.arange(-7.5,0.5,0.5)
colors = ['red','blue','black']
plt.title("Histogram of pattern speeds")
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.ylim(0,15)
plt.xlim(-8,0.5)
plt.hist([m1,m3,bar_m], bins=bins, histtype='stepfilled', alpha=0.6, color=['lightsalmon','skyblue','silver'], label=['Slits 16 to 30 spiral','Slits -16 to -30 spiral','Slits 15 to -15 bar only'], ec='black')
plt.vlines(thresholds, 0, 15, colors=colors, linestyles='dashed')
plt.legend()
plt.savefig("histogram_compare.png")
plt.close()