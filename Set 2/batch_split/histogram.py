import numpy as np
import matplotlib.pyplot as plt

# slope threshold
m_thr = 0.2

data = np.loadtxt("speed_var.dat")
dist = data[:,0]
# considering only the slopes (speeds) which have errrors less than threshold
m1_m5 = data[:,1]
m1_m5_err = data[:,2]
m1 = np.extract(m1_m5_err<m_thr, m1_m5)
m2_m4 = data[:,3]
m2_m4_err = data[:,4]
m2 = np.extract(m2_m4_err<m_thr, m2_m4)
m3 = data[:,5]
m3_err = data[:,6]
m3 = np.extract(m3_err<m_thr, m3)

bins = np.arange(-3.0,0,0.1)
fig,axs = plt.subplots(3,1,sharex=True,sharey=True)
fig.suptitle("Histogram of pattern speeds")
plt.ylim(0,60)
plt.xlim(-3.5,0.0)

axs[0].hist(m1_m5, bins=bins, histtype='bar', color='lightsalmon', label='Slits 31 to 50 and -31 to -50', ec='black')
axs[0].vlines(np.mean(m1_m5), 0, 60, colors='red', linestyles='dashed')
axs[0].legend(loc='upper left')

axs[1].hist(m2_m4, bins=bins, histtype='bar', color='skyblue', label='Slits 11 to 30 and -11 to -30', ec='black')
axs[1].vlines(np.mean(m2_m4), 0, 60, colors='saddlebrown', linestyles='dashed')
axs[1].legend(loc='upper left')

axs[2].hist(m3, bins=bins, histtype='bar', color='greenyellow', label='Slits -10 to 10', ec='black')
axs[2].vlines(np.mean(m3), 0, 60, colors='green', linestyles='dashed')
axs[2].legend(loc='upper left')

fig.text(0.5, 0.04, 'Pattern speed', ha='center')
fig.text(0.04, 0.5, 'Frequency', va='center', rotation='vertical')

plt.savefig("histogram.png")
plt.close()