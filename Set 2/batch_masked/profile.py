import os
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
 
path = "/home/pavan/Thesis/pattern_speed/Set 2/xQp55A-i30-10Rd/"

#making list of all surface density images
den_list = [file for file in os.listdir(path) if file.endswith('.den.DB.i30.fits')]
den_list = sorted(den_list)

#making list of all radial velocity images
vel_list = [file for file in os.listdir(path) if file.endswith('.vel.DB.i30.fits')]
vel_list = sorted(vel_list)

#number of image snapshots
num_files = len(den_list)

if not os.path.exists("profile_dat"):
	os.mkdir("profile_dat")
if not os.path.exists("vel_profile"):
	os.mkdir("vel_profile")
if not os.path.exists("den_profile"):
	os.mkdir("den_profile")

for index in range(num_files):
	den_path = os.path.join(path, den_list[index])
	vel_path = os.path.join(path, vel_list[index])

	with fits.open(den_path) as den_hdul:
		den_data = den_hdul[0].data

	filename = den_list[index][:-16] #strips the end .den.DB.i30.fits

	with fits.open(vel_path) as vel_hdul:
		vel_data = vel_hdul[0].data
		
	# IN THIS IMAGE, VERTICAL AXIS IS Y AND HORIZONTAL AXIS IS X (NOT ALWAYS TRUE)

	xlen = den_data.shape[1]
	ylen = den_data.shape[0]

	# summation of surface density (weighted by x and y)
	tot = sum(sum(den_data))
	xtot = 0.
	ytot = 0.

	for y in range(ylen):	
		for x in range(xlen):
			xtot += x*den_data[y,x]
			ytot += y*den_data[y,x]

	# center of surface density
	x0 = int(xtot/tot)
	y0 = int(ytot/tot)

	#masking the bar region, radius 15px from (x0,y0)
	for y in range(ylen):	
		for x in range(xlen):
			dist = np.sqrt((x-x0)**2 + (y-y0)**2)
			if dist <= 25:
				den_data[y,x] = 0
				vel_data[y,x] = 0

	# half-slit width
	L = 50.0
	# different slit translations
	yst = 25
	# negative slope of slit (since Y axis in image is reversed)
	m = 0
	for st in range(-yst,yst+1):
		# choosing (x,y) in a slit passing through (x0,y0)
		line = []
		dist = []	
		x_line = []
		for y in range(ylen):
			for x in range(xlen):
				if (y-y0-st) == -m*(x-x0):
					line.append([x,y])
					if x!=x0:
						dist.append(np.sqrt((x-x0)**2+(y-y0-st)**2) * (abs(x-x0)/(x-x0)))
					else:
						dist.append(np.sqrt((x-x0)**2+(y-y0-st)**2))
					x_line.append(x-x0)

		if not os.path.exists("profile_dat/"+filename):
			os.mkdir("profile_dat/"+filename)
		with open("profile_dat/"+filename+"/profile_%d.dat" %(st),"w") as f:
			# velocity and density slit profiles
			vel_line = np.empty(len(line))
			den_line = np.empty(len(line))
			for i in range(len(line)):
				vel_line[i] = vel_data[line[i][1],line[i][0]]
				den_line[i] = den_data[line[i][1],line[i][0]]
				if vel_line[i] != -9999 and (dist[i] >= -L and dist[i] <= L):
					f.write("%f\t%f\t%f\n" %(x_line[i],vel_line[i],den_line[i]))

	print("Line profiles extraction %d/%d iterations" %(index+1,num_files))
