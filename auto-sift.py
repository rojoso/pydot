from PIL import Image
from numpy import *
from pylab import *
import os
import sift

imlist = os.listdir('pages')
nbr_images = len(imlist)
imlist_dir = [str('../pages/'+imlist[n]) for n in range(nbr_images)]

imname = [imlist[n][:-4] for n in range(nbr_images)]

os.mkdir('sifts')

os.chdir('sifts')

for n in range(nbr_images):
	sift.process_image(imlist_dir[n],str(imname[n]+'.sift'))



