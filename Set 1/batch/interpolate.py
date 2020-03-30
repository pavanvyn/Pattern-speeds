import os
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt

#number of image snapshots
num_files = 57

yst = 10

for index in range(num_files):
	for st in range(-yst,yst+1):
		data = np.loadtxt("profile_dat/snapshot%03d/profile_%d.dat" %(index,st),delimiter="\t")
		x_line = data[:,0]
		vel_line = data[:,1]
		den_line = data[:,2]

		# half-slit width
		L = 15.0

		# constrain to x_line -L to +L
		vel_line = vel_line[(x_line >= -L) & (x_line <= L)]
		den_line = den_line[(x_line >= -L) & (x_line <= L)]	
		x_line = x_line[(x_line >= -L) & (x_line <= L)]

		# interpolation functions
		vel_func = interpolate.CubicSpline(x_line,vel_line,extrapolate=False)
		den_func = interpolate.CubicSpline(x_line,den_line,extrapolate=False)

		# interpolated values (0.5 intervals)
		new_x_line = np.arange(-L,L+0.5,0.5)
		new_vel_line = vel_func(new_x_line)	
		new_den_line = den_func(new_x_line)
		new_vel_line = np.nan_to_num(new_vel_line)
		new_den_line = np.nan_to_num(new_den_line)

		np.savetxt("profile_dat/snapshot%03d/inter_profile_%d.dat" %(index,st),np.transpose([new_x_line,new_vel_line,new_den_line]),fmt="%f",delimiter="\t")

	print("Line profiles interpolation %d/%d iterations" %(index+1,num_files))