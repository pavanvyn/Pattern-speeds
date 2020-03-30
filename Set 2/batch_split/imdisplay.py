import os
from astropy.io import fits
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
 
path = "/home/pavan/Thesis/pattern_speed/Set 2/xQp55A-i30-10Rd/"

#making list of all surface density images
den_list = [file for file in os.listdir(path) if file.endswith('.den.DB.i30.fits')]
den_list = sorted(den_list)

#making list of all radial velocity images
vel_list = [file for file in os.listdir(path) if file.endswith('.vel.DB.i30.fits')]
vel_list = sorted(vel_list)

num_files = len(den_list)

if not os.path.exists("den_img"):
	os.mkdir("den_img")
if not os.path.exists("vel_img"):
	os.mkdir("vel_img")

for index in range(num_files):
	den_path = os.path.join(path, den_list[index])
	vel_path = os.path.join(path, vel_list[index])

	with fits.open(den_path) as den_hdul:
		den_data = den_hdul[0].data

	filename = den_list[index][:-16] #strips the end .den.DB.i30.fits

	with fits.open(vel_path) as vel_hdul:
		vel_data = vel_hdul[0].data

	# negative slope of slit (since Y axis in image is reversed)
	m = 0
	# centre of surface density
	y0 = 127
	x0 = 127
	# different slit translations
	yst = 50

	# contour smoothing factor
	sigma = 3
	
	# masking the 0 values in surface density profile and plotting log
	den_data = np.ma.array(den_data)
	ma_den_data = np.ma.masked_where(den_data == 0, den_data)
	sm_den_data = gaussian_filter(ma_den_data, sigma)
	plt.imshow(np.log(ma_den_data),cmap="gist_rainbow")
	plt.clim(-7,1)
	plt.colorbar()
	plt.contour(np.log(sm_den_data),np.arange(-5.5,0.5,0.5),colors="k",linewidths=0.5,linestyles="solid")
	for st in range(0,yst+1,5):
		if st == 0:			
			L = 10
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		if st == 15:
			L = 30
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		if st == 35:
			L = 50
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		plt.plot(x_slit,y_slit+st,color="black",linestyle="solid",linewidth=1)
		plt.plot(x_slit,y_slit-st,color="black",linestyle="solid",linewidth=1)
	plt.title("Log surface density profile")
	plt.xlim(0,255)
	plt.ylim(255,0)
	plt.savefig("den_img/den_"+filename+".png",bbox_inches = 'tight',pad_inches = 0.2)
	plt.close()
		
	# changing the -9999 values to 0 in velocity profile and plotting
	vel_data = np.ma.array(vel_data)
	vel_data = np.where(vel_data==-9999,0,vel_data)
	ma_vel_data = np.ma.masked_where(vel_data == 0, vel_data)
	sm_vel_data = gaussian_filter(ma_vel_data, sigma)
	plt.imshow(ma_vel_data,cmap="Spectral")
	plt.clim(-75,75)
	plt.colorbar()
	plt.contour(sm_vel_data,np.arange(-75,90,15),colors="k",linewidths=0.5,linestyles="solid")
	for st in range(0,yst+1,5):
		if st == 0:			
			L = 10
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		if st == 15:
			L = 30
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		if st == 35:
			L = 50
			x_slit = np.arange(x0-L,x0+L+1)
			y_slit = -m*(x_slit-x0) + y0
		plt.plot(x_slit,y_slit+st,color="black",linestyle="solid",linewidth=1)
		plt.plot(x_slit,y_slit-st,color="black",linestyle="solid",linewidth=1)
	plt.title("Radial velocity profile")
	plt.xlim(0,255)
	plt.ylim(255,0)
	plt.savefig("vel_img/vel_"+filename+".png",bbox_inches = 'tight',pad_inches = 0.2)
	plt.close()

	print("Image profiles display %d/%d iterations" %(index+1,num_files))