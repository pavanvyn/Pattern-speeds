import os
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#number of image snapshots
num_files = 57

yst = 5

if not os.path.exists("speed_dat"):
	os.mkdir("speed_dat")

for index in range(num_files):
	with open("speed_dat/pattern_speed_%03d.dat" %(index),"w") as f:
		for st in range(-yst,yst+1):
			data = np.loadtxt("profile_dat/snapshot%03d/inter_profile_%d.dat" %(index,st),delimiter="\t")
			x_line = data[:,0]
			vel_line = data[:,1]
			den_line = data[:,2]

			# Simpson's rule integration
			x_sig_intg = integrate.simps(den_line*x_line,x_line,even="avg")
			v_sig_intg = integrate.simps(den_line*vel_line,x_line,even="avg")
			sig_intg = integrate.simps(den_line,x_line,even="avg")

			# normalized sky position and line of sight velocity w.r.t surface density
			x_avg = x_sig_intg/sig_intg
			v_avg = v_sig_intg/sig_intg
			f.write("%f\t%f\t%f\t%f\n" %(x_avg,v_avg,x_sig_intg,v_sig_intg))

	print("Pattern speed integration %d/%d iterations" %(index+1,num_files))