import os
import pydicom
import matplotlib.pyplot as plt
import cv2
import csv
import numpy as np


def read_save_data(image,images_path, datalocation, save_folder_path):	
	ds = pydicom.dcmread(os.path.join(datalocation, image))
	convertedImg = ds.pixel_array   # store the raw image data

	# print(convertedImg.max())   # if = 4095: 2^12 >> the images are with 12 depth bit

	data = convertedImg.astype(np.float64) / np.amax(convertedImg) # normalize the data to 0 - 1
	convertedImg2 = 255 * data # Now scale by 255

	# save the image
	image = image.replace('.dcm', '.png')
	cv2.imwrite(os.path.join(save_folder_path, image), convertedImg2)

	# Show the image
	#plt.imshow(convertedImg2,cmap='gray')
	#plt.show()


def main(datalocation, save_folder_path, csv_file_location):

	images_path = os.listdir(datalocation)
	for n, image in enumerate(images_path):
		print(n)
		read_save_data(image,images_path, datalocation, save_folder_path)



if __name__ == "__main__":

	datalocation = '/media/azh2/Elements1/Azam/BreastData/Mammography_Dataset/DREAM_CHALLENGE/OriginalImages/'
	save_folder_path = '/media/azh2/Elements1/Azam/BreastData/Mammography_Dataset/DREAM_CHALLENGE/PNGs/'
	csv_file_location = '/media/azh2/Elements1/Azam/BreastData/Mammography_Dataset/DREAM_CHALLENGE' 

	main(datalocation, save_folder_path, csv_file_location)
