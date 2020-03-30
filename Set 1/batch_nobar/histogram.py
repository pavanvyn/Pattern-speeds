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

bins = np.arange(-7.0,0.5,0.25)
fig = plt.figure()
plt.suptitle("Histogram of pattern speeds")
plt.ylim(0,10)
plt.xlim(-7.5,0.5)

plt.subplot(3,1,1)
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.hist(m1, bins=bins, histtype='bar', color='lightsalmon', label='Slits 16 to 30', ec='black')
plt.vlines(np.mean(m1), 0, 10, colors='red', linestyles='dashed')
plt.legend()

plt.subplot(3,1,2)
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.hist(m2, bins=bins, histtype='bar', color='greenyellow', label='Slits 15 to -15', ec='black')
plt.vlines(np.mean(m2), 0, 10, colors='green', linestyles='dashed')
plt.legend()

plt.subplot(3,1,3)
plt.xlabel("Pattern speed")
plt.ylabel("Frequency")
plt.hist(m3, bins=bins, histtype='bar', color='skyblue', label='Slits -16 to -30', ec='black')
plt.vlines(np.mean(m3), 0, 10, colors='blue', linestyles='dashed')
plt.legend()

plt.savefig("histogram.png")
plt.close()